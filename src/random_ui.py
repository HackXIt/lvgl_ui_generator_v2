import sys
if sys.implementation.name == "micropython":
    from display_driver_utils import driver
    import lvgl as lv
    import random
    # NOTE typing not available in micropython and making it work is difficult
    # from typing import List, Tuple, Self
    import time
    from ui import UI
    from widget import *
    from global_definitions import widget_types, ascii_letters
else:
    import mock
    from .mock.display import driver
    from .mock.lvgl import lv
    from .ui import UI
    from .widget import *
    from .global_definitions import widget_types, ascii_letters
    import random
    # from typing import List, Tuple, Self
    import time

class SpatialMap:
    """
    A simple spatial map to keep track of occupied areas in a container.

    **Object Attributes:**
    - `width` The width of the container.
    - `height` The height of the container.
    - `occupied` A list of dictionaries representing occupied areas in the container.
    """
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.occupied = []

    def is_space_available(self, x, y, w, h):
        """
        **Params:**
        - `x` The x-coordinate of the space.
        - `y` The y-coordinate of the space.
        - `w` The width of the space.
        - `h` The height of the space.

        **Returns:**
        - `bool` True if the space is available, False otherwise.

        Check if the given space is available for a widget.
        """
        # Check if within container boundaries
        if x + w > self.width or y + h > self.height:
            return False

        # Check for overlap with other widgets
        for oc in self.occupied:
            if not (x + w <= oc['x'] or x >= oc['x'] + oc['width'] or y + h <= oc['y'] or y >= oc['y'] + oc['height']):
                return False

        return True

    def occupy_space(self, x, y, w, h):
        """
        **Params:**
        - `x` The x-coordinate of the space.
        - `y` The y-coordinate of the space.
        - `w` The width of the space.
        - `h` The height of the space.

        Mark the given space as occupied, by adding it to the list of occupied areas.
        """
        self.occupied.append({'x': x, 'y': y, 'width': w, 'height': h})

def place_widget(container: lv.obj, widget: lv.obj, spatial_map: SpatialMap):
    """
    **Params:**
    - `container` The container to place the widget in.
    - `widget` The widget to place.
    - `spatial_map` The spatial map to check for available space.

    **Returns:**
    - `bool` True if the widget was placed successfully, False otherwise.

    Place a widget in a container, avoiding overlap with other widgets.
    Placement occurs virtually be checking if the widget fits in the container using a spatial map.
    The placing is done randomly within the container space and by checking the spatial map to avoid overlap with other widgets.
    Placement is attempted 100 times before giving up.
    """
    for _ in range(100):  # Try 100 times to find a spot
        x = random.randint(0, container.width - widget.get_width())
        y = random.randint(0, container.height - widget.get_height())
        if spatial_map.is_space_available(x, y, widget.get_width(), widget.get_height()):
            widget.set_pos(x, y)
            spatial_map.occupy_space(x, y, widget.get_width(), widget.get_height())
            return True
    return False  # Could not place the widget

class RandomUI:
    """
    A class to generate a random UI window with a specified width, height, widget count, widget types, output file, layout, and random state.

    **Class Attributes:**
    - `layout_options` A list of valid layout options.

    **Object Attributes:**
    - `width` The width of the UI window.
    - `height` The height of the UI window.
    - `widget_count` The number of widgets to generate.
    - `widget_types` A list of widget types to choose from.
    - `output_file` The output file name.
    - `layout` The layout type to use.
    - `random_state` A boolean flag to randomize widget state.
    """
    layout_options = ['flex', 'grid', 'none']
    def __init__(self, width: int, height: int, widget_count: int, widget_types: list[str], output_file: str, layout: str, random_state: bool = False):
        # Store the input parameters
        self.width = int(width)
        self.height = int(height)
        self.widget_count = int(widget_count)
        self.widget_types = widget_types
        self.output_file = output_file
        self.layout = layout
        self.random_state = random_state
        # Initialize random UI
        # self.display_driver = display_driver.DisplayDriver()
        # self.display_driver.init()
        self.objects = []
        self.widgets = {'count': 0, 'objects': []}
        self.type_count = {}
        random.seed(int(time.time() * 1000000))
        driver(width=self.width, height=self.height)
    
    def create_random_ui(self):
        """
        **Returns**:
        - `Self`

        **Raises**:
        - `ValueError` If the layout is not a valid option.

        Create a random UI window with the specified width and height.
        """
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
        """
        Create a container layout using the flex layout.
        """
        self.container.set_layout(lv.LAYOUT.FLEX)
        self.container.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
        print(f'{self.widget_count}: {type(self.widget_count)}')
        for i in range(self.widget_count):
            widget_type = random.choice(self.widget_types)
            widget_info, widget = self.create_random_widget(widget_type)
            lv.screen_load(self.container)
            self.container.update_layout()
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

    def create_random_layout_grid(self):
        """Create a container layout using the grid layout. **(Not implemented)**"""
        ...
    
    def create_random_layout_none(self):
        """
        Create a container layout with absolute positioning.
        Widgets are placed randomly within the container, attempting to avoid overlap.
        Spacing between widgets is not guaranteed.
        Style properties are randomized for each widget.
        Widget metadata of the UI is stored in the `widgets` dictionary.
        """
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
        """
        **Params:**
        - `widget` The widget to place.
        - `spatial_map` The spatial map to check for available space.

        **Returns:**
        - `bool` True if the widget was placed successfully, False otherwise.

        Place a widget in a container, avoiding overlap with other widgets.
        Placement occurs virtually be checking if the widget fits in the container using a spatial map.
        The placing is done randomly within the container space and by checking the spatial map to avoid overlap with other widgets.
        Placement is attempted 100 times before giving up.
        """
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
        """
        **Params:**
        - `widget_type` The type of widget to create.

        **Returns:**
        - `Tuple[dict, lv.obj]` A tuple containing the widget metadata and object.

        Create a random widget of the specified type and return the widget metadata and object.
        If `random_state` is enabled, the widget state is randomized.
        """
        if widget_type not in widget_types:
            raise ValueError(f'Invalid widget type: {widget_type} (valid options: {",".join(widget_types)})')
        widget = widget_mapping[widget_type]({})
        if self.random_state:
            randomize_state(widget)
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
        """
        **Params:**
        - `widget` The widget to randomize the style of.

        Randomize the style properties of a widget by creating a style object and setting randomly chosen properties with random values.
        """
        # Create style object
        style = lv.style_t()
        # Choose a random amount of style properties to set
        # Randomize the chosen style properties, creating property values according to the property type
        # Apply the style to the widget
        # List of style properties to randomize
        properties = [
            ('set_bg_color', lv.color_make),
            ('set_bg_opa', lambda: random.randint(0, 100)),
            ('set_border_color', lv.color_make),
            ('set_border_opa', lambda: random.randint(0, 100)),
            ('set_border_width', lambda: random.randint(0, 10)),
            ('set_outline_width', lambda: random.randint(0, 10)),
            ('set_outline_color', lv.color_make),
            ('set_outline_opa', lambda: random.randint(0, 100)),
            ('set_shadow_width', lambda: random.randint(0, 15)),
            ('set_shadow_offset_x', lambda: random.randint(0, 10)),
            ('set_shadow_offset_y', lambda: random.randint(0, 10)),
            ('set_shadow_color', lv.color_make),
            ('set_shadow_opa', lambda: random.randint(0, 100)),
            ('set_line_width', lambda: random.randint(0, 10)),
            ('set_line_dash_width', lambda: random.randint(0, 10)),
            ('set_line_dash_gap', lambda: random.randint(0, 10)),
            ('set_line_rounded', lambda: random.choice([True, False])),
            ('set_line_color', lv.color_make),
            ('set_line_opa', lambda: random.randint(0, 100)),
            ('set_text_color', lv.color_make),
            ('set_text_opa', lambda: random.randint(0, 100)),
            ('set_text_letter_space', lambda: random.randint(0, 10)),
            ('set_text_line_space', lambda: random.randint(0, 10)),
            ('set_opa', lambda: random.randint(0, 100)),
            ('set_align', lambda: random.choice([lv.ALIGN.CENTER, lv.ALIGN.TOP_LEFT, lv.ALIGN.TOP_RIGHT, lv.ALIGN.TOP_MID, lv.ALIGN.BOTTOM_LEFT, lv.ALIGN.BOTTOM_RIGHT, lv.ALIGN.BOTTOM_MID, lv.ALIGN.LEFT_MID, lv.ALIGN.RIGHT_MID, lv.ALIGN.DEFAULT])),
            ('set_pad_all', lambda: random.randint(0, 10)),
            ('set_pad_hor', lambda: random.randint(0, 10)),
            ('set_pad_ver', lambda: random.randint(0, 10)),
            ('set_pad_gap', lambda: random.randint(0, 10)),
            ('set_pad_top', lambda: random.randint(0, 10)),
            ('set_pad_bottom', lambda: random.randint(0, 10)),
            ('set_pad_left', lambda: random.randint(0, 10)),
            ('set_pad_right', lambda: random.randint(0, 10)),
            ('set_pad_row', lambda: random.randint(0, 10)),
            ('set_pad_column', lambda: random.randint(0, 10)),
            ('set_margin_top', lambda: random.randint(0, 10)),
            ('set_margin_bottom', lambda: random.randint(0, 10)),
            ('set_margin_left', lambda: random.randint(0, 10)),
            ('set_margin_right', lambda: random.randint(0, 10))
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
        """Return the root widget (container) of the UI."""
        return self.container
    
    def get_ui(self) -> UI:
        """
        **Returns:**
        - `UI` The UI object containing the metadata.

        Return a UI object (special dictionary) containing the screen dimensions and all widget position metadata required for bounding box annotation.
        """
        ui = UI()
        ui['count'] = self.widgets['count']
        ui['objects'] = self.widgets['objects']
        return ui
    
    def cleanup(self):
        """
        Cleanup the screen and widgets, destroying all created objects.
        Note that this function will cause a known error when sub-widgets are indirectly deleted by destroying their parent container.
        That error is safe to ignore, as the widgets should be properly deleted by LVGL.
        """
        for obj in self.objects:
            if obj is lv.obj:
                obj.delete()