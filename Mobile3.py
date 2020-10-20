from kivy.lang import Builder

from kivymd.app import MDApp

KV = '''
BoxLayout:
    padding: "20dp"
    
    MDProgressBar:
        value: 50
'''

class Test(MDApp):
    def build(self):
        return Builder.load_string(KV)


Test().run()
