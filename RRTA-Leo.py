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
            on_press: root.manager.current = 'subtract'

<CalcGridLayoutScreen>:
    # Where input is displayed
    BoxLayout:
        id: calculator
        display: entry
        rows: 5
        padding: 10
        spacing: 10
   
    BoxLayout:
        TextInput:
            id: entry
            font_size: 32
            multiline: False
 
    # When buttons are pressed update the entry
    GridLayout:
        rows: 5
        cols: 4
        spacing: 5
        Button:
            background_color: 0, 0, 0, 0
        Button:
            background_color: 0, 0, 0, 0
        Button:
            background_color: 0, 0, 0, 0
        Button:
            background_color: 0, 0, 0, 0
        Button:
            text: "7"
            on_press: entry.text += self.text
        Button:
            text: "8"
            on_press: entry.text += self.text
        Button:
            text: "9"
            on_press: entry.text += self.text
        Button:
            text: "+"
            on_press: entry.text += self.text
        Button:
            text: "4"
            on_press: entry.text += self.text
        Button:
            text: "5"
            on_press: entry.text += self.text
        Button:
            text: "6"
            on_press: entry.text += self.text
        Button:
            text: "-"
            on_press: entry.text += self.text
        Button:
            text: "1"
            on_press: entry.text += self.text
        Button:
            text: "2"
            on_press: entry.text += self.text
        Button:
            text: "3"
            on_press: entry.text += self.text
        Button:
            text: "*"
            on_press: entry.text += self.text
        Button:
            text: "AC"
            on_press: entry.text = ""
        Button:
            text: "0"
            on_press: entry.text += self.text
        Button:
            text: "="
            def calculate(self, calculation):
        if calculation:
            try:
                # Solve formula and display it in entry
                # which is pointed at by display
                self.display.text = str(eval(calculation))
            except Exception:
                self.display.text = "Error"

            on_press: calculator.calculate(entry.text)
            
            
        Button:
            text: "/"
            on_press: entry.text += self.text

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