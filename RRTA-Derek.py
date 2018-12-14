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
from kivy.uix.behaviors import FocusBehavior
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
Window.clearcolor = (0, 0.75, 1, 1)
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
    display: entry
    GridLayout:
        cols: 3
        rows: 5
        spacing: 5
        padding: 5
        Button:
            background_color: 0,0,0,0
            text: 'Points'
            font_size: 50
            color: 0,0,0,0
        TextInput: 
            input_filter: 'int'
            background_color: 0,0,0,0
            outline_color: 0,0,0,0
            id: entry
            font_size: 40   
        Button:
            background_color: 0,0,0,0
        Button:
            text: 'Join a club (5 points)'
            padding: 25,0
            text_size: 250,None
            font_size: 20
            on_press: entry.int += 5
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
        
        Button:
            text: 'Quit'
            font_size: 20
            on_press: app.stop()         
        
""")


# Declare both screens


class MenuScreen(Screen):
    pass


class SettingsScreen(Screen):
    pass


class LeoScreen(Screen):
    def points(self, adding):
        if adding:
                self.display.text = str(eval(adding))




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
