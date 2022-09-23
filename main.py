
#Calculator_Of_The_Future



from kivy.app import App
from kivy.uix.button import Button
from kivy.config import Config
from kivy.uix.gridlayout import GridLayout
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label




#Config.set('graphics','resizable','0')
Config.set('graphics','width','350')
Config.set('graphics','height','600')

class MyApp(App):

    formul = '0'


    def lable_update(self):
        self.lbl.text = self.formul

    def add_number(self, instance):

        if self.formul == '0':

            self.formul = ''
        if instance.text.lower() == "x":
            self.formul += "*"
        else:
            self.formul += instance.text
        self.lable_update()

        print(self.formul)


    def resalt(self, instance):
        if eval(self.formul) - int(eval(self.formul)) == 0:
            self.formul = str(int(eval(self.formul)))
        else:
            self.formul = str(eval(self.formul))
        self.lable_update()



    def clear(self, instance):
        self.formul = "0"
        self.lable_update()

    def delit(self, instance):
        if len(self.formul) <= 0:
            return
        l = []
        for i in self.formul:
            l.append(i)

        l.pop(-1)

        self.formul = ''
        for i in l:
            self.formul += i

        if len(self.formul) < 1:
            self.formul = "0"
        self.lable_update()



    def build(self):


        bl = BoxLayout(orientation = "vertical", padding = 20)


        gl = GridLayout(cols = 4, rows = 5, spacing = 4, size_hint = (1, .6))

        gl.add_widget(Button(text = "7", on_press = self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text = "8", on_press = self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text = "9", on_press = self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text = "X", on_press = self.add_number, font_size = 30, background_color = [1, 1, 0, 1]))

        gl.add_widget(Button(text="4", on_press=self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text="5", on_press=self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text="6", on_press=self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text="-", on_press=self.add_number, font_size = 30, background_color = [1, 1, 0, 1]))

        gl.add_widget(Button(text="1", on_press=self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text="2", on_press=self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text="3", on_press=self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text="+", on_press=self.add_number, font_size = 30, background_color = [1, 1, 0, 1]))

        gl.add_widget(Button(text=".", on_press=self.add_number, font_size = 30, background_color = [1, 1, 0, 1]))
        gl.add_widget(Button(text="0", on_press=self.add_number, font_size = 30, background_color = [1, 0, 1, 1]))
        gl.add_widget(Button(text="/", on_press=self.add_number, font_size = 30, background_color = [1, 1, 0, 1]))
        gl.add_widget(Button(text="=", on_press=self.resalt, font_size = 30, background_color = [0, 1, 0, 1]))



        self.lbl = Label(text = self.formul, font_size = 30, size_hint = (1, .25), text_size = (350 - 40, 600* .25 - 40), halign = "right")

        blv = BoxLayout(orientation="horizontal", padding=20, spacing=4, size_hint=(1, .15))
        blv.add_widget(Button(text="C", on_press=self.clear, font_size=30, background_color = [200,0,0,1]))
        blv.add_widget(Button(text="D", on_press=self.delit, font_size=30, background_color = [1,0,0,1]))


        bl.add_widget(self.lbl)
        bl.add_widget(gl)
        bl.add_widget(blv)

        return bl


if __name__ == "__main__":
    MyApp().run()






