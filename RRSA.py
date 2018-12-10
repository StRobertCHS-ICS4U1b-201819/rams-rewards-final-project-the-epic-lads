import kivy
kivy.require('1.10.1')

from kivy.app import App
from kivy.uix.button import Label

class Student(object):

    def __init__(self):
        self.points = 0
        self.firstname = ''
        self.middlename = ''
        self.lastname = ''
        self.homeroom = ''
        self.studentID = 0

    def set_name(self, fname, mname, lname):
        self.firstname = fname
        self.middlename = mname
        self.lastname = lname

    def add_points(self, Points):
        holder = self.points + Points
        self.points = holder

    def set_homeroom(self, hroom):
        self.homeroom = hroom

    def set_studentID(self, sID):
        self.studentID = sID


class RRSA(App):
    def build(self):
        return Label(text="RRSA")

runapp = RRSA()

runapp.run()


