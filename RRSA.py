from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.textinput import TextInput

Builder.load_string("""
<MainScreen>:
    BoxLayout:
        id: fname
        orientation: 'vertical'
        Button:
            text: 'Check information'
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
    BoxLayout:
        orientation: 'vertical'
        Label: 
            text: 'Firstname: '
        Label:
            text: 'Middlename: '
        Label: 
            text: 'Lastname: '
        Label: 
            text: 'Student ID: '
        Label: 
            text: 'Homeroom: '
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

<HistoryScreen>:
    BoxLayout:
        Button:
            text: 'Return'
            on_press: root.manager.current = 'main'
""")


class MainScreen(Screen):
    pass

class InformationScreen(Screen):
    pass

class UpdateScreen(Screen):
    def goto_main(self, *args):
        self.manager.current = 'main'

class QRScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(InformationScreen(name='view'))
sm.add_widget(UpdateScreen(name='update'))
sm.add_widget(QRScreen(name='qr'))
sm.add_widget(HistoryScreen(name='history'))

class TestApp(App):
    #firstname = StringProperty('XXX')
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

