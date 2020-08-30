# -*- coding: utf-8 -*-

from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import MDList
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.utils import platform

KV = '''
# Menu item in the DrawerList list.
Screen:
    screen_manager: screen_manager
    nav_drawer: nav_drawer
    NavigationLayout:
        ScreenManager:
            id: screen_manager
            Screen:
                id: camera_screen
                name: "camera_screen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Camera'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    Widget:
                MDLabel:
                    text: "Camera"
                    halign: "center"

            Screen:
                id: gallery_screen
                name: " gallery_screen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Gallery'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    Widget:
                MDLabel:
                    text: "Gallery"
                    halign: "center"

            Screen:
                id: signin_screen
                name: "signin_screen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Signin (Beta)'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    Widget:
                MDLabel:
                    text: "Signin (Beta)"
                    halign: "center"

            Screen:
                id: google_screen
                name: "google_screen"
                BoxLayout:
                    orientation: 'vertical'
                    MDToolbar:
                        title: 'Google Photos (Beta)'
                        left_action_items: [["menu", lambda x: nav_drawer.toggle_nav_drawer()]]
                        elevation:10
                    Widget:
                MDLabel:
                    text: "Google Photos (Beta)"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer
            ContentNavigationDrawer:
                orientation: 'vertical'
                padding: "8dp"
                spacing: "8dp"
                AnchorLayout:
                    anchor_x: "center"
                    size_hint_y: None
                    height: avatar.height
                    Image:
                        id: avatar
                        size_hint: None, None
                        size: "100dp", "100dp"
                        source: "resources/doctor.png"
                MDLabel:
                    text: "Soichi Tamashiro"
                    font_style: "Subtitle1"
                    size_hint_y: None
                    height: self.texture_size[1]
                MDLabel:
                    text: "soichi.tamashiro@gmail.com"
                    size_hint_y: None
                    font_style: "Caption"
                    height: self.texture_size[1]
                ScrollView:
                    DrawerList:
                        id: md_list

                        MDList:
                            OneLineIconListItem:
                                id: camera_button
                                text: "Cámara"

                                on_release:
                                    root.nav_drawer.set_state("close")
                                    root.screen_manager.current = "camera_screen"

                                IconLeftWidget:
                                    icon: "camera"


                            OneLineIconListItem:
                                text: "Mis Fotos"

                                on_release:
                                    root.nav_drawer.set_state("close")
                                    root.screen_manager.current = " gallery_screen"

                                IconLeftWidget:
                                    icon: "image-search"


                            OneLineIconListItem:
                                text: "Signin (Beta)"

                                on_release:
                                    root.nav_drawer.set_state("close")
                                    root.screen_manager.current = "signin_screen"

                                IconLeftWidget:
                                    icon: "account-plus-outline"

                            OneLineIconListItem:
                                text: "Google Photos (Beta)"

                                on_release:
                                    root.nav_drawer.set_state("close")
                                    root.screen_manager.current = "google_screen"

                                IconLeftWidget:
                                    icon: "google-photos"
'''


class DemoApp(MDApp):
    nav_drawer = ObjectProperty()
    screen_manager = ObjectProperty()

    class ContentNavigationDrawer(BoxLayout):
        pass

    class DrawerList(ThemableBehavior, MDList):
        pass

    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""
        # Set the color of the icon and a text for the menu ItemDrawer
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color == self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color
        pass

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
        screen = Builder.load_string(KV)

        if platform == "android":
            print("Android detected. Requesting permissions")
            self.request_android_permissions()
        Window.bind(on_keyboard=self.key_input)
        self.theme_cls.accent_palette = 'Blue'
        return screen

    def key_input(self, window, key, scancode, codepoint, modifier):
        if key == 27:
            return True  # override the default behaviour
        else:           # the key now does nothing
            return False

    def on_start(self):
        pass


if __name__ == '__main__':
    DemoApp().run()
