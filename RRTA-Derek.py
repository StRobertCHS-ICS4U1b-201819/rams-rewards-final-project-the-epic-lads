# Choose from a list of rewards activities (activities will have predetermined point values) to rewards points for
# (i.e Coding Club meeting, attend a basketball game, attend a dance.

import kivy

kivy.require('1.10.0')

from kivy.app import App
from kivy.uix.gridlayout import GridLayout


class GridApp(App):

    def build(self):
        return GridLayout


grApp = GridApp()

grApp.run()
