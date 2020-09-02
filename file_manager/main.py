# -*- coding: utf-8 -*-
import os
import kivy
import kivymd
from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.core.window import Window
from kivymd.uix.filemanager import MDFileManager
from kivymd.toast import toast
from plyer import storagepath

KV = '''
BoxLayout:
    orientation: 'vertical'
    MDToolbar:
        title: "MDFileManager"
        # left_action_items: [['menu', lambda x: None]]
        elevation: 10
    FloatLayout:
        MDRoundFlatIconButton:
            text: "Open manager"
            icon: "folder"
            pos_hint: {'center_x': .5, 'center_y': .6}
            on_release: app.file_manager_open()
'''


class MainApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Window.bind(on_keyboard=self.events)
        self.manager_open = False
        self.file_manager = MDFileManager(
            exit_manager=self.exit_manager,
            select_path=self.select_path,
            previous=True,
        )

    def build(self):
        return Builder.load_string(KV)

    def file_manager_open(self):
        # self.file_manager.show('/')  # output manager to the screen
        self.file_manager.show(str(storagepath.get_pictures_dir()))
        self.manager_open = True

    def select_path(self, path):
        '''It will be called when you click on the file name
        or the catalog selection button.

        :type path: str;
        :param path: path to the selected directory or file;
        '''

        self.exit_manager()
        toast(path)

    def exit_manager(self, *args):
        '''Called when the user reaches the root of the directory tree.'''

        self.manager_open = False
        self.file_manager.close()

    def events(self, instance, keyboard, keycode, text, modifiers):
        '''Called when buttons are pressed on the mobile device.'''

        if keyboard in (1001, 27):
            if self.manager_open:
                self.file_manager.back()
        return True


if __name__ == "__main__":
    MainApp().run()
