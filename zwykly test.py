from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:

    MDBoxLayout:
        orientation: "vertical"

        MDTopAppBar:
            title: "MDLabel"

        MDLabel:
            text: "MDLabel"
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()