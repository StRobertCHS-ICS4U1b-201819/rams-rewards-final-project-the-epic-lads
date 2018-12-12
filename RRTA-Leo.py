from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.clearcolor = (1, 0, 1, 0)

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        cols: 2
        rows: 1

       
        padding: 55
        
        Button:
            text: 'Goto settings'
            on_press: root.manager.current = 'settings'
        Button:
            text: "Exit"
            on_press: app.stop() 

<SettingsScreen>:
    GridLayout:
        cols: 2
        rows: 1
        Button:
            text: 'My settings button'
            on_press: root.manager.current = 'leo'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            
<LeoScreen>:
    GridLayout:
        cols: 2
        rows: 1
        Button:
            text: 'scan QR code'
            on_press: root.manager.current = 'settings'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
""")

# Declare both screens


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class LeoScreen(Screen):
    pass


# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(SettingsScreen(name='settings'))
sm.add_widget(LeoScreen(name='leo'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
