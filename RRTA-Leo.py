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
            on_press: root.manager.current = 'rewards'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'back to menu'
            
        
<RewardsScreen>:
    GridLayout:
        cols: 3
        rows: 3
        font_size: 20
        Button:
            text: '1'
            font_size: 20
        Button:
            text: '2'
            font_size: 20
        Button:
            text: '3'
            font_size: 20
        Button:
            text: '4'
            font_size: 20
        Button:
            text: '5'
            font_size: 20
        Button:
            text: '6'
            font_size: 20
        Button:
            text: '7'
            font_size: 20
        Button:
            text: 'Deduct points'
            font_size: 20
        Button:
            text: 'Points Counter'
            font_size: 20
     
""")


class MenuScreen(Screen):
    pass


class ScanQRCodeScreen(Screen):
    pass


class RewardsScreen(Screen):
    pass



# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ScanQRCodeScreen(name='scanQRcode'))

sm.add_widget(RewardsScreen(name='rewards'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
