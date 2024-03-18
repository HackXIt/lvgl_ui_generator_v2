from display_driver_utils import driver
import lvgl as lv
import random
# NOTE typing not available in micropython and making it work is difficult
# from typing import List, Tuple, Self
import time

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class RandomUI:
    layout_options = ['flex', 'grid', 'none']
    def __init__(self, width: int, height: int, widget_count: int, widget_types: list[str], output_file: str, layout: str):
        # Store the input parameters
        self.width = int(width)
        self.height = int(height)
        self.widget_count = int(widget_count)
        self.widget_types = widget_types
        self.output_file = output_file
        self.layout = layout
        # Initialize random UI
        # self.display_driver = display_driver.DisplayDriver()
        # self.display_driver.init()
        self.objects = []
        self.widgets = {'count': 0, 'objects': []}
        random.seed(int(time.time() * 1000000))
        driver(width=self.width, height=self.height)

    def create_random_layout_flex(self):
        ...

    def create_random_layout_grid(self):
        ...

    def create_random_widget(self, widget_type: str) -> tuple[dict, lv.obj]:
        if widget_type == 'button':
            widget = lv.button(self.container)
            label = lv.label(widget)
            label.set_parent(widget)
            label.set_text('Button')
        elif widget_type == 'label':
            widget = lv.label(self.container)
            widget.set_text('Label')
        elif widget_type == 'image':
            widget = lv.img(self.container)
            widget.set_src(lv.SYMBOL.OK)
        elif widget_type == 'line':
            widget = lv.line(self.container)
            widget.set_points([(0, 0), (self.width, self.height)])
        elif widget_type == 'bar':
            widget = lv.bar(self.container)
            widget.set_value(50, lv.ANIM.ON)
        elif widget_type == 'slider':
            widget = lv.slider(self.container)
            widget.set_range(0, 100)
            widget.set_value(50, lv.ANIM.ON)
        elif widget_type == 'switch':
            widget = lv.switch(self.container)
        elif widget_type == 'checkbox':
            widget = lv.checkbox(self.container)
            widget.set_text('Checkbox')
        elif widget_type == 'roller':
            widget = lv.roller(self.container)
            for i in range(random.randint(1, 10)):
                options = '\n'.join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
            widget.set_options(options)
        elif widget_type == 'dropdown':
            widget = lv.dropdown(self.container)
            for i in range(random.randint(1, 10)):
                options = '\n'.join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
            widget.set_options(options)
        elif widget_type == 'textarea':
            widget = lv.textarea(self.container)
            widget.set_text('Textarea')
        elif widget_type == 'chart':
            widget = lv.chart(self.container)
            ser1 = widget.add_series(lv.color_hex(0x2587FF))
            ser2 = widget.add_series(lv.color_hex(0xFF0000))
            widget.set_type(ser1, lv.chart.TYPE.LINE | lv.chart.TYPE.LINE)
            widget.set_type(ser2, lv.chart.TYPE.LINE | lv.chart.TYPE.LINE)
            widget.set_point_count(ser1, 10)
            widget.set_point_count(ser2, 10)
            widget.set_ext_y_array(ser1, [lv.OPA.COVER, lv.OPA.COVER, lv.OPA.COVER, lv.OPA.COVER])
        widget.set_parent(self.container)
        type_count = [widget['object'] for widget in self.widgets['objects'] if widget['type'] == widget_type]
        self.objects.append(widget)
        widget_info = {
            'type': widget_type,
            'class': widget.__class__.__name__,
            'index': len(type_count)
        }
        return widget_info, widget # type: ignore

    def create_random_ui(self):
        if self.layout not in self.layout_options:
            raise ValueError(f'Invalid layout: {self.layout} (valid options: {",".join(self.layout_options)})')
        # Create a screen
        self.container = lv.obj()
        self.container.set_size(self.width, self.height)
        # lv.scr_load(scr)

        # Create a container
        # self.container = lv.obj()
        # self.container.set_parent(self.scr)
        # self.container.set_size(self.width, self.height)
        # self.container.align(lv.ALIGN.CENTER, 0, 0)

        # Create a layout
        if self.layout == 'flex':
            self.create_random_layout_flex()
        elif self.layout == 'grid':
            self.create_random_layout_grid()
        elif self.layout == 'none':
            print(f'{self.widget_count}: {type(self.widget_count)}')
            for i in range(self.widget_count):
                widget_type = random.choice(self.widget_types)
                widget_info, widget = self.create_random_widget(widget_type)
                print(f'width: {widget.get_width()}, height: {widget.get_height()}')
                max_x = self.width - widget.get_width()
                max_y = self.height - widget.get_height()
                print(f'max_x: {max_x}, max_y: {max_y}')
                x = random.randint(0, max_x)
                y = random.randint(0, max_y)
                print(f'x: {x}, y: {y}')
                widget.set_pos(x, y)
                lv.screen_load(self.container)
                self.container.update_layout()
                # self.container.update_layout()
                widget_info['x'] = widget.get_x()
                widget_info['y'] = widget.get_y()
                widget_info['width'] = widget.get_width()
                widget_info['height'] = widget.get_height()
                self.widgets['objects'].append(widget_info)
                self.objects.append(widget)
                print(f'[{i}]: {widget_info}')
            self.widgets['count'] = len(self.widgets['objects'])
            print(self.widgets)
        return self
