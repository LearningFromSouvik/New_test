#from kivy.lang import Builder
from kivy.lang import Builder
from kivymd.app import MDApp
from kivymd.uix.snackbar import Snackbar
from kivy.uix.screenmanager import Screen,ScreenManager
from kivymd.uix.list import OneLineListItem

Buil_strng ='''
ScreenManager:
    First:
    Second:
<First>:
    name:'first'
    MDLabel:
        text:'Task'
        halign: 'center'
        font_style: 'H2'
        pos_hint:{'center_y':0.8}

    MDTextField:
        id : task_text1
        size_hint:(0.7,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.45}
        hint_text:'Enter your First Number'

    
    MDTextField:
        id : task_text2
        size_hint:(0.7,0.1)
        pos_hint:{'center_x':0.5,'center_y':0.35}
        hint_text:'Enter your Second Number'
    

    MDRaisedButton:
        text:'Add 2 Number'
        pos_hint: {'center_x':0.5,'center_y':0.20}
        on_press:
            app.addTask()
<Second>:
    name: 'second'
    MDLabel:
        id : result
        text:''
        halign: 'center'
        font_style: 'H2'
        pos_hint:{'center_y':0.8}

    MDRaisedButton:
        text: 'Back'
        pos_hint: {'center_x':0.3,'center_y':0.2}
        on_press:
            root.manager.current = 'first'
'''
class First(Screen):
    pass
class Second(Screen):
    pass


sm = ScreenManager()
sm.add_widget(First(name = 'first'))
sm.add_widget(Second(name = 'second'))


class NewApp(MDApp):
    def build(self):
        self.strng = Builder.load_string(Buil_strng)
        return self.strng

    def addTask(self):
        a = int(self.strng.get_screen('first').ids.task_text1.text)
        b = int(self.strng.get_screen('first').ids.task_text2.text)
        c=str(a+b)
        self.strng.get_screen('second').ids.result.add_widget(
                OneLineListItem(text = "Souvik"))


NewApp().run()