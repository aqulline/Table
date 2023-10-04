import json

from kivy.base import EventLoop
from kivy.properties import NumericProperty, StringProperty
from kivy.uix.image import Image
from kivymd.app import MDApp
from kivy.core.window import Window
from kivy.clock import Clock
from kivy import utils
from kivymd.toast import toast
from kivymd.uix.card import MDCard

from kivymd.uix.navigationdrawer import MDNavigationDrawer

Window.keyboard_anim_args = {"d": .2, "t": "linear"}
Window.softinput_mode = "below_target"
Clock.max_iteration = 250

if utils.platform != 'android':
    Window.size = (1920, 1016)
    Window.minimum_width, Window.minimum_height = Window.size


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
    all_programmes = {}
    all_programmes_count = StringProperty("0")
    specific_programme = StringProperty("")
    modules_count = StringProperty("0")
    programme_size = StringProperty("")
    all_modules = {}

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
                    "viewclass": "ProCard",
                    "name": self.all_modules[i],

                }
            )

    def load_module(self, programme):
        self.all_modules = self.all_programmes[programme]
        self.modules_count = str(len(self.all_modules))
        self.programme_size = str(self.get_programme_size(programme)[0])
        self.specific_programme = str(self.get_programme_size(programme)[1])

    """"

                  END  PROGRAMMES FUNCTIONS
        """

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
