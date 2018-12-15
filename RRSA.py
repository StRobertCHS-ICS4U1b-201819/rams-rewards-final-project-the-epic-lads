from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.textinput import TextInput
from kivy.core.image import Image as CoreImage
import qrcode
student = {
    "firstName": "",
    "middleName": "",
    "lastName": "",
    "studentID":"",
    "homeRoom": ""
}



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
    BoxLayout:
        Button:
            text: 'Return'
            on_press: root.manager.current = 'main'
        Image:
            source: 'image.jpg'

<HistoryScreen>:
    BoxLayout:
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
    student_ID = StringProperty(student["studentID"])
    def on_start(self, *args):
        self.first_name = student["firstName"]
        self.middle_name = student["middleName"]
        self.last_name = student["lastName"]
        self.home_room = student["homeRoom"]
        self.student_ID = student["studentID"]
        print(student["firstName"])

class UpdateScreen(Screen):
    def goto_main(self, *args):
        student["firstName"] = self.ids.fname.text
        student["middleName"] = self.ids.mname.text
        student["lastName"] = self.ids.lname.text
        student["studentID"] = self.ids.SID.text
        student["homeRoom"] = self.ids.hroom.text
        print(student["firstName"])
        self.manager.current = 'main'

class QRScreen(Screen):
    KQR = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
    )
    KQR.add_data(student["studentID"])
    KQR.make(fit=True)
    img = KQR.make_image(fill_color="black", back_color="white")
    img.save("image.jpg")

class HistoryScreen(Screen):
    pass

sm = ScreenManager()
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

