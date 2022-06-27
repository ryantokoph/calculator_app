from kivy.app import App
from kivy.uix.widget import Widget
from kivy.core.window import Window
from kivy.lang.builder import Builder
import re

Builder.load_file('calc.kv')
Window.size = (350, 500)


class CalculatorWidget(Widget):
    def clear(self):
        self.ids.input.text = '0'

    def btn_value(self, num):
        current_num = self.ids.input.text

        if "Not a number" in current_num:
            current_num = ''

        elif current_num == '0':
            self.ids.input.text = ''
            self.ids.input.text = f'{num}'
        else:
            self.ids.input.text = f'{current_num}{num}'

    def sign_value(self, sign):
        current_num = self.ids.input.text

        if "Not a number" in current_num:
            current_num = "Not a number"

        self.ids.input.text = f'{current_num}{sign}'

    def backspace(self):
        current_num = self.ids.input.text
        current_num = current_num[:-1]
        self.ids.input.text = current_num

    def equals(self):
        current_value = self.ids.input.text
        try:
            result = eval(current_value)
            self.ids.input.text = str(result)
        except:
            self.ids.input.text = "Not a number"

    def pos_neg(self):
        current_num = self.ids.input.text

        if '-' in current_num:
            self.ids.input.text = f"{current_num.replace('-', '')}"
        else:
            self.ids.input.text = f'-{current_num}'

    def dot(self):
        current_num = self.ids.input.text
        num_list = re.split("\+|\*|-|/|%|/", current_num)

        if ('+' in current_num or '*' in current_num or '-' in current_num or '%' in current_num or '/') and '.' not in num_list[-1]:
            current_num = f'{current_num}.'
            self.ids.input.text = current_num

        elif '.' in current_num:
            pass
        else:
            current_num = f'{current_num}.'
            self.ids.input.text = current_num


class CalculatorApp(App):
    def build(self):
        return CalculatorWidget()


if __name__ == "__main__":
    CalculatorApp().run()
