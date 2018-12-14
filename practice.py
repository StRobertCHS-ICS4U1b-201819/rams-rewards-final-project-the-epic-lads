import kivy
kivy.require('1.9.0')

from kivy.app import App
from kivy.uix.pagelayout import PageLayout

class PageLayoutApp(App):

    def build(self):
        return PageLayout()

glApp = PageLayoutApp()
glApp.run()