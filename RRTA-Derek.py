# Choose from a list of rewards activities (activities will have predetermined point values) to rewards points for
# (i.e Coding Club meeting, attend a basketball game, attend a dance.
"""
import kivy

kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout



class GridLayoutApp(App):

    def build(self):
        return GridLayout()


grApp = GridLayoutApp()

grApp.run()
"""

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    FloatLayout:
        Button:
            background_color: 0, 0, 0, 0
            size_hint: (1, 1.5)
            text: 'Rams Rewards Teacher Admin App'
            font_size: 32
        
        Button:
            size_hint: (1, 0.5)
            text: 'Scan QR Code'
            font_size: 20
            on_press: root.manager.current = 'settings'
            
            


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
            text: 'no u'
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
