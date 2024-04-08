from display_driver_utils import driver
import lvgl as lv
import random
# NOTE typing not available in micropython and making it work is difficult
# from typing import List, Tuple, Self
import time
from ui import UI
from widget import *
from global_definitions import widget_types, ascii_letters

class SpatialMap:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.occupied = []

    def is_space_available(self, x, y, w, h):
        # Check if within container boundaries
        if x + w > self.width or y + h > self.height:
            return False

        # Check for overlap with other widgets
        for oc in self.occupied:
            if not (x + w <= oc['x'] or x >= oc['x'] + oc['width'] or y + h <= oc['y'] or y >= oc['y'] + oc['height']):
                return False

        return True

    def occupy_space(self, x, y, w, h):
        self.occupied.append({'x': x, 'y': y, 'width': w, 'height': h})

def place_widget(container, widget, spatial_map):
    for _ in range(100):  # Try 100 times to find a spot
        x = random.randint(0, container.width - widget.get_width())
        y = random.randint(0, container.height - widget.get_height())
        if spatial_map.is_space_available(x, y, widget.get_width(), widget.get_height()):
            widget.set_pos(x, y)
            spatial_map.occupy_space(x, y, widget.get_width(), widget.get_height())
            return True
    return False  # Could not place the widget

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

    def create_random_layout_flex(self):
        ...

    def create_random_layout_grid(self):
        ...
    
    def create_random_layout_none(self):
        spatial_map = SpatialMap(self.width, self.height)
        print(f'{self.widget_count}: {type(self.widget_count)}')
        for i in range(self.widget_count):
            widget_type = random.choice(self.widget_types)
            widget_info, widget = self.create_random_widget(widget_type)
            lv.screen_load(self.container)
            self.container.update_layout()
            print(f'Placing {widget_type} with width: {widget.get_width()}, height: {widget.get_height()}')
            if not self.place_widget(widget, spatial_map):
                print(f'Could not place the widget: {widget_info}')
                widget.delete()
                continue
            self.randomize_style(widget)
            lv.screen_load(self.container)
            self.container.update_layout()
            tmp_coords = lv.area_t()
            widget.get_coords(tmp_coords)
            widget_info["x"] = (tmp_coords.x1 + tmp_coords.x2) // 2
            widget_info["y"] = (tmp_coords.y1 + tmp_coords.y2) // 2
            widget_info['width'] = widget.get_width()
            widget_info['height'] = widget.get_height()
            self.widgets['objects'].append(widget_info)
            self.objects.append(widget)
            print(f'[{i}]: {widget_info}')
        self.widgets['count'] = len(self.widgets['objects'])
        print(self.widgets)

    def place_widget(self, widget, spatial_map: SpatialMap):
        max_attempts = 100  # Max attempts to find a suitable spot
        for _ in range(max_attempts):
            x = random.randint(0, self.width - widget.get_width())
            y = random.randint(0, self.height - widget.get_height())
            if spatial_map.is_space_available(x, y, widget.get_width(), widget.get_height()):
                widget.set_pos(x, y)
                spatial_map.occupy_space(x, y, widget.get_width(), widget.get_height())
                return True
        return False  # Could not place the widget

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
    
    def randomize_style(self, widget: lv.obj):
        # Create style object
        style = lv.style_t()
        # Choose a random amount of style properties to set
        # Randomize the chosen style properties, creating property values according to the property type
        # Apply the style to the widget
        # List of style properties to randomize
        properties = [
            ('set_bg_color', lv.color_make),
            ('set_border_color', lv.color_make),
            ('set_border_width', lambda: random.randint(0, 10)),
            ('set_radius', lambda: random.randint(0, 50)),
            ('set_shadow_width', lambda: random.randint(0, 15)),
            ('set_shadow_color', lv.color_make),
            ('set_text_color', lv.color_make),
            ('set_line_color', lv.color_make),
            ('set_line_width', lambda: random.randint(0, 10)),
            # Add more properties as needed
        ]

        # Choose a random amount of style properties to set
        num_props_to_set = random.randint(3, len(properties))

        # Randomly select and set properties
        for _ in range(num_props_to_set):
            prop, value_generator = random.choice(properties)
            if 'color' in prop:
                # Generate a random color
                value = lv.color_hex(random.randint(0, 0xFFFFFF))
            else:
                # Generate a random value
                value = value_generator()
            getattr(style, prop)(value)

        # Apply the style to the widget
        widget.add_style(style, lv.PART.MAIN)
    
    def get_root_widget(self):
        return self.container
    
    def get_ui(self) -> UI:
        ui = UI()
        ui['count'] = self.widgets['count']
        ui['objects'] = self.widgets['objects']
        return ui
    
    def cleanup(self):
        for obj in self.objects:
            if obj is lv.obj:
                obj.delete()