import kivy

from fritzconnection import FritzConnection
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.core.window import Window
from functools import partial
import os
from dotenv import load_dotenv


class Screen:
    def generate_box_layout(self):
        # fc = FritzConnection(address=os.getenv('fritzbox_address'))

        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Status')
        btn1.bind(on_press=partial(self.press_button, 'state'))
        btn2 = Button(text='WLAN an/aus')
        btn2.bind(on_press=partial(self.press_button, 'wlan'))
        btn3 = Button(text='WLAN QR Code')
        btn3.bind(on_press=partial(self.press_button, 'wlan_qr_code'))

        layout.add_widget(Label(text='Fritzbox Panel', color=(0, 0, 0)))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

    def press_button(self, value, instance):
        print(instance)

        if value == 'state':
            self.__get_state()
        elif value == 'wlan':
            self.__wlan()
        else:
            print('Nicht unterstütze Eigenschaft!')

    def __get_state(self):
        print('state')

    def __wlan(self):
        print('wlan')


class Fritz(App):
    def build(self):
        # Load .env File
        load_dotenv()

        # Das Fenster soll einen weißen Hintergrund haben
        Window.clearcolor = (1, 1, 1, 1)

        return Screen().generate_box_layout()


if __name__ == '__main__':
    Fritz().run()
