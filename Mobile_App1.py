from kivy.app import App
from kivy.uix.label import label
from kivy.uix.floatlayout import floatlayout

class MyApp(App):
	def build(self):
		layout = FloatLayout()
		label1 = Label(text="Hello, I am Souvik.", size_hint=(0.3,0.2), pos_hint={'center_x':0.2, 'center_y':0.5})
		label2 = Label(text="Hello, I am Suvo.", size_hint=(0.5,0.2), pos_hint={'center_x':0.5, 'center_y':0.1})

		layout.add_widget(label1)
		layout.add_widget(label2)

		return layout

if __name__ == '__main__':
	MyApp().run()


