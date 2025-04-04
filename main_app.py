# write your app here
from kivy.app import App
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextInput
from kivy.core.window import Window
from kivy.uix.scrollview import ScrollView
from instructions import txt_instruction, txt_test1, txt_test2, txt_test3, txt_sits
from ruffier import test

age = 7
name = ""
p1, p2, p3 = 0, 0, 0
class InstrScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_instruction)
        lbl1 = Label(text='Enter the name:', halign='right')
        self.in_name = TextInput(multiline=False)
        lbl2 = Label(text='Enter the age:', halign='right')
        self.in_age = TextInput(text='7',multiline=False)
        self.btn = Button(text='Start', size_hint=(0.3, 0.2), pos_hint={'center_x': 0.5})
        self.btn.on_press = self.next
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        line1.add_widget(lbl1)
        line1.add_widget(self.in_name)
        line2.add_widget(lbl2)
        line2.add_widget(self.in_age)
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global name
        name = self.in_name.text
        self.manager.current = 'pulse1'

class PulseScr(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        instr = Label(text=txt_test1)

        line = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result = Label(text='Enter the result:', halign='right')
        self.in_result = TextInput(text='0', multiline=False)

        line.add_widget(lbl_result)
        line.add_widget(self.in_result)
        self.btn = Button(text='Next', size_hint=(0.3, 0.2), pos_hint={'center_x':0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p1
        p1 = int(self.in_result.text)
        self.manager.current = 'sits'

class CheckSits(Screen):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_sits)
        self.btn = Button(text='Next', size_hint=(0.3, 0.2), pos_hint={'center_x':0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        self.manager.current = 'pulse2'

class PulseScr2(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        instr = Label(text=txt_test3)
        line1 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result1 = Label(text='Result', halign='right')
        self.in_result1 = TextInput(text='0', multiline=False)
        line1.add_widget(lbl_result1)
        line1.add_widget(self.in_result1)
        line2 = BoxLayout(size_hint=(0.8, None), height='30sp')
        lbl_result2 = Label(text='Result after test', halign='right')
        self.in_result2 = TextInput(text='0', multiline=False)
        line2.add_widget(lbl_result2)
        line2.add_widget(self.in_result2)
        self.btn = Button(text='Finalise',size_hint=(0.3, 0.2), pos_hint={'center_x':0.5})
        self.btn.on_press = self.next
        outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        outer.add_widget(instr)
        outer.add_widget(line1)
        outer.add_widget(line2)
        outer.add_widget(self.btn)
        self.add_widget(outer)
    def next(self):
        global p2, p3
        p2 = int(self.in_result1.text)
        p3 = int(self.in_result2.text)
        self.manager.current = 'result'
    
class Result(Screen):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        self.outer = BoxLayout(orientation='vertical', padding=8, spacing=8)
        self.instr = Label(text = '')
        self.outer.add_widget(self.instr)
        self.add_widget(self.outer)
        self.on_enter = self.before
    def before(self):
        global name
        self.instr.text = name + '\n' + test(p1, p2, p3, age)

class HeartCheck(App):
    def build(self):
        sm = ScreenManager()
        sm.add_widget(InstrScr(name='instr'))
        sm.add_widget(PulseScr(name='pulse1'))
        sm.add_widget(CheckSits(name='sits'))
        sm.add_widget(PulseScr2(name='pulse2'))
        sm.add_widget(Result(name='result'))
        return sm

app = HeartCheck()
app.run()
