import ast
import os

import kivy
from kivy.config import ConfigParser, Config
from kivy.uix.screenmanager import ScreenManager, Screen

Config.set('graphics', 'resizable', 0)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.button import Button
from kivy.uix.widget import Widget
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.factory import Factory

Builder.load_file('C:/Users/Варвара/PycharmProjects/app-diet/MyApp.kv')


def callback(instance):
    print("ok")


class SearchScreen(Screen):
    pass


class AddIngrScreen(Screen):
    _app = ObjectProperty()

    def set_user_data(self, input_food):
        self._app.user_data = ast.literal_eval(self._app.config.get('General', 'user_data'))

    def get_data_foods(self):
        return ast.literal_eval(App.get_running_app().config.get('General', 'user_data'))

    def set_list_foods(self, data_foods):
        for f, d in sorted(data_foods.items(), key=lambda x: x[1]):
            fd = f.decode('u8')
            data = {'viewclass': 'Button', 'text': fd}
            if data not in self.ids.rv.data:
                self.ids.rv.data.append({'viewclass': 'Button', 'text': fd})

    def on_enter(self):
        data_foods = self.get_data_foods()
        self.set_list_foods(data_foods)

    def save_user_data(self):
        self._app.config.set('General', 'user_data')
        self._app.config.write()

    def set_new_food(self, name_food):
        self.ids.result_label.text = name_food

    def button_clicked(self, input_food):
        self.set_user_data(input_food)
        self.save_user_data()
        self.set_new_food(input_food)


class DietApp(App):
    def __init__(self, **kvargs):
        super(DietApp, self).__init__(**kvargs)

        self.config = ConfigParser()
        self.screen_manager = Factory.ManagerScreens()
        self.user_data = {}

    def build(self):
        Window.size = (360, 640)

        def build_config(self, config):
            config.adddefaultsection('General')
            config.setdefault('General', 'user_data', '{}')

        def set_value_from_config(self):
            self.config.read(os.path.join(self.directory, '%(appname)s.ini'))
            self.user_data = ast.literal_eval(self.config.get('General', 'user_data'))

        def get_application_config(self):
            return super(DietApp, self).get_application_config('{}/%(appname)s.ini'.format(self.directory))

        return self.screen_manager


if __name__ == "__main__":
    DietApp().run()
