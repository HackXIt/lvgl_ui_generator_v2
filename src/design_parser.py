from display_driver_utils import driver
import lvgl as lv
import json
import random
from ui import UI

ascii_letters = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

class UiLoader:
    special_types = ["container", "random"]
    widget_types = ["arc", "bar", "button", "buttonmatrix", "calendar", "chart", "checkbox", "dropdown", "image", "imagebutton", "keyboard", "label", "led", "line", "list", "menu", "messagebox", "roller", "scale", "slider", "spangroup", "spinbox", "spinner", "switch", "table", "tabview", "textarea", "tileview", "window"]
    valid_types = special_types + widget_types
    valid_layouts = ["none", "grid", "flex"]
    valid_flow = ["row", "column", "row_wrap", "column_wrap", "row_reverse", "column_reverse"]
    _options = "options"
    def __init__(self, json_file):
        # Load JSON data from file
        with open(json_file, "r") as file:
            json_data = file.read()
        # Load JSON data
        self.data = json.loads(json_data)
        if "ui" not in self.data or type(self.data["ui"]) is not dict:
            raise ValueError(f"JSON must have 'ui' property of type dict: {self.data}")
        self.ui = self.data["ui"]
        # Create a dictionary to store references to created widgets
        self.widgets = {}
        self.styles = {}
    
    def initialize_screen(self):
        # Create the screen
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
        # Parse the root element
        if "root" not in self.ui or type(self.ui["root"]) is not dict:
            raise ValueError(f"UI must have 'root' property of type dict: {self.ui}")
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
                if child["type"] == "random": # NOTE Random widget is a special case and places itself
                    continue
                child_widget.set_parent(widget)
                if "grid" in element["layout_type"]:
                    self.place_widget_in_grid(child_widget, child)
                    
        if "style" in element:
            self.apply_style(widget, element["style"])
        return widget

    def create_widget(self, element) -> lv.obj | lv.button | lv.label | lv.image | lv.line | lv.bar | lv.slider | lv.switch | lv.checkbox | lv.roller | lv.dropdown | lv.textarea | lv.chart:
        widget = None
        widget_type = element["type"]
        if widget_type not in self.valid_types:
            raise ValueError(f"Invalid widget type: {widget_type}. Valid types are: {self.valid_types}")
        if widget_type == 'container':
            widget = self.create_container(element)
        elif widget_type == "random":
            widget = self.create_random_widget(element)
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
        if widget == None:
            raise ValueError(f"Failed to create widget: {element}")
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
        if "id" not in element or type(element["id"]) is not str:
            raise ValueError(f"Container widget must have 'id' of type str: {element}")
        if "options" not in element or type(element["options"]) is not dict:
            raise ValueError(f"Container widget must have 'options' of type dict: {element}")
        options = element["options"]
        if "layout" not in options or options["layout"] not in self.valid_layouts:
            raise ValueError(f"Container widget must have 'layout' property: {options}. Valid options are: {self.valid_layouts}")
        container = lv.obj(lv.screen_active())
        layout = options["layout"]
        if layout == "none":
            container.set_layout(lv.LAYOUT.NONE)
            element["layout_type"] = "none"
        elif layout == "grid":
            self.configure_grid_layout(container, options)
            element["layout_type"] = "grid"
        elif layout == "flex":
            self.configure_flex_layout(container, options)
            element["layout_type"] = "flex"
        return container
    
    def configure_flex_layout(self, container, options):
        container.set_layout(lv.LAYOUT.FLEX)
        if "flow" not in options or options["flow"] not in self.valid_flow:
            raise ValueError(f"Flex layout must have 'flow' property: {options}. Valid options are: {self.valid_flow}")
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
        if "grid_dsc" not in options or type(options["grid_dsc"]) is not dict:
            raise ValueError(f"Grid layout must have 'grid_dsc' of type dict: {options}")
        container.set_layout(lv.LAYOUT.GRID)
        # TODO Need to properly handle grid placements of children with grid layout
        if "col_dsc" not in options["grid_dsc"] or type(options["grid_dsc"]["col_dsc"]) is not list or "row_dsc" not in options["grid_dsc"] or type(options["grid_dsc"]["row_dsc"]) is not list:
            raise ValueError(f"grid_dsc must have 'col_dsc' and 'row_dsc' of type list: {options['grid_dsc']}")
        col_dsc = []
        for col in options["grid_dsc"]["col_dsc"]:
            if type(col) is int:
                col_dsc.append(col)
            elif type(col) is str:
                if col.endswith("fr"):
                    col_dsc.append(lv.grid_fr(int(col.strip("fr"))))
                elif col == "content":
                    col_dsc.append(lv.GRID_CONTENT)
                else:
                    raise ValueError(f"Unsupported column description: {col}. Must be an integer, '#fr' value or 'content'.")
        row_dsc = []
        for row in options["grid_dsc"]["row_dsc"]:
            if type(row) is int:
                row_dsc.append(row)
            elif type(row) is str:
                if row.endswith("fr"):
                    row_dsc.append(lv.grid_fr(int(row.strip("fr"))))
                elif row == "content":
                    row_dsc.append(lv.GRID_CONTENT)
                else:
                    raise ValueError(f"Unsupported row description: {row}. Must be an integer, '#fr' value or 'content'.")
        container.set_grid_dsc_array(col_dsc, row_dsc)

    def create_random_widget(self, element):
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
                self.apply_style(widget, element["style"])
            if "placement" in element:
                # NOTE Assuming parent is grid layout if "placement" is present
                # FIXME placement should be adjusted for each created random widget, as they can't all be in the same spot
                self.place_widget_in_grid(widget, element)
        return widget
    
    def place_widget_in_grid(self, widget: lv.obj, child_element):
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

# NOTE ------------ WIDGET CREATION METHODS ------------
# TODO Should update the JSON tree with all randomly created values to export the UI back to JSON again

    def create_arc(self, element) -> lv.arc:
        widget = lv.arc(lv.screen_active())
        if "options" in element:
            mode = element["options"].get("mode", "normal")
            arc_mode = getattr(lv.arc.MODE, mode.upper(), lv.arc.MODE.NORMAL)
            range_max = element["options"].get("range_max", random.randint(1, 100))
            range_min = element["options"].get("range_min", random.randint(1, range_max))
            value = element["options"].get("value", random.randint(range_min, range_max))
            rotation = element["options"].get("rotation", 0)
            angle_start, angle_end = element["options"].get("angle_range", (0, 360))
            widget.set_mode(arc_mode)
            widget.set_angles(angle_start, angle_end)   
            widget.set_rotation(rotation)
            widget.set_range(range_min, range_max)
            widget.set_value(value)
        else:
            range_max = random.randint(0, 100)
            range_min = random.randint(0, range_max)
            # NOTE Leave other arc properties at default
            widget.set_mode(lv.arc.MODE.NORMAL)
            widget.set_range(range_min, range_max)
            widget.set_value(random.randint(range_min, range_max))
        return widget
    
    def create_bar(self, element) -> lv.bar:
        widget = lv.bar(lv.screen_active())
        if "options" in element:
            range_min = element["options"].get("range_min", 0)
            range_max = element["options"].get("range_max", 100)
            value = element["options"].get("value", random.randint(range_min, range_max))
            widget.set_range(range_min, range_max)
            widget.set_value(value, lv.ANIM.ON)
        else:
            widget.set_range(0, 100)
            widget.set_value(random.randint(0, 100), lv.ANIM.ON)
        return widget
    
    def create_button(self, element) -> lv.button:
        widget = lv.button(lv.screen_active())
        if "options" in element:
            # FIXME when both text and symbol are provided, they will overlap, but should be placed side by side
            if "text" in element["options"]:
                label = lv.label(widget) # FIXME Label of button currently ignores style properties (uses defaults)
                label.set_parent(widget)
                label.set_text(element["options"]["text"])
            if "symbol" in element["options"]:
                symbol = element["options"]["symbol"]
                if hasattr(lv.SYMBOL, symbol.upper()):
                    widget.set_style_bg_image_src(getattr(lv.SYMBOL, symbol.upper()), 0)
        else:
            label = lv.label(widget)
            label.set_parent(widget)
            label.set_text("".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
        return widget
    
    def create_buttonmatrix(self, element) -> lv.buttonmatrix:
        widget = lv.buttonmatrix(lv.screen_active())
        if "options" in element:
            map = element["options"].get("map", [random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
            widget.set_map(map)
        else:
            widget.set_map([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
        return widget
    
    def create_calendar(self, element) -> lv.calendar:
        widget = lv.calendar(lv.screen_active())
        if "options" in element:
            current_date = element["options"].get("current_date", {"year": 2024, "month": 3, "day": 30})
            showed_date = element["options"].get("showed_date", {"year": 2024, "month": 3})
            if "year" not in current_date or "month" not in current_date or "day" not in current_date:
                raise ValueError(f"Invalid date format for current_date: {current_date}. Must have 'year', 'month', 'day' keys.")
            if "year" not in showed_date or "month" not in showed_date:
                raise ValueError(f"Invalid date format for showed_date: {showed_date}. Must have 'year', 'month' keys.")
            date_highlights = element["options"].get("date_highlights", [])
            widget.set_today_date(current_date.year, current_date.month, current_date.day)
            widget.set_showed_date(showed_date.year, showed_date.month)
            if len(date_highlights) > 0:
                if type(date_highlights) is not list:
                    raise ValueError(f"Invalid date_highlights format: {date_highlights}. Must be a list.")
                highlights = []
                for date_highlight in date_highlights:
                    if "year" not in date_highlight or "month" not in date_highlight or "day" not in date_highlight:
                        raise ValueError(f"Invalid date format for date_highlight: {date_highlight}. Must have 'year', 'month', 'day' keys.")
                    date = lv.calendar_date_t()
                    date.year = date_highlight.year
                    date.month = date_highlight.month
                    date.day = date_highlight.day
                    highlights.append(date)
                widget.set_highlighted_dates(highlights, len(highlights))
        else:
            widget.set_today_date(2024, 3, 30)
            widget.set_showed_date(2024, 3)
            highlight = lv.calendar_date_t()
            highlight.year = 2024
            highlight.month = 3
            highlight.day = 29
            widget.set_highlighted_dates([highlight], 1)
        return widget
    
    def create_chart(self, element) -> lv.chart:
        # TODO Implement chart widget (also tough to implement)
        widget = lv.chart(lv.screen_active())
        return widget
    
    def create_canvas(self, element) -> lv.canvas:
        # TODO Implement canvas widget
        widget = lv.canvas(lv.screen_active())
        return widget
    
    def create_checkbox(self, element) -> lv.checkbox:
        widget = lv.checkbox(lv.screen_active())
        if "options" in element:
            state = element["options"].get("state", "disabled")
            cb_state = getattr(lv.STATE, state.upper(), lv.STATE.DISABLED)
            widget.add_state(cb_state)
        else:
            widget.add_state(lv.STATE.DEFAULT)
        return widget
    
    def create_dropdown(self, element) -> lv.dropdown:
        widget = lv.dropdown(lv.screen_active())
        if "options" in element:
            entries = element["options"].get("entries", [])
            if len(entries) == 0:
                for i in range(random.randint(1, 10)):
                    entries.append("".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
            widget.set_options("\n".join(entries))
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
        if "options" in element:
            text = element["options"].get("text", "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
        else:
            text = "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
        widget.set_text(text)
        return widget
    
    def create_led(self, element) -> lv.led:
        widget = lv.led(lv.screen_active())
        if "options" in element:
            brightness = element["options"].get("brightness", 100)
            widget.set_brightness(brightness)
        else:
            widget.set_brightness(random.randint(0, 100))
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
        widget = lv.roller(lv.screen_active())
        if "options" in element:
            entries = element["options"].get("entries", [random.choice(ascii_letters) for _ in range(1, random.randint(1, 10))])
            mode = element["options"].get("mode", "infinite")
            visible_rows = element["options"].get("visible_rows", 3)
            roller_mode = getattr(lv.roller.MODE, mode.upper(), lv.roller.MODE.INFINITE)
            widget.set_options("\n".join(entries), roller_mode)
            widget.set_visible_row_count(visible_rows)
        else:
            widget.set_options("\n".join([random.choice(ascii_letters) for _ in range(1, random.randint(1, 10))]), lv.roller.MODE.INFINITE)
        return widget
    
    def create_scale(self, element) -> lv.scale:
        widget = lv.scale(lv.screen_active())
        if "options" in element:
            mode = element["options"].get("mode", "horizontal_bottom")
            scale_mode = getattr(lv.scale.MODE, mode.upper(), lv.scale.MODE.HORIZONTAL_BOTTOM)
            show_label = element["options"].get("show_label", True)
            total_ticks = element["options"].get("total_ticks", random.randint(1, 100))
            major_ticks = element["options"].get("major_ticks", random.randint(1, total_ticks))
            major_range = element["options"].get("major_range", random.randint(1, 100))
            minor_range = element["options"].get("minor_range", random.randint(1, major_range))
            sections = element["options"].get("sections", random.randint(1, 10))
            default_labels = [random.choice(ascii_letters) for _ in range(sections)]
            labels = element["options"].get("labels", default_labels)
            widget.set_mode(scale_mode)
            widget.set_range(minor_range, major_range)
            widget.set_total_tick_count(total_ticks)
            widget.set_major_tick_every(major_ticks)
            widget.set_label_show(show_label)
            widget.set_text_src(labels)
        else:
            widget.set_mode(lv.scale.MODE.HORIZONTAL_BOTTOM)
            widget.set_range(0, 100)
            widget.set_total_tick_count(random.randint(1, 100))
            widget.set_major_tick_every(random.randint(1, 100))
            widget.set_label_show(True)
            widget.set_text_src([c for _ in range(random.randint(1, 10)) for c in ascii_letters])
        return widget

    def create_slider(self, element) -> lv.slider:
        widget = lv.slider(lv.screen_active())
        if "options" in element:
            range_min = element["options"].get("range_min", 0)
            range_max = element["options"].get("range_max", 100)
            value = element["options"].get("value", 0)
            widget.set_range(range_min, range_max)
            widget.set_value(value, lv.ANIM.ON)
        else:
            widget.set_range(0, 100)
            widget.set_value(random.randint(0, 100), lv.ANIM.ON)
        return widget

    def create_spangroup(self, element) -> lv.spangroup:
        # TODO Implement span widget
        widget = lv.spangroup(lv.screen_active())
        return widget

    def create_spinbox(self, element) -> lv.spinbox:
        widget = lv.spinbox(lv.screen_active())
        if "options" in element:
            range_min = element["options"].get("range_min", 0)
            range_max = element["options"].get("range_max", 100)
            step = element["options"].get("step", 1)
            value = element["options"].get("value", random.randint(0, 100))
            widget.set_range(range_min, range_max)
            widget.set_step(step)
            widget.set_value(value)
        else:
            min = random.randint(0, 100)
            max = random.randint(min, 100)
            step = random.randint(1, 10)
            value = random.randint(min, max)
            widget.set_range(min, max)
            widget.set_step(step)
            widget.set_value(value)
        return widget

    def create_spinner(self, element) -> lv.spinner:
        # TODO Implement spinner widget
        widget = lv.spinner(lv.screen_active())
        return widget

    def create_switch(self, element) -> lv.switch:
        widget = lv.switch(lv.screen_active())
        if "options" in element:
            state = element["options"].get("state", False)
            sw_state = getattr(lv.STATE, state.upper(), lv.STATE.DISABLED)
            widget.add_state(sw_state)
        else:
            widget.add_state(lv.STATE.DEFAULT)
        return widget
    
    def create_table(self, element) -> lv.table:
        widget = lv.table(lv.screen_active())
        if "options" in element:
            col_cnt = element["options"].get("column_count", 1)
            row_cnt = element["options"].get("row_count", 1)
            widget.set_column_count(col_cnt)
            widget.set_row_count(row_cnt)
        else:
            widget.set_column_count(random.randint(1, 10))
            widget.set_row_count(random.randint(1, 10))
        return widget

    def create_tabview(self, element) -> lv.tabview:
        # TODO Implement tabview widget
        widget = lv.tabview(lv.screen_active())
        return widget

    def create_textarea(self, element) -> lv.textarea:
        widget = lv.textarea(lv.screen_active())
        if "options" in element:
            text = element["options"].get("text", str([c for _ in range(random.randint(10, 100)) for c in ascii_letters]))
            widget.set_text(text)
        else:
            widget.set_text(str([c for _ in range(random.randint(10, 100)) for c in ascii_letters]))
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
    
    def get_ui(self) -> UI:
        ui = UI()
        ui["count"] = len(self.widgets)
        lv.screen_load(self.root_widget)
        self.root_widget.update_layout()
        # FIXME coordinates are not accurate/relative to the whole window, only relative to parent container (which is incorrect for nested containers)
        for id, widget in self.widgets.items():
            if type(widget) is lv.obj:
                continue # Skip container widgets
            widget_info = {}
            widget_info["x"] = widget.get_x()
            widget_info["y"] = widget.get_y()
            widget_info["width"] = widget.get_width()
            widget_info["height"] = widget.get_height()
            widget_info["class"] = widget.__class__.__name__
            print(f"Widget {id}: {widget_info}")
            ui["objects"].append(widget_info)
        return ui

if __name__ == "__main__":
    # Load UI from JSON file
    ui_loader = UiLoader("./designs/ui_attempt1.json")
    ui_loader.initialize_screen()
    ui_loader.parse_ui()
    root_widget = ui_loader.get_root_widget()
