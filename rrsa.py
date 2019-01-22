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
from kivy.uix.listview import ListItemButton
from kivy.uix.textinput import TextInput
from kivy.core.image import Image as CoreImage
import qrcode
import requests as req
import re
import datetime
from datetime import datetime
from kivy.uix.listview import ListItemButton

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
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Check information '
            on_press: root.manager.current = 'view'
        Button:
            text: 'Update Information'
            on_press: root.manager.current = 'update'
        Button:
            text: 'View QR Code'
            on_press: root.manager.current = 'qr'
        Button:
            text: 'View History'
            on_press: root.manager.current = 'history'
        Button:
            text: 'Quit'
            on_press: App.get_running_app().stop() 


<UpdateScreen>:
    on_leave:
        root.on_quit()
    BoxLayout:
        orientation: 'vertical'
        Label:
            text: "Firstname:" + fname.text 
        TextInput: 
            id: fname
        Label:
            text: "Middle name:" + mname.text
        TextInput:
            id: mname
        Label:
            text: "Last name:" + lname.text
        TextInput:
            id: lname
        Label:
            text: "Student ID:" + SID.text
        TextInput:
            id: SID
        Label:
            text: "Homeroom:" + hroom.text
        TextInput:
            id: hroom
        Button:
            text: 'Save and Return'
            on_press: root.goto_main()


<InformationScreen>:
    on_enter:
        root.on_start()
    BoxLayout:
        orientation: 'vertical' 
        Label: 
            text: 'Firstname: ' + root.first_name
        Label:
            text: 'Middlename: ' + root.middle_name
        Label: 
            text: 'Lastname: ' + root.last_name
        Label: 
            text: 'Student ID: ' + root.student_ID
        Label: 
            text: 'Homeroom: ' + root.home_room
        Label: 
            text: 'Reward Points: '
        Button:
            text: 'Return'
            on_press: root.manager.current = 'main'

<QRScreen>:
    on_enter:
        root.on_QR()
    BoxLayout:
        orientation: 'vertical'
        Button:
            text: 'Return'
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

