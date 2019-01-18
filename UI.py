import webcrawler as wbc
import filehandler as fh
import sys
import kivy
import wx
kivy.require('1.10.1')
from kivy.core.window import Window
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty

window_width = 700
window_height = 700
padding = 20

background_red = 0.9, 0.1, 0.15, 1
results_background = 0.85, 0.15, 0.2, 1
text_input_color = 1, 1, 1, 0.5
button_col = 0.7, 0.8, 0.8, 1
black = 0, 0, 0, 1
# 0.7, 0.8, 0.8, 1 white
'''
# used to allow to draw window if sdl2 cannot provide window
import os
def resourcepath():
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS)
    return os.path.join(os.path.abspath("."))


kivy.resources.resource_add_path(resourcepath())
'''

app = wx.App(False)
wxwidth, wxheight = wx.GetDisplaySize()

Window.size = (window_width, window_height)
Window.top = int(wxheight/2 - window_height/2)
Window.left = int(wxwidth/2 - window_width/2)
Window.borderless = True
Window.clearcolor = background_red  # stops black flicker on transition


fh.startup()    # begin file handler

name, address, stop = fh.get_all_data()


gui = f"""

AppScreenManager:
    MainScreen:
        name: 'main'
        id: main_id
    PopScreen:
        name: 'pop'
        id: ps_id
    EditScreen:
        name: 'edit'
        id: edit_id

<MainScreen>:
    canvas.before:
        Color:
            rgb: {background_red}
        Rectangle:
            pos: self.pos
            size: self.size

    BoxLayout:
        orientation: 'vertical'  
        spacing: 3            
        AnchorLayout:
            size_hint: 1, 0.045
            anchor_x: 'right'
            anchor_y: 'top'
            Button:
                text: 'x'
                color: {button_col}
                background_color: {black}
                background_normal: ''
                size_hint_y: 1 
                size_hint_x: 0.05
                on_release:
                    root.exit()
        GridLayout:
            size_hint: 1, 0.945
            cols: 3
            rows: 3
            spacing: 3
            padding: {padding}, 0, {padding}, {padding}
    
            Button:
                text: root.b_t0
                color: {black}
                background_color: {button_col}
                background_normal: ''
                font_size: 20
                text_size: self.width, None
                id: b0
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(0)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'
            Button:
                text: root.b_t1
                font_size: 20
                color: {black}
                background_color: {button_col}
                background_normal: ''
                text_size: self.width, None
                id: b1
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(1)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'                
            Button:
                text: root.b_t2
                color: {black}
                background_color: {button_col}
                background_normal: ''
                text_size: self.width, None
                id: b2
                font_size: 20
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(2)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'        
            Button:
                text: root.b_t3
                color: {black}
                background_color: {button_col}
                background_normal: ''
                font_size: 20
                text_size: self.width, None
                id: b3
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(3)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'        
            Button:
                text: root.b_t4
                color: {black}
                background_color: {button_col}
                background_normal: ''
                font_size: 20
                text_size: self.width, None
                id: b4
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(4)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'       
            Button:
                text: root.b_t5
                color: {black}
                background_color: {button_col}
                background_normal: ''
                id: b5
                font_size: 20
                text_size: self.width, None
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(5)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'        
            Button:
                text: root.b_t6
                color: {black}
                background_color: {button_col}
                background_normal: ''
                font_size: 20
                text_size: self.width, None
                id: b6
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(6)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'    
            Button:
                text: root.b_t7
                color: {black}
                background_color: {button_col}
                background_normal: ''
                font_size: 20
                text_size: self.width, None
                id: b7
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(7)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'    
            Button:
                text: root.b_t8
                color: {black}
                background_color: {button_col}
                background_normal: ''
                font_size: 20
                text_size: self.width, None
                id: b8
                size_hint_y: {window_height/9}
                size_hint_x: {window_width/3}
                halign: 'center'
                valign: 'top'
                on_press:
                    app.main_callback(8)
                    root.manager.transition.direction = 'down'
                    root.manager.current='pop'
<PopScreen>:
    canvas.before:
        Color:
            rgb: {background_red}
        Rectangle:
            pos: self.pos
            size: self.size
    FloatLayout:
        Button:
            text: 'X'
            pos: {padding}, {window_height - 4*padding}
            color: {black}
            background_color: {button_col}
            background_normal: ''
            size_hint: .09, .09
            on_press:
                root.manager.transition.direction = 'up'
                root.manager.current='main'
        AnchorLayout:
            anchor_x: 'left'
            anchor_y: 'top'
            Label:
                text: 'Stop: ' + root.current_address+'     Watching: '+ root.current_bus_name
                color: {black}
                font_size: 19
                size_hint: 0.9, 0.3 
                # pos: 0, {.09 * window_height + 5* padding }
        
        AnchorLayout:
            anchor_x: 'right'
            anchor_y: 'top'
            Label:
                color: {black}
                text: root.current_stop_num
                font_size: 18
                size_hint: None, None
        
        Label:
            canvas.before: 
                Color: 
                    rgb: {results_background}
                Rectangle: 
                    pos: self.pos 
                    size: self.size 
            text: root.results
            color: {black}
            valign:'top'
            halign:'left'
            size_hint: 0.75, 0.6
            text_size: self.size
            pos: {4* padding}, 150
            multiline: True
                        
        Button:
            text: '>'
            color: {black}
            background_color: {button_col}
            background_normal: ''
            pos: {window_width - 4*padding}, {window_height/2 + padding}
            size_hint: .09, .09
            font_size: 17
            on_press:
                root.manager.transition.direction = 'left'
                root.manager.current='edit'
<EditScreen>:
    canvas.before:
        Color:
            rgb: {background_red}
        Rectangle:
            pos: self.pos
            size: self.size
    Button:
        text: '<'
        color: {black}
        background_color: {button_col}
        background_normal: ''
        pos: {padding}, {window_height/2 + padding}
        size_hint: .09, .09
        font_size: 17
        on_press:
            app.update_main()
            root.manager.transition.direction = 'right'
            root.manager.current='pop'
    Label:
        text: 'Edit stop number:'
        color: {black}
        size_hint: 0.29, 0.1
        valign: 'center'
        halign: 'left'
        text_size: self.size
        font_size: 19
        pos: {window_width*0.3}, {window_height/2 + 0.1*window_height - 21}
    Label:
        text: 'Edit bus to watch:'
        color: {black}
        size_hint: 0.29, 0.1
        valign: 'center'
        halign: 'left'
        text_size: self.size
        font_size: 19
        pos: {window_width*0.3}, {window_height/2 -21}
    TextInput:
        id: change_num_id
        text: root.current_stop_num
        background_color: {text_input_color}
        background_normal: ''
        size_hint: 0.2, 0.1
        font_size: 19
        text_size: self.size
        padding_y: 24
        pos: {window_width*0.6 -21}, {window_height/2 + 0.1*window_height -20}
        multiline: False        
        on_text_validate:
            root.change_num()
            app.edit_callback()
            
    TextInput:
        id: change_name_id
        text: root.current_bus_name
        background_color: {text_input_color}
        background_normal: ''
        size_hint: 0.2, 0.1
        font_size: 19
        text_size: self.size
        padding_y: 24
        pos: {window_width*0.6 -21}, {window_height/2 -22}
        multiline: False
        on_text_validate:
            root.change_name()
            app.edit_callback()
            
    Button:
        text: 'list all buses'
        color: {black}
        background_color: {button_col}
        background_normal: ''
        pos: {3*padding}, 100
        size_hint: 0.16, 0.08
        font_size: 17
        on_press:
            root.displayall()
            
    Label:
        text: root.buslist
        color: {black}
        size_hint: 0.8, 0.1
        valign: 'center'
        halign: 'left'
        text_size: self.size
        font_size: 17
        pos: {3*padding}, {100 - 0.08*window_height}
        
                           
"""


class AppScreenManager(ScreenManager):
    pass


# Declare screens
class MainScreen(Screen):
    b_t0 = StringProperty(f'{name[0]} \n\n {address[0]}')
    b_t1 = StringProperty(f'{name[1]} \n\n {address[1]}')
    b_t2 = StringProperty(f'{name[2]} \n\n {address[2]}')
    b_t3 = StringProperty(f'{name[3]} \n\n {address[3]}')
    b_t4 = StringProperty(f'{name[4]} \n\n {address[4]}')
    b_t5 = StringProperty(f'{name[5]} \n\n {address[5]}')
    b_t6 = StringProperty(f'{name[6]} \n\n {address[6]}')
    b_t7 = StringProperty(f'{name[7]} \n\n {address[7]}')
    b_t8 = StringProperty(f'{name[8]} \n\n {address[8]}')

    def update_b_texts(self, index):
        v_name = f'b_t{index}'
        setattr(self, v_name, f'{name[index]} \n\n {address[index]}')

    def exit(self):
        sys.exit()
    pass


class PopScreen(Screen):
    current_stop_num = StringProperty('None')
    current_bus_name = StringProperty('None')
    current_address = StringProperty('None')
    results = StringProperty('None')

    def updatelabels(self, index):
        wbc_names, wbc_routes, wbc_times, wbc_address, wbc_diffs = wbc.next_times(stop[index], name[index])
        self.results = 'no information available for this querey'
        if wbc_names[0] != -1 and wbc_routes[0] != -1 and wbc_times[0] != -1:
            self.results = 'Bus{:_<9} Route{:_<27} Arrival Time{:_<15} \n'.format('', '', '')  # inserts blank strings
            for i in range(0, len(wbc_names)):
                self.results += f'{wbc_names[i]: <20} {wbc_routes[i]: <40} ' \
                                f'{wbc_times[i]: <20} : {wbc_diffs[i]:<0} Mins \n\n'

        self.current_stop_num = stop[index]
        self.current_address = wbc_address
        if self.current_address != address[index]:
            address[index] = self.current_address

        self.current_bus_name = name[index]
        fh.update_index(index, self.current_bus_name, self.current_stop_num, self.current_address)
        pass
    pass


class EditScreen(Screen):
    current_stop_num = StringProperty('None')
    current_bus_name = StringProperty('None')
    buslist = StringProperty('')
    edit_index = 0

    def updatelabels(self, index):
        self.current_bus_name = name[index]
        self.current_stop_num = stop[index]
        self.buslist = ''

    def change_name(self):
        name[self.edit_index] = self.ids.change_name_id.text
        # fh.update_name(index)

    def change_num(self):
        stop[self.edit_index] = self.ids.change_num_id.text
        if self.buslist != '':
            self.displayall()
        # fh.update_num(index)

    def displayall(self):
        if self.buslist == '' and self.current_stop_num != '':
            names = wbc.return_all(self.current_stop_num)
            res = ''
            for x in range(0, len(names)):
                res = res + '  ' + names[x]
            self.buslist = res
    pass


class TestApp(App):

    # bus name being search, e.g. 67, bus stop number e.g 495, address of bus stop eg. Westmoreland st
    current_index = -1

    def build(self):
        # return sm
        self.title = 'Bus times'
        return Builder.load_string(gui)

    def main_callback(self, index):
        self.current_index = index
        # this callback is here instead of being in the MainScreen class to access the root to use its attached ids
        self.root.ids.ps_id.updatelabels(index)
        self.root.ids.edit_id.buslist = ''
        self.root.ids.edit_id.updatelabels(index)
        self.root.ids.edit_id.edit_index = index
        # find the bus stop number from stops[index] and the searching for bus at bus_routes[index] read from file

    def edit_callback(self):
        self.root.ids.edit_id.edit_index = self.current_index
        self.root.ids.edit_id.updatelabels(self.current_index)
        self.root.ids.ps_id.updatelabels(self.current_index)

    def update_main(self):
        self.root.ids.main_id.update_b_texts(self.current_index)


if __name__ == '__main__':
    app_instance = TestApp()
    app_instance.run()

# use pyinstaller --noconsole -- onefile UI.py
