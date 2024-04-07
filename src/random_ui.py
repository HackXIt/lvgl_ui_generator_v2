from display_driver_utils import driver
import lvgl as lv
import random
# NOTE typing not available in micropython and making it work is difficult
# from typing import List, Tuple, Self
import time
from ui import UI
from widget import *
from global_definitions import widget_types, ascii_letters

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
        self.type_count = {}
        random.seed(int(time.time() * 1000000))
        driver(width=self.width, height=self.height)

    def create_random_layout_flex(self):
        ...

    def create_random_layout_grid(self):
        ...
    
    def create_random_layout_none(self):
        print(f'{self.widget_count}: {type(self.widget_count)}')
        for i in range(self.widget_count):
            widget_type = random.choice(self.widget_types)
            widget_info, widget = self.create_random_widget(widget_type)
            lv.screen_load(self.container)
            self.container.update_layout()
            print(f'width: {widget.get_width()}, height: {widget.get_height()}')
            max_x = self.width - widget.get_width()
            max_y = self.height - widget.get_height()
            if max_x < 0:
                max_x = 0
            if max_y < 0:
                max_y = 0
            print(f'max_x: {max_x}, max_y: {max_y}')
            x = random.randint(0, max_x)
            y = random.randint(0, max_y)
            print(f'x: {x}, y: {y}')
            widget.set_pos(x, y)
            lv.screen_load(self.container)
            self.container.update_layout()
            # self.container.update_layout()
            # NOTE Coordinates would not be accurate if another container would be nested inside the main container
            widget_info['x'] = widget.get_x()
            widget_info['y'] = widget.get_y()
            widget_info['width'] = widget.get_width()
            widget_info['height'] = widget.get_height()
            self.widgets['objects'].append(widget_info)
            self.objects.append(widget)
            print(f'[{i}]: {widget_info}')
        self.widgets['count'] = len(self.widgets['objects'])
        print(self.widgets)

    def create_random_widget(self, widget_type: str) -> tuple[dict, lv.obj]:
        if widget_type not in widget_types:
            raise ValueError(f'Invalid widget type: {widget_type} (valid options: {",".join(widget_types)})')
        widget = widget_mapping[widget_type]({})
        widget.set_parent(self.container)
        self.type_count[widget_type] = self.type_count.get(widget_type, 0) + 1
        self.objects.append(widget)
        widget_info = {
            'type': widget_type,
            'class': widget.__class__.__name__,
            'index': self.type_count[widget_type]
        }
        return widget_info, widget # type: ignore

    def create_random_ui(self):
        if self.layout not in self.layout_options:
            raise ValueError(f'Invalid layout: {self.layout} (valid options: {",".join(self.layout_options)})')
        # Create a screen
        self.container = lv.obj(lv.screen_active())
        self.container.set_size(self.width, self.height)

        # Create a layout
        if self.layout == 'flex':
            self.create_random_layout_flex()
        elif self.layout == 'grid':
            self.create_random_layout_grid()
        elif self.layout == 'none':
            self.create_random_layout_none()
        return self
    
    def get_root_widget(self):
        return self.container
    
    def get_ui(self) -> UI:
        ui = UI()
        ui['count'] = self.widgets['count']
        ui['objects'] = self.widgets['objects']
        return ui