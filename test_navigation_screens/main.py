# -*- coding: utf-8 -*-
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.properties import StringProperty

from kivymd.app import MDApp
from kivymd.theming import ThemableBehavior
from kivymd.uix.list import OneLineIconListItem, MDList
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.properties import StringProperty, ListProperty
KV = '''
# Menu item in the DrawerList list.
<ItemDrawer>:
    theme_text_color : "Custom"
    on_release:
        self.parent.set_color_item(self)
        # root.root.
    IconLeftWidget:
        id: icon
        icon: root.icon
        theme_text_color: "Custom"
        text_color: root.text_color

<ContentNavigationDrawer>:
    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "usb.png"
    MDLabel:
        text: "Gallery App"
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]
    MDLabel:
        text: "soichi.tamashiro@gmail.com"
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]
    ScrollView:

        DrawerList:
            id: md_list

Screen:

    NavigationLayout:

        ScreenManager:

            Screen:
                # id: camera
                name: "camera"
                BoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        title: "Camera and Gallery"
                        elevation: 10
                        left_action_items: [['menu', lambda x: nav_drawer.toggle_nav_drawer()]]

                    Widget:
            Screen:
                # id: gallery
                name: "gallery"
                MDLabel:
                    text: "Gallery"
                    halign: "center"

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                id: content_drawer

'''


class ContentNavigationDrawer(BoxLayout):
    pass


class ItemDrawer(OneLineIconListItem):
    icon = StringProperty()
    text_color = ListProperty((0, 0, 0, 1))


class DrawerList(ThemableBehavior, MDList):
    def set_color_item(self, instance_item):
        """Called when tap on a menu item."""

        # Set the color of the icon and a text for the menu ItemDrawer
        for item in self.children:
            if item.text_color == self.theme_cls.primary_color:
                item.text_color == self.theme_cls.text_color
                break
        instance_item.text_color = self.theme_cls.primary_color


class TestNavigationDrawer(MDApp):
    def build(self):
        return Builder.load_string(KV)

    def on_start(self):
        icons_item = {
            "camera": "Cámara",
            "image-search": "Mis Fotos",
            "account-plus-outline": "Signin (Beta)",
            "google-photos": "Google Photos (Beta)",
        }
        for icon_name in icons_item.keys():
            self.root.ids.content_drawer.ids.md_list.add_widget(
                ItemDrawer(icon=icon_name, text=icons_item[icon_name])
            )


if __name__ == '__main__':
    TestNavigationDrawer().run()
