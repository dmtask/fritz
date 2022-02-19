import kivy

from fritzconnection import FritzConnection
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label

class Screen(GridLayout):
    def __init__(self, **kwargs):
        super(Screen, self).__init__(**kwargs)

        #fc = FritzConnection(address='192.168.178.1')

        layout = BoxLayout(orientation='horizontal')
        btn1 = Button(text='Status')
        btn2 = Button(text='WLAN an/aus')

        layout.add_widget(Label(text='Fritzbox Panel'))
        layout.add_widget(btn1)
        layout.add_widget(btn2)

class Fritz(App):
    def build(self):
        return Screen()

if __name__ == '__main__':
    Fritz().run()