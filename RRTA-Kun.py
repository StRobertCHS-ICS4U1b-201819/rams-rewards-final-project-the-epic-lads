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
        cols: 2
        rows: 1
        padding: 27
        spacing: 27
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
            on_press: root.manager.current = 'qrimage'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<-FullImage>:
    canvas:
        Color:
            rgb: (1, 1, 1)
        Rectangle:
            texture: self.texture
            size: self.width + 20, self.height + 20
            pos: self.x - 10, self.y - 10
""")


# Declare both screens


class MenuScreen(Screen):
    pass


class ScanQRCodeScreen(Screen):
    pass


class FullImage(Image):
    pass


#class QrPicScreen(Screen):
#    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ScanQRCodeScreen(name='scanQRcode'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
