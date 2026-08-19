from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button

class MainUI(BoxLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.orientation = "vertical"
        self.add_widget(Label(text="1+1=", font_size=30))
        self.box = TextInput(hint_text="请输入答案", font_size=25)
        self.add_widget(self.box)
        btn = Button(text="提交", font_size=28)
        btn.bind(on_press=self.check)
        self.add_widget(btn)

    def check(self, obj):
        try:
            a = int(self.box.text)
            if a == 3:
                self.box.text = "成立"
            elif a != 3:
                self.box.text = "不成立"
        except ValueError:
            self.box.text = "bug被发现了😭"

class MyApp(App):
    def build(self):
        return MainUI()

MyApp().run()