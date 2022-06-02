from fritzconnection import FritzConnection
from fritzconnection.lib.fritzstatus import FritzStatus
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.popup import Popup
from kivy.core.window import Window
from functools import partial
import os
from dotenv import load_dotenv


class Screen:
    def generate_box_layout(self):
        fc = FritzConnection(address=os.getenv('fritzbox_address'))

        layout = BoxLayout(orientation='vertical')
        btn1 = Button(text='Status')
        btn1.bind(on_press=partial(self.press_button, 'state', fc))
        btn2 = Button(text='WLAN an/aus')
        btn2.bind(on_press=partial(self.press_button, 'wlan', fc))
        btn3 = Button(text='WLAN QR Code')
        btn3.bind(on_press=partial(self.press_button, 'wlan_qr_code', fc))

        layout.add_widget(Label(text='Fritzbox Panel', color=(0, 0, 0)))
        layout.add_widget(btn1)
        layout.add_widget(btn2)
        layout.add_widget(btn3)

        return layout

    def press_button(self, value, fc, instance):
        if value == 'state':
            self.__get_state(fc)
        elif value == 'wlan_qr_code':
            self.__create_wlan_qr_code(fc)
        else:
            print('Nicht unterstütze Eigenschaft!')

    def __get_state(self, fc):
        fritz_state = FritzStatus(address=os.getenv('fritzbox_address'), password=os.getenv('fritzbox_password'))

        output = fc.modelname + ' - Version: ' + fc.system_version + '\n\nOnline: ' + 'Ja' if fritz_state.is_connected else 'Nein'
        popup_layout = BoxLayout(orientation='vertical')
        popup_layout.add_widget(Label(text=output))

        button = Button(text='Schließen')
        popup_layout.add_widget(button)

        popup = Popup(title='Status', content=popup_layout, auto_dismiss=False)
        button.bind(on_press=popup.dismiss)

        popup.open()

    def __create_wlan_qr_code(self, fc):
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
