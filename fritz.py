import kivy

from fritzconnection import FritzConnection
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window

class Screen():
    def generateBoxLayout(self):
        #fc = FritzConnection(address='192.168.178.1')

        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Status')
        btn1.bind(on_press=self.pressBtn1())
        btn2 = Button(text='WLAN an/aus')

        layout.add_widget(Label(text='Fritzbox Panel', color=(0, 0, 0)))
        layout.add_widget(btn1)
        layout.add_widget(btn2)

        return layout

    def pressBtn1(self):
        print('Btn1')

        return ''

class Fritz(App):
    def build(self):
        Window.clearcolor = (1, 1, 1, 1)

        return Screen().generateBoxLayout()

if __name__ == '__main__':
    Fritz().run()