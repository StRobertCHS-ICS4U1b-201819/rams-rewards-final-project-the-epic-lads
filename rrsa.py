"""
-------------------------------------------
Name: RRSA.py
Purpose:
This file contains the Student App of the Rams Rewards system.
Author: Varabei.A
Created: 9/12/18
-------------------------------------------
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.core.window import Window
from kivy.core.text import LabelBase
import qrcode
from kivy.uix.listview import ListItemButton
from kivy.uix.textinput import TextInput
from kivy.core.image import Image as CoreImage
import requests as req
import re
import datetime
from datetime import datetime
from kivy.uix.listview import ListItemButton


Window.clearcolor = (0, 0, 0, 1)
LabelBase.register(name = "KaushanSans",
    fn_regular =  "KaushanScript-Regular.otf"
    )
LabelBase.register(name = "QuickSand",
    fn_regular = "Quicksand-Regular.otf",
    fn_bold = "Quicksand-Bold.otf",
    fn_bolditalic= "Quicksand-BoldItalic.otf",
    fn_italic= "Quicksand-Italic.otf"
    )


pytime = str(datetime.now())
datelist = []
# student dictionary will be used to hold the user's information
student = {
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "student_ID": "",
    "homeRoom": ""
}


def make_Image():
    KQR = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4,
    )
    KQR.add_data(student["student_ID"])
    KQR.make(fit=True)
    img = KQR.make_image(fill_color="black", back_color="white")
    img.save("image.jpg")


# Kivy will be built in the python file since it is more convenient that way
Builder.load_string("""
<MainScreen>:
    GridLayout:
        rows: 4
        cols: 2
        
        Button:
         
        Button:

        Button:
            background_color: 3, .9, .85, .85
            size_hint: 1, .90
            font_size: 32
            bold: True      
            text: 'Check information '
            font_name: "QuickSand"
            on_press: root.manager.current = 'view'
     
        Button:
            background_color: 3, .9, .85, .85
            font_size: 32
            bold: True
            text: 'Update Information'
            font_name: "QuickSand"
            on_press: root.manager.current = 'update'
     
        Button:
            background_color: 2.2, .9, .85, .85

            text: 'View QR Code'
            font_name: "QuickSand"

            font_size: 32
            bold: True
            on_press: root.manager.current = 'qr'
       
        Button:
            background_color: 2.2, .9, .85, .85

            text: 'View History'
            font_name: "QuickSand"

            font_size: 32
            bold: True
            on_press: root.manager.current = 'history'
            
        FloatLayout:
            
            Button:
                pos: 0,0
                size_hint_x: 2
                text: 'Quit'
                font_name: "QuickSand"
    
                font_size: 32
                bold: True
                on_press: app.stop()
            
    FloatLayout:
        Button:
            readonly: True
            pos: 0,450
            background_color: 10, 10, 10, 10
            size_hint: 1, .26
            text: 'Rams Rewards'
            font_name: "KaushanSans"
            color: 0, 0, 0, 1
            font_size: 64
    
    FloatLayout:
        Image:
            source: 'logo.png'
            pos: -300, 240
            size: 10, 10
        Image:
            source: 'ecoschool.png'
            pos: 300, 240
            size: 10, 10
        
        Image:
            source: 'exit.png'
            pos: 0, -227
            
<UpdateScreen>:
    on_leave:
        root.on_quit()
    GridLayout:
        color: 0,0,0,0

        rows: 6
        cols: 2
        
        orientation: 'vertical'
        Button:
            text: "First name:"
            background_color: 3, .9, .85, .85
            font_size: 24

        TextInput: 
            size_hint_x: 0.35
            width: 100
            id: fname


        Button:
            text: "Middle name:"
            background_color: 3, .9, .85, .85
            font_size: 24
            
        TextInput:
            id: mname
            
        Button:
            text: "Last name:"
            background_color: 3, .9, .85, .85
            font_size: 24
            
        TextInput:
            id: lname
            
        Button:
            text: "Student ID:"
            background_color: 2.2, .9, .85, .85
            font_size: 24
            
        TextInput:
            id: SID
            
        Button:
            text: "Homeroom:"
            background_color: 2.2, .9, .85, .85
            font_size: 24
            
        TextInput:
            id: hroom
            
        FloatLayout:    
            Button:
                size_hint_x: 2
                text: 'Save and Return'
                font_size: 24
                on_press: root.goto_main()

<InformationScreen>:
    
    on_enter:
        root.on_start()
        
    GridLayout:
        rows: 7
        cols: 2

        Label: 
            text: 'First name: ' + root.first_name
            font_size: 24
        
        Label: 
            text: ' '
            
        Label:
            text: '  Middle name: ' + root.middle_name
            font_size: 24
  
        Label: 
            text: ' '
            
        Label: 
            text: 'Last name: ' + root.last_name
            font_size: 24
            
        Label: 
            text: ' '
            
        Label: 
            text: 'Student ID: ' + root.student_ID
            font_size: 24
        
        Label: 
            text: ' '
            
        Label: 
            text: 'Homeroom: ' + root.home_room
            font_size: 24
        
        Label: 
            text: ' '
            
        Label: 
            readonly: True
            text: 'Reward Points: '
            font_size: 24
        
        Label: 
            text: ' '
            
        FloatLayout:    
            Button:
                text: 'Return'
                font_size: 24
                size_hint_x:2
                color: 1,1,1,1
                bold: True
                background_color: 1, 1, 1, 1
                on_press: root.manager.current = 'main'
<QRScreen>:
    on_enter:
        root.on_QR()
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Return'
            font_size: 24
            on_press: root.manager.current = 'main'
        Image:
            source: 'image.jpg'
<HistoryScreen>:
    on_enter:
        root.on_history()
    BoxLayout:
        Label: 
            text: 'History:\\n' + root.history
        Button:
            text: 'Return'
            font_size: 24
            on_press: root.manager.current = 'main'

""")


class MainScreen(Screen):
    pass


class InformationScreen(Screen):
    first_name = StringProperty(student["firstName"])
    middle_name = StringProperty(student["middleName"])
    last_name = StringProperty(student["lastName"])
    home_room = StringProperty(student["homeRoom"])
    student_ID = StringProperty(student["student_ID"])

    def on_start(self, *args):
        self.first_name = student["firstName"]
        self.middle_name = student["middleName"]
        self.last_name = student["lastName"]
        self.home_room = student["homeRoom"]
        self.student_ID = student["student_ID"]
        print(student["firstName"])


class UpdateScreen(Screen):
    def goto_main(self, *args):
        student["firstName"] = self.ids.fname.text
        student["middleName"] = self.ids.mname.text
        student["lastName"] = self.ids.lname.text
        student["student_ID"] = self.ids.SID.text
        student["homeRoom"] = self.ids.hroom.text
        self.manager.current = 'main'

    def on_quit(self, *args):
        make_Image()


class QRScreen(Screen):
    def on_QR(self, *args):
        time = str(datetime.now())
        time = time[0:19]
        event = 'sample event'
        datelist.append(event + ':' + time)


class HistoryScreen(Screen):
    history = StringProperty('')

    def on_history(self, *args):
        h = ''
        i = 0
        while i < len(datelist):
            h = h + '\n' + datelist[i]
            i = i + 1
        self.history = h


sm = ScreenManager()
# Kivy screen management
sm.add_widget(MainScreen(name='main'))
sm.add_widget(InformationScreen(name='view'))
sm.add_widget(UpdateScreen(name='update'))
sm.add_widget(QRScreen(name='qr'))
sm.add_widget(HistoryScreen(name='history'))


class TestApp(App):
    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
