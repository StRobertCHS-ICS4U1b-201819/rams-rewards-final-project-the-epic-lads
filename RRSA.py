from kivy.app import App
from kivy.lang import Builder
from kivy.uix.screenmanager import ScreenManager, Screen
Builder.load_string("""
<MainScreen>:
    BoxLayout:
        Button:
            text: 'Check information'
            on_press: root.manager.current = 'view'
        Button:
            text: 'Update Information'
            on_press: root.manager.current = 'update'
        Button:
            text: 'View QR Code'
            on_press: root.manager.current = 'qr'
        Button:
            text: 'View History'
            on_press: root.manager.current = 'history'
        Button:
            text: 'Quit'
            on_press: App.get_running_app().stop() 

<InformationScreen>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press: root.manager.current = 'main'

<UpdateScreen>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press: root.manager.current = 'main'

<QRScreen>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press: root.manager.current = 'main'

<HistoryScreen>:
    BoxLayout:
        Button:
            text: 'Back'
            on_press: root.manager.current = 'main'
""")


class MainScreen(Screen):
    pass

class InformationScreen(Screen):
    pass

class UpdateScreen(Screen):
    pass

class QRScreen(Screen):
    pass

class HistoryScreen(Screen):
    pass

sm = ScreenManager()
sm.add_widget(MainScreen(name='main'))
sm.add_widget(InformationScreen(name='view'))
sm.add_widget(UpdateScreen(name='update'))
sm.add_widget(QRScreen(name='qr'))
sm.add_widget(HistoryScreen(name='history'))

class TestApp(App):

    def build(self):
        return sm

if __name__ == '__main__':
    TestApp().run()

