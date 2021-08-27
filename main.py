from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
MDScreen:
    MDBoxLayout:
        orientation: "vertical"

        MDToolbar:
            title: "Калькулятор ФИЗО"

        MDLabel:
            text: "Тут будет целое приложение"
            halign: "center"
    MDRectangleFlatButton:
        text: "Узнать баллы"
        theme_text_color: "Custom"
        text_color: 1, 0, 1, 1
        line_color: 0, 1, 1, 1
        pos_hint: {"center_x": .5, "y": .5}
'''


class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)
        return Builder.load_string(KV)



Test().run()
