import requests
import time

table_start_string = 'table id="rtpi-results"'.encode()  # encode to bytes for find() function
table_end_string = 'table id="rtpi-stops-key"'.encode()
due_instance_string = 'Due'.encode()
end_instance_string = ':'.encode()
all_stops_string = 'for="ctl00_FullRegion_MainRegion_ContentColumns_holder' \
                   '_RealTimeStopInformation1_cblRouteFilter_'.encode()

# table = ''      # make option to see all buses at that stop

def next_times(stop_id, bus_id):

    # global table
    # table = ''

    current_time = time.strftime('%H:%M')
    current_time = time.strptime(f'{current_time}', '%H:%M')
    busnames = []  # this handles variations in names eg. 67x
    routes = []
    times = []
    diffs = []
    url = f"http://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/" \
          f"?searchtype=view&searchquery={stop_id}"

    fullsource = requests.get(url).content
    address_start = fullsource.find("StopAddress".encode())
    fullsource = fullsource[address_start:]
    address_end = fullsource.find("<".encode())
    address = fullsource[13: address_end].decode()

    table_start = fullsource.find(table_start_string)

    table_end = fullsource.find(table_end_string)

    if table_start == -1 or table_end == -1:
        # this bus is not showing any real time information at this stop
        return [-1], [-1], [-1], address, diffs

    table = fullsource[table_start:table_end]   # make option to show entire table
    temp_table = table
    empty = 1
    while 1:

        if len(f"{temp_table}") == 3:
            break
        instance = temp_table.find(f' {bus_id}'.encode())
        if instance == -1:
            break

        temp_table = temp_table[instance:]
        due_instance = temp_table.find(due_instance_string)+4
        end_instance = temp_table.find(end_instance_string)+3

        if -1 < due_instance-4 < end_instance-3:  # next bus is due
            end_instance = due_instance

        data = temp_table[0:end_instance]

        busnames, routes, times = handle_data(data, busnames, routes, times)

        temp_table = temp_table[end_instance-3:]
        empty = 0

    if empty:
        return [-1], [-1], [-1], address, diffs

    for t in range(0, len(times)):
        if times[t] != ' Due\r':
            if len(times[t]) != 5:   # i.e times[t] == '' or other site information leaks through
                return [-1], [-1], [-1], address, []
            convert = time.strptime(times[t], '%H:%M')
            difference = abs(convert.tm_hour*60 + convert.tm_min - current_time.tm_hour*60 - current_time.tm_min)
            diffs.append(difference)
        else:
            diffs.append(0)
    return busnames, routes, times, address, diffs


def handle_data(data, busnames, routes, times):
    # bus name
    name_end = data.find("\r\n".encode())
    bus_name = data[0: name_end]
    busnames.append(bus_name.decode())

    # bus route
    for _ in range(0, 3):
        nextp = data.find("\r\n".encode()) + 4
        data = data[nextp:]
    data = data.decode()

    data = data[34:]
    n = []
    i = 0
    while i < len(data) and data[i] != '\r':
        n.append(data[i])
        i = i+1
    routes.append(''.join(n))

    # time
    t = data[-5:]
    times.append(t)
    return busnames, routes, times


def return_all(stop_id):
    # lists all routes that visit this stop
    url = f"http://www.dublinbus.ie/RTPI/Sources-of-Real-Time-Information/" \
          f"?searchtype=view&searchquery={stop_id}"

    fullsource = requests.get(url).content
    table_start = fullsource.find(all_stops_string)

    fullsource = fullsource[table_start:]
    table_end = fullsource.find("</table>".encode())
    fullsource = fullsource[:table_end]
    if table_end == -1 or table_start == -1:
        return [-1]  # stop is wrong
    names = append_all(fullsource)

    return names


def append_all(data):
    names = []

    while 1:
        start_instance = data.find(">".encode())
        end_instance = data.find("<".encode())
        if start_instance == -1 or end_instance == -1:
            break
        name = data[start_instance+1:end_instance]
        names.append(name.decode())
        data = data[end_instance:]
        start_instance = data.find(all_stops_string)
        data = data[start_instance:]

    return names
