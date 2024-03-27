from display_driver_utils import driver
import lvgl as lv
import json
import random

class UiLoader:
    valid_types = ["container", "label", "button", "image", "line", "bar", "slider", "switch", "checkbox", "roller", "dropdown", "textarea", "chart", "random"]
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
        return widget

    def create_widget(self, element) -> lv.obj | lv.button | lv.label | lv.image | lv.line | lv.bar | lv.slider | lv.switch | lv.checkbox | lv.roller | lv.dropdown | lv.textarea | lv.chart:
        widget = None
        widget_type = element["type"]
        if widget_type not in self.valid_types:
            raise ValueError(f"Invalid widget type: {widget_type}, valid types are: {self.valid_types}")
        if widget_type == 'container':
            widget = lv.obj(lv.screen_active())
        elif widget_type == 'button':
            widget = lv.button(lv.screen_active())
            label = lv.label(widget)
            label.set_parent(widget)
            label.set_text(element["text"]) if "text" in element else label.set_text('Button')
        elif widget_type == 'label':
            widget = lv.label(lv.screen_active())
            widget.set_text(element["text"]) if "text" in element else widget.set_text('Label')
        elif widget_type == 'image':
            widget = lv.image(lv.screen_active())
            # widget.set_src(lv.SYMBOL.OK)
        elif widget_type == 'line':
            widget = lv.line(lv.screen_active())
            # widget.set_points([(0, 0), (self.width, self.height)])
        elif widget_type == 'bar':
            widget = lv.bar(lv.screen_active())
            # widget.set_value(50, lv.ANIM.ON)
        elif widget_type == 'slider':
            widget = lv.slider(lv.screen_active())
            # widget.set_range(0, 100)
            # widget.set_value(50, lv.ANIM.ON)
        elif widget_type == 'switch':
            widget = lv.switch(lv.screen_active())
        elif widget_type == 'checkbox':
            widget = lv.checkbox(lv.screen_active())
            # widget.set_text('Checkbox')
        elif widget_type == 'roller':
            widget = lv.roller(lv.screen_active())
            # for i in range(random.randint(1, 10)):
            #     options = '\n'.join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
            # widget.set_options(options)
        elif widget_type == 'dropdown':
            widget = lv.dropdown(lv.screen_active())
            # for i in range(random.randint(1, 10)):
            #     options = '\n'.join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
            # widget.set_options(options)
        elif widget_type == 'textarea':
            widget = lv.textarea(lv.screen_active())
            # widget.set_text('Textarea')
        elif widget_type == 'chart':
            widget = lv.chart(lv.screen_active())
            # ser1 = widget.add_series(lv.color_hex(0x2587FF))
            # ser2 = widget.add_series(lv.color_hex(0xFF0000))
            # widget.set_type(ser1, lv.chart.TYPE.LINE | lv.chart.TYPE.LINE)
            # widget.set_type(ser2, lv.chart.TYPE.LINE | lv.chart.TYPE.LINE)
            # widget.set_point_count(ser1, 10)
            # widget.set_point_count(ser2, 10)
            # widget.set_ext_y_array(ser1, [lv.OPA.COVER, lv.OPA.COVER, lv.OPA.COVER, lv.OPA.COVER])
        elif widget_type == "random":
            choice = random.choice(list(filter(lambda x: x != "random", element["options"])))
            element["type"] = choice
            return self.create_widget(element)

        # Apply styles (more complex style handling should be added here)
        if "style" in element:
            self.apply_style(widget, element["style"]) if widget else print(f"No widget to apply style to. {element}")

        # Store widget reference by id if id exists
        if "id" in element:
            self.widgets[element["id"]] = widget

        return widget
    
    def create_style(self, style_def):
        print(f"Creating style: {style_def}")
        style = lv.style_t()
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

    def get_root_widget(self):
        return self.root_widget

if __name__ == "__main__":
    # Load UI from JSON file
    ui_loader = UiLoader("./designs/example.json")
    ui_loader.initialize_screen()
    ui_loader.parse_ui()
    root_widget = ui_loader.get_root_widget()
