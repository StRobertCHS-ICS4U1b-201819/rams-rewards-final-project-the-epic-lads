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
from kivy.core.window import Window
Window.clearcolor = (0, 0.75, 1, 1)
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
            size_hint: (1.5, 0.5)
            text: 'Quit'
            font_size: 20
            on_press: app.stop() 
            
        Button:
            size_hint: (0.5, 0.5)
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
        cols:3
        rows:4
        
        Button:
            text: 'Join a club (5 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
        Button:
            text: 'Make it in a athletic team (10 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20

        Button:
            text: 'Attend a club/team meeting (1 point)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
            
        Button:
            text: 'Donate $5 for school charity events (once per event) (3 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
            
        Button:
            text: 'Place top 3 in cafeteria kahoot games (3 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
        
        Button:
            text: 'Participate in the Terry Fox turkey trot (5 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
        Button:
            text: 'Achieve a unit test mark of 85+ (2 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20

        Button:
            text: 'Achieve a course mark of 80 (4 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
        
        Button:
            text: 'Achieve a course mark of 90 (5 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
        
        Button:
            text: 'Achieve a course mark of 95+ (6 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
            
        Button:
            text: 'Deduct points'
            font_size: 20
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
