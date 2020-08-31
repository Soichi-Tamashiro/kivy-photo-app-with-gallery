# -*- coding: utf-8 -*-
from kivymd.app import MDApp
from kivy.lang import Builder
from kivymd.uix.boxlayout import MDBoxLayout
from kivy.core.window import Window
from kivy.utils import platform
from plyer import storagepath
Builder.load_string(
    '''
<Recetas>:
    orientation:'vertical'
    MDToolbar:
        title: 'Mis Recetas'
        md_bg_color: .2, .2, .2, 1
        specific_text_color: 1, 1, 1, 1

    MDBottomNavigation:
        panel_color: .2, .2, .2, 1

        MDBottomNavigationItem:
            name: 'signin_screen'
            text: 'Cuenta'
            icon: 'account-plus-outline'

            MDLabel:
                text: 'Mi Cuenta'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'camera_screen'
            text: 'Cámara'
            icon: 'camera'

            MDLabel:
                text: 'Mi Cámara'
                halign: 'center'

        MDBottomNavigationItem:
            name: 'gallery_screen'
            text: 'Mis Fotos'
            icon: 'image-search'

            MDLabel:
                text: 'Mis Fotos'
                halign: 'center'
            MDRaisedButton:
                text: 'Pictures'
                on_press: label.text = str(storagepath.get_pictures_dir())

'''
)


class Recetas(MDBoxLayout):
    pass


class MainApp(MDApp):

    def request_android_permissions(self):
        """
        Since API 23, Android requires permission to be requested at runtime.
        This function requests permission and handles the response via a
        callback.
        The request will produce a popup if permissions have not already been
        been granted, otherwise it will do nothing.
        """
        from android.permissions import request_permissions, Permission

        def callback(permissions, results):
            """
            Defines the callback to be fired when runtime permission
            has been granted or denied. This is not strictly required,
            but added for the sake of completeness.
            """
            if all([res for res in results]):
                print("callback. All permissions granted.")
            else:
                print("callback. Some permissions refused.")

        request_permissions([Permission.CAMERA,
                             Permission.READ_EXTERNAL_STORAGE,
                             Permission.WRITE_EXTERNAL_STORAGE], callback)
        # # To request permissions without a callback, do:
        # request_permissions([Permission.CAMERA,
        #                      Permission.READ_EXTERNAL_STORAGE,
        #                      Permission.WRITE_EXTERNAL_STORAGE])

    def build(self):
        self.theme_cls.primary_palette = "Blue"
        if platform == "android":
            print("Android detected. Requesting permissions")
            self.request_android_permissions()
        Window.bind(on_keyboard=self.key_input)
        self.theme_cls.accent_palette = 'Blue'
        return Recetas()

    def key_input(self, window, key, scancode, codepoint, modifier):
        if key == 27:
            return True  # override the default behaviour
        else:           # the key now does nothing
            return False

    def on_start(self):
        pass


if __name__ == '__main__':
    MainApp().run()
