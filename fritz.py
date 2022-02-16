import kivy

from fritzconnection import FritzConnection
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        fc = FritzConnection(address='192.168.178.1')

        self.rows = 2
        self.add_widget(Label(text=fc.modelname))
        self.add_widget(Label(text='Hallo Welt...'))

class Fritz(App):
    def build(self):
        return Screen()

if __name__ == '__main__':
    Fritz().run()