from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.image import Image

Window.clearcolor = (0, 0.7, 1, 1)

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        rows: 2
        BoxLayout:
            padding: 10
            Button:
                background_color: 0, 0, 250, 255
                font_size: 32
                text: 'Rams Rewards'
        BoxLayout:
            spacing: 10
            padding: 10
            Button: 
                text: 'Scan QR Code'
                on_press: root.manager.current = 'scanQRcode'
            Button:
                text: "Exit"
                on_press: app.stop() 
<ScanQRCodeScreen>:
    GridLayout:
        cols: 2
        rows: 1
        padding: 27
        spacing: 27
        Button:
            text: 'Reward Your Students'
            on_press: root.manager.current = 'rewarding'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'

<RewardingScreen>:
    GridLayout:
        id: rewarding
        display: entry
        rows: 4
        spacing: 10
        padding: 10

        BoxLayout:
            Button: 
                text: 'Current Points:'
                background_color: 0,0,0,0
                font_color: 0,0,0,0
                font_size: 28
                size_hint_x: 0.35
                width: 100
            TextInput:
                id: entry
                font_size: 32
                multiline: False
                readonly: True

        BoxLayout:
            spacing: 10
            Button:
                text: "Join a Club (5 pts)"
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 5'))

            Button:
                text: 'Join Athletic Team (10 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 10'))
            Button:
                text: 'Attend a club/team meeting (1 pts)'
                padding: 25,0
                font_size: 11
                on_press: entry.text = str(eval(entry.text + '+ 1'))
            Button:
                text: 'Donate $5 for school (3 points)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 3'))
        BoxLayout:
            spacing: 10
            Button:
                text: 'Top 3 in cafeteria Kahoot (3 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 3'))
            Button:
                text: 'Participate Terry Fox Trot (5 pts)'
                padding: 25, 0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 5'))
            Button:
                text: 'Unit Test Mark: 85+ (2 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 2'))
            Button:
                text: 'Course Mark: 80+(4 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 4'))
        BoxLayout:
            spacing: 10
            Button:
                text: 'Course Mark: 90+ (5 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 5'))
            Button:
                text: 'Course Mark: 95+ (6 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 6'))
            Button:
                text: 'Deduct pts (-1 pts)'
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '- 1'))
            Button:
                text: 'Save and Quit'
                font_size: 12




<AreYouSureScreen>:
    GridLayout:
        rows: 2
        BoxLayout:
            padding: 10
            Button:
                background_color: 250, 0, 0, 25
                font_size: 32
                text: 'Are you sure about that?'
        BoxLayout:
            spacing: 10
            padding: 10
            Button: 
                text: 'Yes'
                on_press: root.manager.current = 'scanQRcode' 
            Button:
                text: "No"
                on_press: root.manager.current = 'rewarding' 
""")


# Declare screens
class MenuScreen(Screen):
    pass


class ScanQRCodeScreen(Screen):
    pass


class RewardingScreen(Screen):
    pass


class AreYouSureScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ScanQRCodeScreen(name='scanQRcode'))
sm.add_widget(RewardingScreen(name='rewarding'))
sm.add_widget(AreYouSureScreen(name='areyousure'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
