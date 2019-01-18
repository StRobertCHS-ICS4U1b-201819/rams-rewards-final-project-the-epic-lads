from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.floatlayout import FloatLayout
from kivy.properties import ObjectProperty
from kivy.uix.listview import ListItemButton
from kivy.uix.image import Image
from kivy.properties import NumericProperty
from QRcodeScanner import Scanner


Window.clearcolor = (1, 1, 1, 1)
LabelBase.register(name = "KaushanSans",
    fn_regular =  "KaushanScript-Regular.otf"
    )
LabelBase.register(name = "QuickSand",
    fn_regular = "Quicksand-Regular.otf",
    fn_bold = "Quicksand-Bold.otf",
    fn_bolditalic= "Quicksand-BoldItalic.otf",
    fn_italic= "Quicksand-Italic.otf"
    )

# Create both screens. Please note the root.manager.current: this is how
# you can control the ScreenManager from kv. Each screen has by default a
# property manager that gives you the instance of the ScreenManager used.
Builder.load_string("""
<MenuScreen>:
    GridLayout:
        rows: 4
        
        BoxLayout:
            Label:
                text: 'Rams Rewards'
                font_size: 60
                color: 0,0,0,1
                font_name: "KaushanSans"
                
        BoxLayout:
            Button:
                background_color: 3, .9, .85, .85
                size_hint: 1, .90
                font_size: 32
                text: 'Rams Rewards'
                font_name: "QuickSand"
                bold: True
                on_press: root.manager.current = "studentList"
              
        BoxLayout:
            Button: 
                background_color: 2.2, .9, .85, .85
                text: 'Scan QR Code'
                font_size: 32
                on_press: root.manager.current = 'scanQRcode'
                font_name: "QuickSand"
                bold: True
                
        BoxLayout:
            Button:
                background_color: 1.8, .9, .85, .85
                font_size: 32
                text: "Exit"
                on_press: app.stop() 
                font_name: "QuickSand"
                bold: True
                
    FloatLayout:
        Image:
            source: 'logo.png'
            pos: -300, 220
            size: 10, 10
        Image:
            source: 'ecoschool.png'
            pos: 300, 220
            size: 10, 10
        Image:
            source: 'rewards.png'
            pos: -300, 70
        Image:
            source: 'scan.png'
            pos: -300, -75
        Image:
            source: 'exit.png'
            pos: 0, -227
                    
<ScanQRCodeScreen>:
    GridLayout:
        cols: 2
        rows: 1
        padding: 27
        spacing: 27
        Button:
            text: 'Reward Your Students'
            on_press: root.manager.current = 'rewarding'
        Button:
            text: 'Back to menu'
            on_press: root.manager.current = 'menu'
<RewardingScreen>:
    GridLayout:
        id: rewarding
        display: entry
        rows: 4
        spacing: 10
        padding: 10
        BoxLayout:
            Button: 
                text: 'Current Points:'
                background_color: 0,0,0,0
                color: 0,0,0,0
                font_size: 28
                size_hint_x: 0.35
                width: 100
            TextInput:
                id: entry
                font_size: 32
                multiline: False
                readonly: True
        BoxLayout:
            spacing: 10
            Button:
                text: "Join a Club (5 pts)"
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 5'))
            Button:
                text: 'Join Athletic Team (10 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 10'))
            Button:
                text: 'Attend a club/team meeting (1 pts)'
                padding: 25,0
                font_size: 11
                on_press: entry.text = str(eval(entry.text + '+ 1'))
            Button:
                text: 'Donate $5 for school (3 points)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 3'))
        BoxLayout:
            spacing: 10
            Button:
                text: 'Top 3 in cafeteria Kahoot (3 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 3'))
            Button:
                text: 'Participate Terry Fox Trot (5 pts)'
                padding: 25, 0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 5'))
            Button:
                text: 'Unit Test Mark: 85+ (2 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 2'))
            Button:
                text: 'Course Mark: 80+(4 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 4'))
        BoxLayout:
            spacing: 10
            Button:
                text: 'Course Mark: 90+ (5 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 5'))
            Button:
                text: 'Course Mark: 95+ (6 pts)'
                padding: 25,0
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '+ 6'))
            Button:
                text: 'Deduct pts (-1 pts)'
                font_size: 12
                on_press: entry.text = str(eval(entry.text + '- 1'))
           
            Button:
                text: 'Save and Quit'
                font_size: 12
                on_press: entry.text = str(0)
                on_press: root.manager.current = 'areyousure'
                
<AreYouSureScreen>:
    GridLayout:
        rows: 2
        BoxLayout:
            padding: 10
            Button:
                background_color: 250, 0, 0, 25
                font_size: 32
                text: 'Are you sure about that?'
        BoxLayout:
            spacing: 10
            padding: 10
            Button: 
                text: 'Yes'
                on_press: root.manager.current = 'scanQRcode'
            Button:
                text: "No"
                on_press: root.manager.current = 'rewarding' 
            
<StudentListScreen>:
    orientation: "vertical"
    padding: 10
    spacing: 10
    GridLayout:
        rows: 4
        spacing: 10
        padding: 10
        BoxLayout:
            Label: 
                text: 'Last Name:'
                font_size: 28
                size_hint_z: 0.35
                width: 100
                color: 0,0,0,1
                font_name: "KaushanSans"
            TextInput:
                id: last_name
                font_size: 32
                multiline: False
            Label: 
                text: 'First Name:'
                font_size: 28
                size_hint_z: 0.35
                width: 100
                color: 0,0,0,1
                font_name: "KaushanSans"
            TextInput:
                id: first_name
                font_size: 32
                multiline: False
        
        BoxLayout:
            Button:
                background_color: .5,0.5,0.5,1
                text: 'Submit'
                font_size: 32
                on_press: 
            Button:
                background_color: .5,0.5,0.5,1
                text: 'Delete'
                font_size: 32
                on_press:
            Button:
                background_color: .5,0.5,0.5,1
                text: 'Replace'
                font_size: 32
                minimum_height: 0
                on_press: 
        BoxLayout:
        BoxLayout:
            Button:
                text: 'Back to menu'
                on_press: root.manager.current = 'menu'      
""")

# Declare screens
class MenuScreen(Screen):
    pass

class ScanQRCodeScreen(Screen):
    pass

class RewardingScreen(Screen):
    pass

class AreYouSureScreen(Screen):
    pass

class StudentListScreen(Screen):
    pass

class StudentDB(BoxLayout):
    first_name_text_input = ObjectProperty()
    last_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_student(self):
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
        self.student_list.adapter.data.extend([student_name])
        self.student_list._trigger_reset_populate()

    def delete_student(self, *args):
        if self.student_list.adapter.selection:
            selection = self.student_list.adapter.selection[0].text
            self.student_list.adapter.data.remove(selection)
            self.student_list._trigger_reset_populate()

    def replace_student(self, *args):
        if self.student_list.adapter.selection:
            selection = self.student_list.adapter.selection[0].text
            self.student_list.adapter.data.remove(selection)
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text
            self.student_list.adapter.data.extend([student_name])
            self.student_list._trigger_reset_populate()

# Create the screen manager
sm = ScreenManager()
sm.add_widget(MenuScreen(name='menu'))
sm.add_widget(ScanQRCodeScreen(name='scanQRcode'))
sm.add_widget(RewardingScreen(name='rewarding'))
sm.add_widget(AreYouSureScreen(name= 'areyousure'))
sm.add_widget(StudentListScreen(name= 'studentList'))

class TestApp(App):
    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()