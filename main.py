import json

from kivy import utils
from kivy.base import EventLoop
from kivy.clock import Clock
from kivy.core.window import Window
from kivy.metrics import dp
from kivy.properties import NumericProperty, StringProperty, DictProperty, ObjectProperty
from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDFlatButton, MDRaisedButton
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.dialog import MDDialog

import webbrowser
from database import DataBase as DB
from generate import Timetable as TB

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"
Clock.max_iteration = 250

if utils.platform != 'android':
    Window.size = (1920, 1016)
    Window.minimum_width, Window.minimum_height = Window.size


class Spin(MDBoxLayout):
    pass


class MainApp(MDApp):
    # app
    size_x, size_y = Window.size
    view_module = NumericProperty(9)
    add_module = NumericProperty(9)

    # screen
    screens = ['home']
    screens_size = NumericProperty(len(screens) - 1)
    current = StringProperty(screens[len(screens) - 1])

    # programmes
    all_programmes = DictProperty({})
    all_programmes_count = StringProperty("0")
    specific_programme = StringProperty("")
    selected_programme = StringProperty("")
    modules_count = StringProperty("0")
    programme_size = StringProperty("")
    all_modules = DictProperty({})
    deleted_module = StringProperty("")

    def on_start(self):
        Clock.schedule_once(self.keyboard_hooker, .1)

    def keyboard_hooker(self, *args):
        EventLoop.window.bind(on_keyboard=self.hook_keyboard)
        self.root.ids.nav_drawer.set_state("open")

    def hook_keyboard(self, window, key, *largs):
        print(self.screens_size)
        if key == 27 and self.screens_size > 0:
            print(f"your were in {self.current}")
            last_screens = self.current
            self.screens.remove(last_screens)
            print(self.screens)
            self.screens_size = len(self.screens) - 1
            self.current = self.screens[len(self.screens) - 1]
            self.screen_capture(self.current)
            return True
        elif key == 27 and self.screens_size == 0:
            toast('Press Home button!')
            return True

    """"
    
                PROGRAMMES FUNCTIONS
    """
    nodata = StringProperty("")
    dialog = ObjectProperty(None)

    def show_alert_dialog(self):
        if not self.dialog:
            self.dialog = MDDialog(
                title="Delete Module!",
                text=f"This module will be deleted permanently!",
                md_bg_color="#ABBEC4",
                type="simple",
                buttons=[
                    MDFlatButton(
                        text="CANCEL",
                        theme_text_color="Custom",
                        text_color="#626A68",
                        on_release=lambda x: self.dialog.dismiss()
                    ),
                    MDRaisedButton(
                        text="Accept",
                        # theme_text_color="Custom",
                        md_bg_color="#626A68",
                        on_release=lambda x: self.remove_module(self.deleted_module)
                    ),
                ],
            )
        self.dialog.open()

    def search_live(self, text):
        self.root.ids.programs.data = {}
        text = text.upper()
        for i in self.all_programmes:
            if text in i:
                self.nodata = ""
                self.root.ids.programs.data.append(
                    {
                        "viewclass": "ProCard",
                        "name": i,

                    }
                )
            else:
                self.nodata = "components/icons/no-data-found.png"

    def display_programmes(self):
        self.root.ids.programs.data = {}
        for i in self.all_programmes:
            self.root.ids.programs.data.append(
                {
                    "viewclass": "ProCard",
                    "name": i,

                }
            )

    def load_all_programmes(self):
        self.all_programmes = self.load("datas/module.json")
        self.all_programmes_count = str(len(self.all_programmes))

    def display_module(self):
        self.root.ids.modules.data = {}
        for i in self.all_modules:
            self.root.ids.modules.data.append(
                {
                    "viewclass": "ModCard",
                    "name": self.all_modules[i],
                    "pos_code": i

                }
            )

    def load_module(self, programme):
        self.selected_programme = programme
        self.all_modules = self.all_programmes[programme]
        self.modules_count = str(len(self.all_modules))
        self.programme_size = str(self.get_programme_size(programme)[0])
        self.specific_programme = str(self.get_programme_size(programme)[1])

    def add_modules(self, Mname, Mcode):
        if Mname != "" and Mcode != "":
            DB.add_module(DB(), self.selected_programme, Mname, Mcode)
            self.load_all_programmes()
            self.load_module(self.selected_programme)

    def remove_module(self, module):
        DB.remove_module(DB(), self.selected_programme, module)
        self.load_all_programmes()
        self.load_module(self.selected_programme)
        self.display_module()
        self.dialog.dismiss()

    """"

                  END  PROGRAMMES FUNCTIONS
        """

    """"
            TIME TABLES FUNCTIONS
    
    """

    exam_days = StringProperty("")
    table_time = StringProperty("")
    dialog_spin = ObjectProperty(None)

    table_fail = StringProperty("0")
    table_finish = StringProperty("0")
    table_succeed = StringProperty("0")

    table_notify = StringProperty("")
    buttons, data_tables = ObjectProperty(None), ObjectProperty(None)

    def spin_dialog(self):
        if not self.dialog_spin:
            self.dialog_spin = MDDialog(
                type="custom",
                auto_dismiss=False,
                size_hint=(.1, None),
                content_cls=Spin(),
            )
        self.dialog_spin.open()

    def get_days(self):
        day = TB.days

        for i in day:
            self.exam_days = f"{self.exam_days} {i},"

    def set_time(self, time_in, time_out, ranges):
        if time_in != "" and time_out != "" and ranges != "":
            table_time = TB.get_time(TB(), int(time_in), int(time_out), int(ranges))
            for i in table_time:
                self.table_time = f"{self.table_time} {i},"
        else:
            TB.table_time = []
            self.table_time = ""

    def generate_caller(self):
        if TB.table_time:
            self.spin_dialog()
            Clock.schedule_once(self.generate_timetable, 5)
        else:
            toast("Set Time!")

    def generate_timetable(self, *args):
        TB.generate_table(TB())
        self.dialog_spin.dismiss()
        self.table_finish = str(int(self.table_finish) + 1)
        self.table_succeed = str(int(self.table_succeed) + 1)
        self.table_notify = str("+1")


    def data_specific_table(self):
        num_rows = 6
        num_cols = 7
        row_data = []
        temp_code = {}
        data = self.load("datas/tble.json")


        for i in data[self.selected_programme]:
            period_one = data[self.selected_programme][i]["period_one_dt"]
            period_two = data[self.selected_programme][i]["period_two_dt"]

            if period_one not in temp_code:
                temp_code[period_one] = {}

            temp_code[period_one] = i

            if period_two not in temp_code:
                temp_code[period_two] = {}

            temp_code[period_two] = i
        # Generate the row_data
        for row_num in range(1, num_rows + 1):
            row = [TB.days[row_num-1]]
            for col_num in range(1, num_cols + 1):
                cell = f"d{row_num}t{col_num}"
                if cell in temp_code:
                    row.append(temp_code[cell])
                else:
                    row.append("----")
            row_data.append(tuple(row))
        return row_data

    def program_table(self):
        self.data_tables = MDDataTable(
            size_hint=(0.9, 0.6),
            background_color_header="#ABBEC4",
            use_pagination=True,
            column_data=[
                ("Days/Time", dp(30)),
                ("7:00-9:00", dp(60)),
                ("9:00-11:00", dp(60),),
                ("11:00-13:00", dp(60)),
                ("13:00-15:00", dp(60)),
                ("15:00-17:00", dp(60)),
                ("17:00-19:00", dp(60)),
                ("9:00-21:00", dp(60)),
            ],
            row_data=self.data_specific_table(),
            sorted_on="Schedule",
            sorted_order="ASC",
            elevation=2,
            pos_hint={"center_x": .5, "center_y": .6}
        )
        self.root.ids.below_box.add_widget(self.data_tables)
        self.buttons = MDRaisedButton(
            text="Close", on_release=self.view_tables,
            md_bg_color="#626A68",
            pos_hint={"center_x": .5, "center_y": .45}
        )
        self.root.ids.below_box.add_widget(self.buttons)

    def view_tables(self, instance):
        # Change the position of the table when the button is pressed
        if self.data_tables:
            if self.data_tables.pos_hint["center_x"] == 0.5:
                self.data_tables.pos_hint = {"center_x": 9, "center_y": .5}
                self.buttons.pos_hint = {"center_x": 9, "center_y": .5}
            else:
                self.data_tables.pos_hint = {"center_x": .5, "center_y": .5}



    """"
            END TABLES FUNCTIONS
    """

    def view_table(self):
        webbrowser.open("datas/table.html")

    def screen_capture(self, screen):
        sm = self.root.ids.manager
        sm.current = screen
        if screen in self.screens:
            pass
        else:
            self.screens.append(screen)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        print(f'size {self.screens_size}')
        print(f'current screen {screen}')

    def screen_leave(self):
        print(f"your were in {self.current}")
        last_screens = self.current
        self.screens.remove(last_screens)
        print(self.screens)
        self.screens_size = len(self.screens) - 1
        self.current = self.screens[len(self.screens) - 1]
        self.screen_capture(self.current)

    def load(self, name):
        with open(name, "r") as file:
            initial_data = json.load(file)
        return initial_data

    def get_programme_size(self, text):
        import re

        pattern = r'^(.*?)\s*\((\d+)\)$'

        match = re.match(pattern, text)

        if match:
            extracted_text = match.group(1).strip()
            extracted_number = match.group(2)

            return [extracted_number, extracted_text]
        else:
            print("No match found.")

    def build(self):
        pass


MainApp().run()
