from kivy.app import App
from kivy.uix.widget import Widget
from kivy.uix.button import Button
from kivy.graphics import (Color, Ellipse, Rectangle, Line)
from kivy.core.window import Window


class PainterWidget(Widget):
    def __init__(self, **kwargs):
        super(PainterWidget, self).__init__(**kwargs)

    def on_touch_down(self, touch):
        with self.canvas:
            Color(rgba=self.color)
            Ellipse(pos=(touch.x - 30/2, touch.y - 30/2), size=(30, 30))
            self.line = Line(pos=(touch.x, touch.y), width=15)


    def on_touch_move(self, touch):
        self.line.points += (touch.x, touch.y)


    def red(self, instance):
        self.color = (1, 0, 0, 1)

    def green(self, instance):
        self.color = (0, 1, 0, 1)

    def dark_blue(self, instance):
        self.color = (0, 0, 1, 1)

    def yellow(self, instance):
        self.color = (1, 1, 0, 1)

    def bereza(self, instance):
        self.color = (0, 1, 1, 1)

    def white(self, instance):
        self.color = (1, 1, 1, 1)


class PaintApp(App):
    def build(self):
        parent = Widget()
        self.painter = PainterWidget()
        parent.add_widget(self.painter)
        parent.add_widget(Button(size=(149, 75), pos=(1, 610), font_size=65, color=[1, 0, 0],
                                 on_press = self.painter.red, background_color=[255, 0, 0]))
        parent.add_widget(Button(size=(149, 75), pos=(152, 610), font_size=65, color=[0, 1, 0, 1],
                                 on_press=self.painter.green, background_color=[0, 255, 0]))
        parent.add_widget(Button(size=(149, 75), pos=(303, 610), font_size=65, color=[0, 1, 0, 1],
                                 on_press=self.painter.dark_blue, background_color=[0, 0, 255]))
        parent.add_widget(Button(size=(149, 75), pos=(454, 610), font_size=65, color=[1, 1, 0, 1],
                                 on_press=self.painter.yellow, background_color=[255, 255, 0]))
        parent.add_widget(Button(size=(149, 75), pos=(605, 610), font_size=65, color=[0, 1, 1, 1],
                                 on_press=self.painter.bereza, background_color=[0, 255, 255]))
        parent.add_widget(Button(size=(149, 75), pos=(756, 610), font_size=65, color=[1, 1, 1],
                                 on_press=self.painter.white, background_color=[255, 255, 255]))
        parent.add_widget((Button(text='Clear', on_press=self.clear_canvas)))

        return parent

    def clear_canvas(self, instance):
        self.painter.canvas.clear()

if __name__ == '__main__':
    PaintApp().run()
