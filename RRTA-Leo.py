from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.uix.image import Image
Window.clearcolor = (1, 1, 1, 1)

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
            on_press: root.manager.current = 'addsubpoints'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
            
<AddSubScreen>:
    BoxLayout:
        Button:
            text: "Add Points"
            on_press: root.manager.current = 'calculate'
        Button:
            text: "Deduct Points"

<CalcGridLayoutScreen>:
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


class MenuScreen(Screen):
    pass


class ScanQRCodeScreen(Screen):
    pass


class RewardsScreen(Screen):
    pass


class AddSubScreen(Screen):
    pass


class CalcGridLayoutScreen(Screen):
    pass

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ScanQRCodeScreen(name='scanQRcode'))
sm.add_widget(AddSubScreen(name='addsubpoints'))
sm.add_widget(RewardsScreen(name='rewards'))
sm.add_widget(CalcGridLayoutScreen(name='calculate'))


class TestApp(App):

    def build(self):
        return sm


if __name__ == '__main__':
    TestApp().run()
"""
< RewardsScreen >:
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
"""
