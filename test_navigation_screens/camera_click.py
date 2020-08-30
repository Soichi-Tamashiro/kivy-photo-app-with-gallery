'''
Camera Example
==============

This example demonstrates a simple use of the camera. It shows a window with
a buttoned labelled 'play' to turn the camera on and off. Note that
not finding a camera, perhaps because gstreamer is not installed, will
throw an exception during the kv language processing.

'''

# Uncomment these lines to see all the messages
# from kivy.logger import Logger
# import logging
# Logger.setLevel(logging.TRACE)

from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
import time
from android.storage import primary_external_storage_path
from kivymd.app import MDApp
from kivy.utils import platform
if platform == "android":
    primary_ext_storage = primary_external_storage_path()
Builder.load_string('''
<CameraClick>:
    id: main
    orientation: 'vertical'
    canvas.before:
        Color:
            rgba: (.06, .45, .45, 1)
        Rectangle:
            size: self.size
            pos: self.pos
    MDToolbar:
        title: "Camera App"
        md_bg_color: app.theme_cls.accent_dark
    MDLabel:
        text: ""
    BoxLayout:
        size_hint_y: None
        height: main.size[1]*.3
        RelativeLayout
            size_hint: None,None
            # size: 1920,1080
            size: 1900,1080
            canvas.before:
                Translate:
                    # x: 20
                    y: 1920
                Rotate:
                    angle: -90
                    axis: 0,0,1
                Color:
                    rgba: (.06, .45, .45, 1)
            Camera:
                id: camera
                resolution: (1920, 1080)
                keep_ratio: True
                allow_stretch: True
                play: True
                canvas.before:
                    Rectangle
                        size: self.size

    BoxLayout:
        orientation: 'vertical'
        size_hint_y: None
        height: main.size[1]*.1
        MDLabel:
            id: path_to_android
            text: "asasdad"
            size_hint_y: None
            height: main.size[1]*.05
        BoxLayout:
            orientation: 'horizontal'
            Button:
                text: 'Galería'
                # on_press: camera.play = not camera.play
                # size_hint_y: None
                # height: '48dp'
            Button:
                text: 'Captura'
                # size_hint_y: None
                # height: '48dp'
                on_press: root.capture()
''')


class CameraClick(BoxLayout):
    def capture(self):
        '''
        Function to capture the images and give them the names
        according to their captured time and date.
        '''
        camera = self.ids['camera']
        timestr = time.strftime("%Y%m%d_%H%M%S")
        # camera.export_to_png("IMG_{}.png".format(timestr))
        print("Captured")
        path_to_images = str(primary_ext_storage) + "/DCIM/Camera/"
        self.ids.path_to_android.text = path_to_images

        camera.export_to_png(path_to_images + "{}.jpg".format(timestr))


class TestCamera(MDApp):

    def build(self):
        Window.bind(on_keyboard=self.key_input)
        self.theme_cls.accent_palette = 'Blue'
        return CameraClick()

    def key_input(self, window, key, scancode, codepoint, modifier):
        if key == 27:
            return True  # override the default behaviour
        else:           # the key now does nothing
            return False


TestCamera().run()
