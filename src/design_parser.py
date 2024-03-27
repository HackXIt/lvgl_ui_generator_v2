from display_driver_utils import driver
import lvgl as lv
import json
import random

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class UiLoader:
    special_types = ["container", "random"]
    widget_types = ["arc", "bar", "button", "buttonmatrix", "calendar", "chart", "checkbox", "dropdown", "image", "imagebutton", "keyboard", "label", "led", "line", "list", "menu", "messagebox", "roller", "scale", "slider", "spangroup", "spinbox", "spinner", "switch", "table", "tabview", "textarea", "tileview", "window"]
    valid_types = special_types + widget_types
    def __init__(self, json_file):
        # Load JSON data from file
        with open(json_file, "r") as file:
            json_data = file.read()
        # Load JSON data
        self.data = json.loads(json_data)
        self.ui = self.data["ui"]
        # Create a dictionary to store references to created widgets
        self.widgets = {}
        self.styles = {}
    
    def initialize_screen(self):
        # Create the screen
        self.width = self.ui["window"]["width"]
        self.height = self.ui["window"]["height"]
        self.title = self.ui["window"]["title"]
        self.screen = driver(width=self.width, height=self.height)

    def parse_ui(self):
        # Parse the root element
        self.root_widget = self.parse_element(self.ui["root"])
        self.root_widget.set_parent(lv.screen_active())
        # NOTE The below can be accomplished by setting the width and height of the root widget via style properties
        # self.root_widget.set_width(self.width)
        # self.root_widget.set_height(self.height)

    def parse_element(self, element):
        # Create a widget based on the element type
        widget = self.create_widget(element)
        # Process child elements if they exist
        if "children" in element:
            for child in element["children"]:
                child_widget = self.parse_element(child)
                child_widget.set_parent(widget)
        if "style" in element:
            self.apply_style(widget, element["style"])
        return widget

    def create_widget(self, element) -> lv.obj | lv.button | lv.label | lv.image | lv.line | lv.bar | lv.slider | lv.switch | lv.checkbox | lv.roller | lv.dropdown | lv.textarea | lv.chart:
        widget = None
        widget_type = element["type"]
        if widget_type not in self.valid_types:
            raise ValueError(f"Invalid widget type: {widget_type}, valid types are: {self.valid_types}")
        if widget_type == 'container':
            widget = self.create_container(element)
        elif widget_type == 'arc':
            widget = self.create_arc(element)
        elif widget_type == 'bar':
            widget = self.create_bar(element)
        elif widget_type == 'button':
            widget = self.create_button(element)
        elif widget_type == 'buttonmatrix':
            widget = self.create_buttonmatrix(element)
        elif widget_type == 'calendar':
            widget = self.create_calendar(element)
        elif widget_type == 'chart':
            widget = self.create_chart(element)
        elif widget_type == 'checkbox':
            widget = self.create_checkbox(element)
        elif widget_type == 'dropdown':
            widget = self.create_dropdown(element)
        elif widget_type == 'image':
            widget = self.create_image(element)
        elif widget_type == 'imagebutton':
            widget = self.create_imagebutton(element)
        elif widget_type == 'keyboard':
            widget = self.create_keyboard(element)
        elif widget_type == 'label':
            widget = self.create_label(element)
        elif widget_type == 'led':
            widget = self.create_led(element)
        elif widget_type == 'line':
            widget = self.create_line(element)
        elif widget_type == 'list':
            widget = self.create_list(element)
        elif widget_type == 'menu':
            widget = self.create_menu(element)
        elif widget_type == 'messagebox':
            widget = self.create_messagebox(element)
        elif widget_type == 'roller':
            widget = self.create_roller(element)
        elif widget_type == 'scale':
            widget = self.create_scale(element)
        elif widget_type == 'slider':
            widget = self.create_slider(element)
        elif widget_type == 'spangroup':
            widget = self.create_spangroup(element)
        elif widget_type == 'spinbox':
            widget = self.create_spinbox(element)
        elif widget_type == 'spinner':
            widget = self.create_spinner(element)
        elif widget_type == 'switch':
            widget = self.create_switch(element)
        elif widget_type == 'table':
            widget = self.create_table(element)
        elif widget_type == 'tabview':
            widget = self.create_tabview(element)
        elif widget_type == 'textarea':
            widget = self.create_textarea(element)
        elif widget_type == 'tileview':
            widget = self.create_tileview(element)
        elif widget_type == 'window':
            widget = self.create_window(element)
        elif widget_type == "random":
            widget = self.create_random_widget(element)
        if widget == None:
            raise ValueError(f"Failed to create widget: {element}")
        # Create a unique ID for the widget if it wasn't provided
        if "id" not in element:
            # Count types of the widget
            count = sum([1 for w in self.widgets.values() if type(w) == type(widget)])
            element["id"] = f"{widget_type}_{count}"
        if element["id"] in self.widgets:
            raise ValueError(f"Widget with ID '{element['id']}' already exists. IDs must be unique.")
        self.widgets[element["id"]] = widget
        print(f"Created widget '{element['id']}': {element}")
        return widget

# NOTE ------------ SPECIAL CREATION METHODS ------------

    def create_container(self, element) -> lv.obj:
        if "options" not in element:
            raise ValueError(f"Container widget must have options: {element}")
        container = lv.obj(lv.screen_active())
        options = element["options"]
        if "layout" not in options:
            raise ValueError(f"Container widget must have layout: {options}. Valid options are: ['none', 'grid', 'flex']")
        layout = options["layout"]
        if layout == "none":
            container.set_layout(lv.LAYOUT.NONE)
        elif layout == "grid":
            self.configure_grid_layout(container, options)
        elif layout == "flex":
            self.configure_flex_layout(container, options)
        return container
    
    def configure_flex_layout(self, container, options):
        container.set_layout(lv.LAYOUT.FLEX)
        if "flow" in options:
            flow = options["flow"]
            if flow == "row":
                container.set_flex_flow(lv.FLEX_FLOW.ROW)
            elif flow == "column":
                container.set_flex_flow(lv.FLEX_FLOW.COLUMN)
            elif flow == "row_wrap":
                container.set_flex_flow(lv.FLEX_FLOW.ROW_WRAP)
            elif flow == "column_wrap":
                container.set_flex_flow(lv.FLEX_FLOW.COLUMN_WRAP)
            elif flow == "row_reverse":
                container.set_flex_flow(lv.FLEX_FLOW.ROW_REVERSE)
            elif flow == "column_reverse":
                container.set_flex_flow(lv.FLEX_FLOW.COLUMN_REVERSE)
        else:
            container.set_flex_flow(lv.FLEX_FLOW.ROW)

    def configure_grid_layout(self, container, options):
        container.set_layout(lv.LAYOUT.GRID)
        # TODO Need to properly handle grid placements of children with grid layout
        if "grid_dsc" in options:
            if "col_dsc" not in options["grid_dsc"] or "row_dsc" not in options["grid_dsc"]:
                raise ValueError(f"grid_dsc must have col_dsc and row_dsc: {options['grid_dsc']}")
            container.set_grid_dsc_array(options["grid_dsc"]["col_dsc"], options["grid_dsc"]["row_dsc"])
        else:
            container.set_grid_dsc_array([1, 1], [1, 1])
    
    def create_random_widget(self, element):
        # FIXME Placement of random widget is not handled properly (inside grid layout)
        if "parent_id" not in element:
            raise ValueError(f"Random widget must have parent_id: {element}")
        if "count" not in element:
            raise ValueError(f"Random widget must have count: {element}")
        if "count" in element:
            for i in range(element["count"]):
                element["type"] = random.choice(element["options"])
                widget = self.create_widget(element)
                widget.set_parent(self.widgets[element["parent_id"]])
                if "style" in element:
                    self.apply_style(widget, element["style"])
        return widget

# NOTE ------------ WIDGET CREATION METHODS ------------

    def create_arc(self, element) -> lv.arc:
        # TODO Implement arc widget
        widget = lv.arc(lv.screen_active())
        return widget
    
    def create_bar(self, element) -> lv.bar:
        widget = lv.bar(lv.screen_active())
        if "options" in element:
            range_min = element["options"].get("range_min", 0)
            range_max = element["options"].get("range_max", 100)
            value = element["options"].get("value", 0)
            widget.set_range(range_min, range_max)
            widget.set_value(value, lv.ANIM.ON)
        return widget
    
    def create_button(self, element) -> lv.button:
        # FIXME Label of button currently ignores style properties (uses defaults)
        widget = lv.button(lv.screen_active())
        label = lv.label(widget)
        label.set_parent(widget)
        if "text" not in element:
            text = "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
            element["text"] = text
        label.set_text(element["text"])
        return widget
    
    def create_buttonmatrix(self, element) -> lv.buttonmatrix:
        # TODO Implement buttonmatrix widget
        widget = lv.buttonmatrix(lv.screen_active())
        return widget
    
    def create_calendar(self, element) -> lv.calendar:
        # TODO Implement calendar widget
        widget = lv.calendar(lv.screen_active())
        return widget
    
    def create_chart(self, element) -> lv.chart:
        # TODO Implement chart widget (also tough to implement)
        widget = lv.chart(lv.screen_active())
        # if "options" in element:
        #     chart_type = getattr(lv.chart, element["options"].get("type", "TYPE.LINE"))
        #     point_count = element["options"].get("point_count", 10)
        #     series_options = element["options"].get("series", [])
        #     widget.set_type(chart_type)
        #     widget.set_point_count(point_count)
        #     for series_option in series_options:
        #         series = widget.add_series(lv.color_hex(self.convert_value("color", series_option["color"]))))
        #         points = series_option.get("points", [])
        #         widget.set_points(series, points)
        return widget
    
    def create_canvas(self, element) -> lv.canvas:
        # TODO Implement canvas widget
        widget = lv.canvas(lv.screen_active())
        return widget
    
    def create_checkbox(self, element) -> lv.checkbox:
        # TODO Implement checkbox widget
        widget = lv.checkbox(lv.screen_active())
        # widget.set_text('Checkbox')
        return widget
    
    def create_dropdown(self, element) -> lv.dropdown:
        widget = lv.dropdown(lv.screen_active())
        if "options" in element:
            options = element["options"].get("options", [])
            if len(options) == 0:
                for i in range(random.randint(1, 10)):
                    options.append("".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
            widget.set_options("\n".join(options))
        return widget

    def create_image(self, element) -> lv.image:
        # TODO Implement image widget
        widget = lv.image(lv.screen_active())
        # widget.set_src(lv.SYMBOL.OK)
        return widget
    
    def create_imagebutton(self, element) -> lv.imagebutton:
        # TODO Implement image_button widget
        widget = lv.imagebutton(lv.screen_active())
        return widget
    
    def create_keyboard(self, element) -> lv.keyboard:
        # TODO Implement keyboard widget
        widget = lv.keyboard(lv.screen_active())
        return widget

    def create_label(self, element) -> lv.label:
        widget = lv.label(lv.screen_active())
        if "text" not in element:
            text = "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
            element["text"] = text
        widget.set_text(element["text"])
        return widget
    
    def create_led(self, element) -> lv.led:
        # TODO Implement led widget
        widget = lv.led(lv.screen_active())
        return widget

    def create_line(self, element) -> lv.line:
        # TODO Implement line widget (also tough to implement)
        widget = lv.line(lv.screen_active())
        # if "options" in element:
        #     points = element["options"].get("points", [])
        #     widget.set_points(points)
        return widget
    
    def create_list(self, element) -> lv.list:
        # TODO Implement list widget
        widget = lv.list(lv.screen_active())
        return widget
    
    def create_menu(self, element) -> lv.menu:
        # TODO Implement menu widget
        widget = lv.menu(lv.screen_active())
        return widget
    
    def create_messagebox(self, element) -> lv.msgbox:
        # TODO Implement messagebox widget
        widget = lv.msgbox(lv.screen_active())
        return widget
    
    def create_roller(self, element) -> lv.roller:
        # TODO Implement roller widget
        widget = lv.roller(lv.screen_active())
        # for i in range(random.randint(1, 10)):
        #     options = '\n'.join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
        # widget.set_options(options)
        return widget
    
    def create_scale(self, element) -> lv.scale:
        # TODO Implement scale widget
        widget = lv.scale(lv.screen_active())
        return widget

    def create_slider(self, element) -> lv.slider:
        widget = lv.slider(lv.screen_active())
        if "options" in element:
            range_min = element["options"].get("range_min", 0)
            range_max = element["options"].get("range_max", 100)
            value = element["options"].get("value", 0)
            widget.set_range(range_min, range_max)
            widget.set_value(value, lv.ANIM.ON)
        return widget

    def create_spangroup(self, element) -> lv.spangroup:
        # TODO Implement span widget
        widget = lv.spangroup(lv.screen_active())
        return widget

    def create_spinbox(self, element) -> lv.spinbox:
        # TODO Implement spinbox widget
        widget = lv.spinbox(lv.screen_active())
        return widget

    def create_spinner(self, element) -> lv.spinner:
        # TODO Implement spinner widget
        widget = lv.spinner(lv.screen_active())
        return widget

    def create_switch(self, element) -> lv.switch:
        # TODO Implement switch widget
        widget = lv.switch(lv.screen_active())
        return widget
    
    def create_table(self, element) -> lv.table:
        # TODO Implement table widget
        widget = lv.table(lv.screen_active())
        return widget

    def create_tabview(self, element) -> lv.tabview:
        # TODO Implement tabview widget
        widget = lv.tabview(lv.screen_active())
        return widget

    def create_textarea(self, element) -> lv.textarea:
        # TODO Implement textarea widget
        widget = lv.textarea(lv.screen_active())
        # widget.set_text('Textarea')
        return widget
    
    def create_tileview(self, element) -> lv.tileview:
        # TODO Implement tileview widget
        widget = lv.tileview(lv.screen_active())
        return widget
    
    def create_window(self, element) -> lv.win:
        # TODO Implement window widget
        widget = lv.win(lv.screen_active())
        return widget

    
# NOTE ------------ STYLE CREATION METHODS ------------
    
    def create_style(self, style_def):
        print(f"Creating style: {style_def}")
        style = lv.style_t() # FIXME missing parameter 'args' of type '_style_t_type' (unresolved) - ignore?
        style.init()

        for prop, value in style_def.items():
            if prop == "selector":
                continue
            setter_name = f"set_{prop}"
            if hasattr(style, setter_name):
                setter = getattr(style, setter_name)
                converted_value = self.convert_value(prop, value)
                if(converted_value == None):
                    print(f"Unsupported value conversion: {value} for style property {prop}")
                    continue
                try:
                    setter(converted_value)
                except TypeError as e:
                    print(f"TypeError setting style property {prop}: {e}")
            else:
                print(f"Unsupported style property: {prop}")

        return style
    
    def convert_value(self, prop_name, value):
        # This function converts the value based on the property name
        if "color" in prop_name:
            converted_value = int(value.strip("#"), 16)
            print(f"Color property conversion: {prop_name}:{value} => {converted_value:x}")
            return lv.color_hex(converted_value)
        elif "font" in prop_name:
            print(f"Font property: {prop_name}:{value}")
            # TODO micropython doesn't support font ?
            return None
        elif "align" in prop_name:
            if value == "center":
                return lv.ALIGN.CENTER
            elif value == "top-left":
                return lv.ALIGN.TOP_LEFT
            elif value == "top-right":
                return lv.ALIGN.TOP_RIGHT
            elif value == "top":
                return lv.ALIGN.TOP_MID
            elif value == "bottom-left":
                return lv.ALIGN.BOTTOM_LEFT
            elif value == "bottom-right":
                return lv.ALIGN.BOTTOM_RIGHT
            elif value == "bottom":
                return lv.ALIGN.BOTTOM_MID
            elif value == "left":
                return lv.ALIGN.LEFT_MID
            elif value == "right":
                return lv.ALIGN.RIGHT_MID
            else:
                return lv.ALIGN.DEFAULT
        elif "width" in prop_name or "height" in prop_name:
            if type(value) == float:
                # FIXME Percentage values should be calculated in relation to the parent widget
                new_value = int(value * self.width) if "width" in prop_name else int(value * self.height)
                print(f"Size property conversion: {prop_name}:{value} => {new_value}")
                return new_value
            elif type(value) == int:
                return value
        elif type(value) == int:
            return value
        elif prop_name == "selector":
            if hasattr(lv.PART, value.upper()):
                return getattr(lv.PART, value.upper())
            elif hasattr(lv.STATE, value.upper()):
                return getattr(lv.STATE, value.upper())
            else:
                return None
        # TODO Add more conversions as needed for other property types
        return None

    def apply_style(self, widget, style_name):
        # Style application logic goes here
        # For example, lookup a style in self.data["ui"]["styles"] and apply it to the widget
        if style_name not in self.styles:
            if style_name not in self.ui["styles"]:
                raise ValueError(f"Style not found: {style_name}")
            style = self.create_style(self.ui["styles"][style_name])
            self.styles[style_name] = style
            if "selector" in self.ui["styles"][style_name]:
                selector = self.convert_value("selector", self.ui["styles"][style_name]["selector"])
                if selector == None:
                    print(f"Invalid selector value for style: {style_name}:{self.ui['styles'][style_name]['selector']}")
                    self.styles[f"{style_name}_selector"] = lv.PART.MAIN
                else:
                    self.styles[f"{style_name}_selector"] = selector
            else:
                self.styles[f"{style_name}_selector"] = lv.PART.MAIN
        widget.add_style(self.styles[style_name], self.styles[f"{style_name}_selector"])

# NOTE ------------ GETTERS ------------

    def get_root_widget(self):
        return self.root_widget

if __name__ == "__main__":
    # Load UI from JSON file
    ui_loader = UiLoader("./designs/media_playback_example.json")
    ui_loader.initialize_screen()
    ui_loader.parse_ui()
    root_widget = ui_loader.get_root_widget()
