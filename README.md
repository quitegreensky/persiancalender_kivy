# Persian(Jalali) calender for KivyMD/Kivy

<img align="center" width="256" src=""/>

## Installation

Use the package manager [pip](https://pip.pypa.io/en/stable/) to install package:

```bash
pip install git+https://github.com/quitegreensky/persiancalender_kivy.git
```

- In this case you must have the following requirements in your ```buildozer.spec```:
```
requirements =  kivy,kivymd, git+https://github.com/quitegreensky/persiancalender_kivy.git, git+https://github.com/MeirKriheli/python-bidi.git, git+https://github.com/mhajiloo/persiantools.git
```

Also you should copy and replace ```fonts``` folder with your existing KivyMD's fonts folders.
## Usage

```
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
```
 
## Contributing
Feel free to open issues and ask for help.

## License
[MIT](https://choosealicense.com/licenses/mit/)