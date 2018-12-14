from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MainScreen>:
    BoxLayout:
        Button:
            text: 'Check information'
            on_press: root.manager.current = 'view'
        Button:
            text: 'Quit'

<InformationScreen>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press: root.manager.current = 'main'
""")

# Declare both screens
class MainScreen(Screen):
    pass

class InformationScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(InformationScreen(name='view'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

