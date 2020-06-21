from kivymd.app import MDApp
from kivy.lang.builder import Builder 
from pcalender.datepicker_fa import DatePickerFa
from kivymd.toast import toast

kv='''
FloatLayout:
    MDRaisedButton:
        text: 'Open'
        pos_hint: {'center_x': .5, 'center_y': .5}
        on_release: app.open_calender()
'''

class TestApp(MDApp):

    def build(self):
        return Builder.load_string(kv)

    def open_calender(self):
        self.caleder= DatePickerFa(callback=self.calender_callback)
        self.caleder.open()

    def calender_callback(self,date):
        return toast(date)

TestApp().run()