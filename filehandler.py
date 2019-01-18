import os

pathname = os.path.join(os.path.expanduser('~'), 'bustimes\\')

dir_path = os.path.dirname(pathname)
f_path = os.path.join(dir_path, 'saves.txt')
readme_path = os.path.join(dir_path, 'README.txt')
readme_str = 'Hi! \n This is a small application I made to be able to track buses as an alternative to the usual ' \
             'Dublin Bus website. \n You can keep track of 9 different stops of your choice. \n ' \
             'This will be most useful if youre interested in a single bus route at each stop \n' \
             ' Enjoy! \nBy Brian N  https://github.com/tropical-BN - December 2018. \n '

def startup():
    if not os.path.exists(dir_path):
        os.makedirs(dir_path)
    # init blank files
    if not os.path.exists(f_path):
        f = open(f_path, 'w')
        for _ in range(0, 27):
            f.write('_\n')
        f.close()
    if not os.path.exists(readme_path):
        f = open(readme_path, 'w')
        f.write(readme_str)
        f.close()


def get_all_data():
    # reurns names, stops, addresses for initial loading of UI
    names, stops, address = [], [], []
    f = open(f_path, 'r')
    lines = f.readlines()    # list of all lines
    index = 0
    for _ in range(0, 9):
        n = lines[index]
        a = lines[index+1]
        s = lines[index+2]
        index += 3
        n = n[:-2]
        a = a[:-2]
        s = s[:-2]
        names.append(n)
        stops.append(s)
        address.append(a)
    f.close()
    return names, address, stops


def update_index(index, name, address, stop):
    # updates file to contain name, stop, address at a certain index
    f = open(f_path, 'r')
    lines = f.readlines()
    lines[3*index] = name + '_\n'
    lines[3*index + 1] = stop + '_\n'
    lines[3*index + 2] = address + '_\n'
    f = open(f_path, 'w')
    f.writelines(lines)
    f.close()


