import sys
if sys.implementation.name == "micropython":
    from display_driver_utils import driver
    import lvgl as lv
    import json
    import random
    from ui import UI
    from widget import *
    from global_definitions import widget_types
else:
    import mock
    import random
    import json
    from .mock.display import driver
    from .mock.lvgl import lv
    from .ui import UI
    from .widget import *
    from .global_definitions import widget_types

class UiLoader:
    """
    A class to load and parse UI designs from JSON files.

    **Class Attributes:**
    - `special_types` A list of special widget types that require custom creation logic.
    - `valid_types` A list of all valid widget types that can be created.
    - `valid_layouts` A list of valid layout types for container widgets.
    - `valid_flow` A list of valid flow types for flex layout containers.
    - `_options` The key for the options property in a container widget.

    **Object Attributes:**
    - `data` The JSON data loaded from the file.
    - `ui` The 'ui' object from the JSON data.
    - `widgets` A dictionary to store references to created widgets.
    - `styles` A dictionary to store references to created styles.
    - `width` The width of the screen.
    - `height` The height of the screen.
    - `title` The title of the window (not used, reference for author).
    - `screen` The display driver object.
    - `root_widget` The root widget object of the UI.
    """
    special_types = ["container", "random"]
    valid_types = special_types + widget_types
    valid_layouts = ["none", "grid", "flex"]
    valid_flow = ["row", "column", "row_wrap", "column_wrap", "row_reverse", "column_reverse"]
    _options = "options"
    def __init__(self, json_file: str):
        # Load JSON data
        self.data = self.load_json_file(json_file)
        if "ui" not in self.data or type(self.data["ui"]) is not dict:
            raise ValueError(f"JSON must have 'ui' property of type dict: {self.data}")
        self.ui = self.data["ui"]
        # Create a dictionary to store references to created widgets
        self.widgets = {}
        self.styles = {}

    @staticmethod
    def load_json_file(filepath: str):
        """
        **Params:**
        - `filepath` The path to the JSON file to load.

        **Returns:**
        - `dict` The JSON data loaded from the file.

        Load and return the JSON data from a file.
        """
        with open(filepath, 'r') as file:
            return json.load(file)
    
    def initialize_screen(self):
        """
        **Returns:**
        - `driver` The display driver object.

        **Raises:**
        - `ValueError` If the 'window' property is missing or invalid.
        - `ValueError` If the 'width' property is missing or invalid.
        - `ValueError` If the 'height' property is missing or invalid.

        Initialize a display driver in the specified width and height of the JSON data to create a window.
        """
        if "window" not in self.ui or type(self.ui["window"]) is not dict:
            raise ValueError(f"UI must have 'window' property of type dict: {self.ui}")
        if "width" not in self.ui["window"] or type(self.ui["window"]["width"]) is not int:
            raise ValueError(f"Window must have 'width' property of type int: {self.ui['window']}")
        if "height" not in self.ui["window"] or type(self.ui["window"]["height"]) is not int:
            raise ValueError(f"Window must have 'height' property of type int: {self.ui['window']}")
        self.width = self.ui["window"]["width"]
        self.height = self.ui["window"]["height"]
        if "title" in self.ui["window"]:
            self.title = self.ui["window"]["title"] # FIXME window title is not used
        self.screen = driver(width=self.width, height=self.height)

    def parse_ui(self):
        """
        **Raises:**
        - `ValueError` If the `root` JSON property is missing or invalid.

        Parse the UI elements under the `root` object of the JSON data.
        """
        if "root" not in self.ui or type(self.ui["root"]) is not dict:
            raise ValueError(f"UI must have 'root' property of type dict: {self.ui}")
        self.root_widget = self.parse_element(self.ui["root"])
        self.root_widget.set_parent(lv.screen_active())
        # NOTE The below can be accomplished by setting the width and height of the root widget via style properties
        self.root_widget.set_width(self.width)
        self.root_widget.set_height(self.height)

    def parse_element(self, element):
        """
        **Params:**
        - `element` The JSON element to parse.

        **Returns:**
        - `lv.obj | lv.button | lv.label | lv.image | lv.line | lv.bar | lv.slider | lv.switch | lv.checkbox | lv.roller | lv.dropdown | lv.textarea | lv.chart` The created widget object based on the element type.

        Parse a widget object JSON element and create the corresponding widget.
        If the element has children, **they will be parsed recursively** and attached to the parent widget.
        If the element has one or more styles, they will be applied to the created widget.
        """
        # Create a widget based on the element type
        widget = self.create_widget(element)
        # Process child elements if they exist
        if "children" in element:
            for child in element["children"]:
                child_widget = self.parse_element(child)
                if child["type"] == "random": # NOTE Random widget is a special case and places itself
                    continue
                child_widget.set_parent(widget)
                if "grid" in element['options']["layout_type"]:
                    self.place_widget_in_grid(child_widget, child)
                    
        if "style" in element:
            if type(element["style"]) is list:
                for style in element["style"]:
                    self.apply_style(widget, style)
            else:
                self.apply_style(widget, element["style"])
        return widget

    def create_widget(self, element) -> lv.obj | lv.button | lv.label | lv.image | lv.line | lv.bar | lv.slider | lv.switch | lv.checkbox | lv.roller | lv.dropdown | lv.textarea | lv.chart:
        """
        **Params:**
        - `element` The JSON element to create the widget from.

        **Returns:**
        - `lv.obj | lv.button | lv.label | lv.image | lv.line | lv.bar | lv.slider | lv.switch | lv.checkbox | lv.roller | lv.dropdown | lv.textarea | lv.chart` The created widget object based on the element type.

        **Raises:**
        - `ValueError` If the widget type is not recognized.
        - `ValueError` If the specified `id` already exists in previously created widgets.

        Create an LVGL widget object based on the type specified in the JSON element.
        """
        widget = None
        widget_type = element["type"]
        if widget_type not in self.valid_types:
            raise ValueError(f"Invalid widget type: {widget_type}. Valid types are: {self.valid_types}")
        if widget_type == 'container':
            widget = self.create_container(element)
        elif widget_type == "random":
            widget = self.create_random_widget(element)
        elif widget_type in widget_mapping.keys():
            widget = widget_mapping[widget_type](element)
        if widget == None:
            raise ValueError(f"Failed to create widget: {element}")
        if 'width' in element:
            widget.set_width(element['width'])
        if 'height' in element:
            widget.set_height(element['height'])
        # Create a unique ID for the widget if it wasn't provided
        if "id" not in element:
            # Count types of the widget
            count = sum([1 for w in self.widgets.values() if type(w) == type(widget)])
            id = f"{widget_type}_{count}"
            self.widgets[id] = widget
            print(f"Created widget '{id}': {element}")
        elif element["id"] in self.widgets:
            raise ValueError(f"Widget with ID '{element['id']}' already exists. IDs must be unique.")
        else:
            self.widgets[element["id"]] = widget
            print(f"Created widget '{element['id']}': {element}")
        return widget

# NOTE ------------ SPECIAL CREATION METHODS ------------

    def create_container(self, element) -> lv.obj:
        """
        **Params:**
        - `element` The JSON element to create the container widget from.

        **Returns:**
        - `lv.obj` The created container widget object.

        **Raises:**
        - `ValueError` If the `id` or `options` properties are missing or invalid.
        - `ValueError` If the `layout_type` property is missing or invalid.
        - `ValueError` If the layout type is `grid` or `flex` and the `layout_options` property is missing or invalid.

        Create a container widget based on the JSON element.
        If the layout type is 'grid' or 'flex', the 'layout_options' property must be present.
        """
        if "id" not in element or type(element["id"]) is not str:
            raise ValueError(f"Container widget must have 'id' of type str: {element}")
        if "options" not in element or type(element["options"]) is not dict:
            raise ValueError(f"Container widget must have 'options' of type dict: {element}")
        options = element["options"]
        if "layout_type" not in options or options["layout_type"] not in self.valid_layouts:
            raise ValueError(f"Container widget must have 'layout_type' property: {options}. Valid options are: {self.valid_layouts}")
        if 'grid' in options["layout_type"] or 'flex' in options["layout_type"]:
            if "layout_options" not in options or type(options["layout_options"]) is not dict:
                raise ValueError(f"Container widget must have 'layout_options' property of type dict: {options}")
        container = lv.obj(lv.screen_active())
        layout = options["layout_type"]
        if layout == "none":
            container.set_layout(lv.LAYOUT.NONE)
            # element["layout_type"] = "none"
        elif layout == "grid":
            self.configure_grid_layout(container, options['layout_options'])
            # element["layout_type"] = "grid"
        elif layout == "flex":
            self.configure_flex_layout(container, options['layout_options'])
            # element["layout_type"] = "flex"
        return container
    
    def configure_flex_layout(self, container: lv.obj, options):
        """
        **Params:**
        - `container` The container widget to configure the flex layout for.
        - `options` The options dictionary for the flex layout.

        **Raises:**
        - `ValueError` If the `flow` property is missing or invalid.

        Configure the flex layout of a container widget based on the options provided in the JSON element.
        """
        if "flow" not in options or options["flow"] not in self.valid_flow:
            raise ValueError(f"Flex layout must have 'flow' property: {options}. Valid options are: {self.valid_flow}")
        container.set_layout(lv.LAYOUT.FLEX)
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

    def configure_grid_layout(self, container: lv.obj, options):
        """
        **Params:**
        - `container` The container widget to configure the grid layout for.
        - `options` The options dictionary for the grid layout.

        **Raises:**
        - `ValueError` If the `grid_dsc` property is missing or invalid.
        - `ValueError` If the `col_dsc` or `row_dsc` properties are missing or invalid.

        Configure the grid layout of a container widget based on the options provided in the JSON element.
        """
        if "grid_dsc" not in options or type(options["grid_dsc"]) is not dict:
            raise ValueError(f"Grid layout must have 'grid_dsc' of type dict: {options}")
        container.set_layout(lv.LAYOUT.GRID)
        # TODO Need to properly handle grid placements of children with grid layout
        if "col_dsc" not in options["grid_dsc"] or type(options["grid_dsc"]["col_dsc"]) is not list or "row_dsc" not in options["grid_dsc"] or type(options["grid_dsc"]["row_dsc"]) is not list:
            raise ValueError(f"grid_dsc must have 'col_dsc' and 'row_dsc' of type list: {options['grid_dsc']}")
        col_dsc = []
        for col in options["grid_dsc"]["col_dsc"]:
            col_dsc.append(lv.GRID_CONTENT) # NOTE Hotfix for ChatGPT (always use content for proper sizes)
            # if type(col) is int:
            #     col_dsc.append(col)
            # elif type(col) is str:
            #     if col.endswith("fr"):
            #         col_dsc.append(lv.grid_fr(int(col.strip("fr"))))
            #     elif col == "content":
            #         col_dsc.append(lv.GRID_CONTENT)
            #     else:
            #         raise ValueError(f"Unsupported column description: {col}. Must be an integer, '#fr' value or 'content'.")
        row_dsc = []
        for row in options["grid_dsc"]["row_dsc"]:
            row_dsc.append(lv.GRID_CONTENT) # NOTE Hotfix for ChatGPT (always use content for proper sizes)
            # if type(row) is int:
            #     row_dsc.append(row)
            # elif type(row) is str:
            #     if row.endswith("fr"):
            #         row_dsc.append(lv.grid_fr(int(row.strip("fr"))))
            #     elif row == "content":
            #         row_dsc.append(lv.GRID_CONTENT)
            #     else:
            #         raise ValueError(f"Unsupported row description: {row}. Must be an integer, '#fr' value or 'content'.")
        container.set_grid_dsc_array(col_dsc, row_dsc)

    def create_random_widget(self, element):
        """
        **Params:**
        - `element` The JSON element to create the random widget from.

        **Returns:**
        - `lv.obj | lv.button | lv.label | lv.image | lv.line | lv.bar | lv.slider | lv.switch | lv.checkbox | lv.roller | lv.dropdown | lv.textarea | lv.chart` The created random widget object.

        **Raises:**
        - `ValueError` If the `parent_id`, `count`, or `widget_list` properties are missing or invalid.

        Create a random widget based on the JSON element.
        A random type is chosen from the 'widget_list' property. The chosen type is then passed to the widget creation function.
        This is done X times based on the 'count' property.
        """
        if "parent_id" not in element or type(element["parent_id"]) is not str:
            raise ValueError(f"Random widget must have 'parent_id' of type str: {element}")
        if "count" not in element or type(element["count"]) is not int:
            raise ValueError(f"Random widget must have 'count' of type int: {element}")
        if "widget_list" not in element or type(element["widget_list"]) is not list:
            raise ValueError(f"Random widget must have 'widget_list' of type list: {element}")
        for i in range(element["count"]):
            element["type"] = random.choice(element["widget_list"])
            widget = self.create_widget(element)
            widget.set_parent(self.widgets[element["parent_id"]])
            if "style" in element:
                if type(element["style"]) is list:
                    for style in element["style"]:
                        self.apply_style(widget, style)
                else:
                    self.apply_style(widget, element["style"])
            if "placement" in element:
                # NOTE Assuming parent is grid layout if "placement" is present
                # FIXME placement should be adjusted for each created random widget, as they can't all be in the same spot
                self.place_widget_in_grid(widget, element)
        return widget
    
    def place_widget_in_grid(self, widget: lv.obj, child_element):
        """
        **Params:**
        - `widget` The widget to place in the grid container.
        - `child_element` The JSON element of the child widget to place in the grid container.

        **Raises:**
        - `ValueError` If the `placement` property is missing or invalid.
        - `ValueError` If the `col_pos`, `col_span`, `row_pos`, or `row_span` properties are missing or invalid.

        Place the provided child widget in the grid container widget based on the 'placement' property in the child JSON element.
        """
        if "placement" not in child_element or type(child_element["placement"]) is not dict:
            raise ValueError(f"Child element of grid layout must have 'placement' property of type 'dict': {child_element}")
        # placement options: column_align: Unknown, col_pos: int, col_span: int, row_align: Unknown, row_pos: int, row_span: int
        if "col_pos" not in child_element["placement"] or type(child_element["placement"]["col_pos"]) is not int:
            raise ValueError(f"Child element of grid layout must have 'col_pos' property of type 'int': {child_element}")
        if "col_span" not in child_element["placement"] or type(child_element["placement"]["col_span"]) is not int:
            raise ValueError(f"Child element of grid layout must have 'col_span' property of type 'int': {child_element}")
        if "row_pos" not in child_element["placement"] or type(child_element["placement"]["row_pos"]) is not int:
            raise ValueError(f"Child element of grid layout must have 'row_pos' property of type 'int': {child_element}")
        if "row_span" not in child_element["placement"] or type(child_element["placement"]["row_span"]) is not int: 
            raise ValueError(f"Child element of grid layout must have 'row_span' property of type 'int': {child_element}")
        row_align = child_element["placement"].get("row_align", "space_evenly")
        col_align = child_element["placement"].get("col_align", "space_evenly")
        row_align = getattr(lv.GRID_ALIGN, row_align.upper(), lv.GRID_ALIGN.SPACE_EVENLY)
        col_align = getattr(lv.GRID_ALIGN, col_align.upper(), lv.GRID_ALIGN.SPACE_EVENLY)
        widget.set_grid_cell(col_align, child_element["placement"]["col_pos"], child_element["placement"]["col_span"], row_align, child_element["placement"]["row_pos"], child_element["placement"]["row_span"])

# TODO Should update the JSON tree with all randomly created values to export the UI back to JSON again
    
# NOTE ------------ STYLE CREATION METHODS ------------
    
    def create_style(self, style_def):
        """
        **Params:**
        - `style_def` The JSON style definition to create the style object from.

        **Returns:**
        - `lv.style_t` The created style object.

        Create an LVGL style object based on the style definition provided in the JSON data.
        Provided style property values are converted to the required type, according to conversion rules of the called conversion function.
        If a style property is not recognized, a message is printed to the console and the property is skipped.
        If value conversion fails, a message is printed to the console and the property is skipped.
        """
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
        """
        **Params:**
        - `prop_name` The name of the property to convert the value for.
        - `value` The value to convert to the required type.

        **Returns:**
        - `int | str | lv.color_t | lv.font_t | lv.align_t | lv.OPA | None` The converted value based on the property name.
        - `None` If the conversion fails.

        Convert the provided value to the required type based on the property name.
        If there is no conversion available for the property, None is returned. (i.e. conversion fails)
        """
        # This function converts the value based on the property name
        if "color" in prop_name:
            converted_value = int(value.strip("#"), 16)
            print(f"set_{prop_name}: Color property conversion:{value} => {converted_value:x}")
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
        elif "opa" in prop_name:
            if type(value) != int:
                print(f"{prop_name}: Invalid opacity value: {value} (expected int)")
                return None
            opacity = int(value / 10)
            if opacity == 0:
                return lv.OPA._0
            elif opacity == 1:
                return lv.OPA._10
            elif opacity == 2:
                return lv.OPA._20
            elif opacity == 3:
                return lv.OPA._30
            elif opacity == 4:
                return lv.OPA._40
            elif opacity == 5:
                return lv.OPA._50
            elif opacity == 6:
                return lv.OPA._60
            elif opacity == 7:
                return lv.OPA._70
            elif opacity == 8:
                return lv.OPA._80
            elif opacity == 9:
                return lv.OPA._90
            elif opacity == 10:
                return lv.OPA._100
            else:
                return lv.OPA.TRANSP
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
        """
        **Params:**
        - `widget` The widget object to apply the style to.
        - `style_name` The name of the style to apply to the widget.

        **Raises:**
        - `ValueError` If the style does not exist in the JSON data.

        Lookup the style name in the list of styles and apply the created style object to the widget.
        If the style name is not found in the list of styles, a new style is created and added to the list.
        """
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

    def update_screen(self):
        """Re-render the screen & update the layout."""
        lv.screen_load(self.root_widget)
        self.root_widget.update_layout()
# NOTE ------------ GETTERS ------------

    def get_root_widget(self):
        """Return the root widget object (container) of the UI."""
        return self.root_widget
    
    def get_ui(self) -> UI:
        """
        **Returns:**
        - `UI` The UI object containing the metadata.

        Return a UI object (special dictionary) containing the screen dimensions and all widget position metadata required for bounding box annotation.
        """
        ui = UI()
        ui["count"] = len(self.widgets)
        self.update_screen()
        for id, widget in self.widgets.items():
            if type(widget) is lv.obj:
                continue # Skip container widgets
            widget_info = {}
            tmp_coords = lv.area_t()
            widget.get_coords(tmp_coords)
            widget_info["x"] = (tmp_coords.x1 + tmp_coords.x2) // 2
            widget_info["y"] = (tmp_coords.y1 + tmp_coords.y2) // 2
            widget_info["width"] = widget.get_width()
            widget_info["height"] = widget.get_height()
            widget_info["class"] = widget.__class__.__name__
            print(f"Widget {id}: {widget_info}")
            ui["objects"].append(widget_info)
        return ui
    
    def cleanup(self):
        """
        Cleanup the screen and widgets, destroying all created objects.
        Note that this function will cause a known error when sub-widgets are indirectly deleted by destroying their parent container.
        That error is safe to ignore, as the widgets should be properly deleted by LVGL.
        """
        # Cleanup the screen and widgets (passing twice to delete widgets before containers)
        for id, widget in self.widgets.items():
            try:
                widget.delete()
                self.widgets.pop(id)
            except Exception as e:
                print(f"Error deleting widget {id}: {e}")
        

if __name__ == "__main__":
    # Load UI from JSON file
    ui_loader = UiLoader("./designs/ui_attempt1.json")
    ui_loader.initialize_screen()
    ui_loader.parse_ui()
    root_widget = ui_loader.get_root_widget()
    ui = ui_loader.get_ui()
    print(ui)
