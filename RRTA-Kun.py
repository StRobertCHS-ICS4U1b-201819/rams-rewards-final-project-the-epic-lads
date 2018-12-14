from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image

Window.clearcolor = (1, 1, 1, 1)

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
                on_press: root.manager.current = "menu"
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
            text: 'scan QR code'
            on_press: root.manager.current = 'qrpic'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<QRPicScreen>:

""")


# Declare both screens


class MenuScreen(Screen):
    pass


class ScanQRCodeScreen(Screen):
    pass


class QrPicScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ScanQRCodeScreen(name='scanQRcode'))
sm.add_widget(QrPicScreen(name='qrpic'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
