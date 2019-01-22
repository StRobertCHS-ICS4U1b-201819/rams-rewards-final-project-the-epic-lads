"""
--------------------------------
Name: RRTA.py
Purpose:
This file ocntains the Teacher App of the Rams Rewards System.
Author: Lee.K, Shat.D, Xiao.L
Created: 9/12/18
--------------------------------
"""
from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.window import Window
from kivy.core.text import LabelBase
from kivy.uix.popup import Popup
from kivy.uix.button import Button
from kivy.uix.label import Label

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
#: import main RRTA-Kun 
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
            size: 10, 10
            size_hint_x: .25
            size_hint_y: 1.7
        Image:
            source: 'ecoschool.png'
            size: 10, 10
            size_hint_x: 1.75
            size_hint_y: 1.7
            
        Image:
            source: 'rewards.png'
            size_hint_x: .25
            size_hint_y: 1.22
        Image:
            source: 'scan.png'
            size_hint_x: .25
            size_hint_y: .75
        Image:
            source: 'exit.png'
            size_hint_x: .98
            size_hint_y: .25
        
        Label: 
            text: '"Knowledge is the beginning"'
            font_size: 20
            color: 0,0,0,1
            font_name: "QuickSand"
            size_hint_x: 1
            size_hint_y: 1.58
                    
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
                color: 0,0,0,1
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
                on_press: root.open_popup()

               
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
                          
#: import ListAdapter kivy.adapters.listadapter.ListAdapter
#: import ListItemButton kivy.uix.listview.ListItemButton     
<StudentListScreen>:
    orientation: "vertical"
    first_name_text_input: first_name
    last_name_text_input: last_name
    student_list: students_list_view
    
    GridLayout:
        rows: 4
        spacing: 10
        padding: 10
        
        BoxLayout:
            size_hint_y: None
            height: "40dp"
     
            Label:
                text: "First Name"
                color: 0,0,0,1
                font_name: "KaushanSans"
            TextInput:
                id: first_name
            Label:
                text: "Last Name"
                color: 0,0,0,1
                font_name: "KaushanSans"
            TextInput:
                id: last_name
                                     
        BoxLayout:
            size_hint_y: None
            height: "40dp"
            Button:
                text: "Submit"
                size_hint_x: 15
                background_color: .5,0.5,0.5,1
                on_press: root.submit_students()
            Button:
                text: "Delete"
                size_hint_x: 15
                background_color: .5,0.5,0.5,1
                on_press: root.delete_students()
            Button:
                text: "Replace"
                size_hint_x: 15
                background_color: .5,0.5,0.5,1
                on_press: root.replace_student()
            Button:
                text: "Reward"
                size_hint_x: 15
                background_color: .5,0.5,0.5,1
                on_press: root.manager.current = 'rewarding'
            Button:
                text: 'Back to menu'
                size_hint_x: 15
                background_color: .5,0.5,0.5,1
                on_press: root.manager.current = 'menu'
    
        ListView:
            id: students_list_view
            adapter:
                ListAdapter(data=["Kun Lee"], cls=main.StudentListButton)
""")
class StudentListButton(ListItemButton):
    pass
# Declare screens
class MenuScreen(Screen):
    pass

class ScanQRCodeScreen(Screen):
    pass

class RewardingScreen(Screen):
    def open_popup(self):
        the_popup = CustomPopUp(title = 'hi')

        the_popup.add_widget(Label(text ='hello'))
        the_popup.open()


class AreYouSureScreen(Screen):
    pass

class StudentListScreen(Screen):
    first_name_text_input = ObjectProperty()
    first_name_text_input = ObjectProperty()
    student_list = ObjectProperty()

    def submit_students(self):
        # Get the student name from the TextInputs
        student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

        # Add the student to the ListView
        self.student_list.adapter.data.extend([student_name])

        # Reset the ListView
        self.student_list._trigger_reset_populate()

    def delete_students(self):
        # If a list item is selected
        if self.student_list.adapter.selection:
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Reset the ListView
            self.student_list._trigger_reset_populate()

    def replace_student(self):

        # If a list item is selected
        if self.student_list.adapter.selection:
            # Get the text from the item selected
            selection = self.student_list.adapter.selection[0].text

            # Remove the matching item
            self.student_list.adapter.data.remove(selection)

            # Get the student name from the TextInputs
            student_name = self.first_name_text_input.text + " " + self.last_name_text_input.text

            # Add the updated data to the list
            self.student_list.adapter.data.extend([student_name])

            # Reset the ListView
            self.student_list._trigger_reset_populate()

#other classes
class StudentListButton(ListItemButton):
    pass

class CustomPopUp(Popup):
    pass




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