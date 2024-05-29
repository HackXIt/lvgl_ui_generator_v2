import sys
if sys.implementation.name == "micropython":
    import lvgl as lv
    import random
    from global_definitions import ascii_letters
else:
    import mock
    from .mock.lvgl import lv
    import random
    from .global_definitions import ascii_letters

# NOTE ------------ WIDGET HELPER METHODS ------------
def randomize_state(widget: lv.obj):
    """
    **Params**
    - `widget` The widget to randomize the state of.

    **Raises**:
    - `AttributeError` If the widget does not have a 'state' property.

    Randomize the state of a widget.

    **Example**
    ```json
    {
        "type": "button",
        "options": {
            "text": "Button",
            "state": "focused"
        }
    }
    ```
    """
    if hasattr(widget, "set_state"):
        state = random.choice([lv.STATE.CHECKED, lv.STATE.DISABLED, lv.STATE.FOCUSED, lv.STATE.PRESSED, lv.STATE.HOVERED, lv.STATE.EDITED])
        widget.set_state(state, True) # Add the state
    else:
        raise AttributeError(f"Widget {widget} does not have a 'state' property.")

# NOTE ------------ WIDGET CREATION METHODS ------------
def create_arc(element) -> lv.arc:
    """
    **Params**
    - `element` The JSON element to create the arc widget from.

    **Returns**
    - `lv.arc` The created arc widget.

    Create an arc widget from a JSON element.

    **Example**
    ```json
    {
        "type": "arc",
        "options": {
            "mode": "normal",
            "range_max": 100,
            "range_min": 0,
            "value": 50,
            "rotation": 0,
            "angle_range": [0, 360]
        }
    }
    ```
    """
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

def create_bar(element) -> lv.bar:
    """
    **Params**
    - `element` The JSON element to create the bar widget from.

    **Returns**
    - `lv.bar` The created bar widget.

    Create a bar widget from a JSON element.

    **Example**
    ```json
    {
        "type": "bar",
        "options": {
            "range_min": 0,
            "range_max": 100,
            "value": 50
        }
    }
    ```
    """
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

def create_button(element) -> lv.button:
    """
    **Params**
    - `element` The JSON element to create the button widget from.

    **Returns**
    - `lv.button` The created button widget.

    Create a button widget from a JSON element.

    **Example**
    ```json
    {
        "type": "button",
        "options": {
            "text": "Button",
            "symbol": "OK"
        }
    }
    ```
    """
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

def create_buttonmatrix(element) -> lv.buttonmatrix:
    """
    **Params**
    - `element` The JSON element to create the buttonmatrix widget from.

    **Returns**
    - `lv.buttonmatrix` The created buttonmatrix widget.

    Create a buttonmatrix widget from a JSON element.

    **Example**
    ```json
    {
        "type": "buttonmatrix",
        "options": {
            "map": [
                ["A", "B", "C"],
                ["D", "E", "F"],
                ["G", "H", "I"]
            ]
        }
    }
    ```
    """
    widget = lv.buttonmatrix(lv.screen_active())
    if "options" in element:
        map = element["options"].get("map", [random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
        if type(map[0]) is list:
            # NOTE Flatten the map
            new_map = []
            for i in range(len(map)):
                for j in range(len(map[i])):
                    new_map.append(map[i][j])
                if i != len(map) - 1:
                    new_map.append("\n")
            new_map.append("") # NOTE Add an empty string to the end (must be done according to docs)
            map = new_map
            print(f"New map: {map}")
        widget.set_map(map)
    else:
        widget.set_map(["".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]) for _ in range(random.randint(1, 10))])
    return widget

def create_calendar(element) -> lv.calendar:
    """
    **Params**
    - `element` The JSON element to create the calendar widget from.

    **Returns**
    - `lv.calendar` The created calendar widget.

    **Raises**:
    - `ValueError` If the date dictionary format is invalid (missing 'year', 'month', 'day' keys).
    - `ValueError` If the date_highlights list format is invalid.

    Create a calendar widget from a JSON element.

    **Example**
    ```json
    {
        "type": "calendar",
        "options": {
            "current_date": {"year": 2024, "month": 3, "day": 30},
            "showed_date": {"year": 2024, "month": 3},
            "date_highlights": [
                {"year": 2024, "month": 3, "day": 29}
            ]
        }
    }
    ```
    """
    widget = lv.calendar(lv.screen_active())
    if "options" in element:
        current_date = element["options"].get("current_date", {"year": 2024, "month": 3, "day": 30})
        showed_date = element["options"].get("showed_date", {"year": 2024, "month": 3})
        if "year" not in current_date or "month" not in current_date or "day" not in current_date:
            raise ValueError(f"Invalid date format for current_date: {current_date}. Must have 'year', 'month', 'day' keys.")
        if "year" not in showed_date or "month" not in showed_date:
            raise ValueError(f"Invalid date format for showed_date: {showed_date}. Must have 'year', 'month' keys.")
        date_highlights = element["options"].get("date_highlights", [])
        widget.set_today_date(current_date['year'], current_date['month'], current_date['day'])
        widget.set_showed_date(showed_date['year'], showed_date['month'])
        if len(date_highlights) > 0:
            if type(date_highlights) is not list:
                raise ValueError(f"Invalid date_highlights format: {date_highlights}. Must be a list.")
            highlights = []
            for date_highlight in date_highlights:
                if "year" not in date_highlight or "month" not in date_highlight or "day" not in date_highlight:
                    raise ValueError(f"Invalid date format for date_highlight: {date_highlight}. Must have 'year', 'month', 'day' keys.")
                date = lv.calendar_date_t()
                date.year = date_highlight['year']
                date.month = date_highlight['month']
                date.day = date_highlight['day']
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

def create_canvas(element) -> lv.canvas:
    """
    **Params**
    - `element` The JSON element to create the canvas widget from.

    **Returns**
    - `lv.canvas` The created canvas widget.

    Create a canvas widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement canvas widget
    widget = lv.canvas(lv.screen_active())
    return widget

def create_chart(element) -> lv.chart:
    """
    **Params**
    - `element` The JSON element to create the chart widget from.

    **Returns**
    - `lv.chart` The created chart widget.

    Create a chart widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement chart widget (also tough to implement)
    widget = lv.chart(lv.screen_active())
    return widget

def create_checkbox(element) -> lv.checkbox:
    """
    **Params**
    - `element` The JSON element to create the checkbox widget from.

    **Returns**
    - `lv.checkbox` The created checkbox widget.

    Create a checkbox widget from a JSON element.

    **Example**
    ```json
    {
        "type": "checkbox",
        "options": {
            "state": "checked"
        }
    }
    ```
    """
    widget = lv.checkbox(lv.screen_active())
    if "options" in element:
        state = element["options"].get("state", "disabled")
        cb_state = getattr(lv.STATE, state.upper(), lv.STATE.DISABLED)
        widget.add_state(cb_state)
    else:
        widget.add_state(lv.STATE.DEFAULT)
    return widget

def create_dropdown(element) -> lv.dropdown:
    """
    **Params**
    - `element` The JSON element to create the dropdown widget from.

    **Returns**
    - `lv.dropdown` The created dropdown widget.

    Create a dropdown widget from a JSON element.

    **Example**
    ```json
    {
        "type": "dropdown",
        "options": {
            "entries": ["Option 1", "Option 2", "Option 3"]
        }
    }
    ```
    """
    widget = lv.dropdown(lv.screen_active())
    if "options" in element:
        entries = element["options"].get("entries", [])
        if len(entries) == 0:
            for i in range(random.randint(1, 10)):
                entries.append("".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
        widget.set_options("\n".join(entries))
    return widget

def create_image(element) -> lv.image:
    """
    **Params**
    - `element` The JSON element to create the image widget from.

    **Returns**
    - `lv.image` The created image widget.

    Create an image widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement image widget
    widget = lv.image(lv.screen_active())
    # widget.set_src(lv.SYMBOL.OK)
    return widget

def create_imagebutton(element) -> lv.imagebutton:
    """
    **Params**
    - `element` The JSON element to create the imagebutton widget from.

    **Returns**
    - `lv.imagebutton` The created imagebutton widget.

    Create an imagebutton widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement image_button widget
    widget = lv.imagebutton(lv.screen_active())
    return widget

def create_keyboard(element) -> lv.keyboard:
    """
    **Params**
    - `element` The JSON element to create the keyboard widget from.

    **Returns**
    - `lv.keyboard` The created keyboard widget.

    Create a keyboard widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement keyboard widget
    widget = lv.keyboard(lv.screen_active())
    return widget

def create_label(element) -> lv.label:
    """
    **Params**
    - `element` The JSON element to create the label widget from.

    **Returns**
    - `lv.label` The created label widget.

    Create a label widget from a JSON element.

    **Example**
    ```json
    {
        "type": "label",
        "options": {
            "text": "Hello, World!"
        }
    }
    ```
    """
    widget = lv.label(lv.screen_active())
    if "options" in element:
        text = element["options"].get("text", "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
    else:
        text = "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
    widget.set_text(text)
    return widget

def create_led(element) -> lv.led:
    """
    **Params**
    - `element` The JSON element to create the led widget from.

    **Returns**
    - `lv.led` The created led widget.

    Create an led widget from a JSON element. **(visually broken since we do nothing functional with it)**

    **Example**
    ```json
    {
        "type": "led",
        "options": {
            "brightness": 100
        }
    }
    ```
    """
    widget = lv.led(lv.screen_active())
    if "options" in element:
        brightness = element["options"].get("brightness", 100)
        widget.set_brightness(brightness)
    else:
        widget.set_brightness(random.randint(0, 100))
    return widget

def create_line(element) -> lv.line:
    """
    **Params**
    - `element` The JSON element to create the line widget from.

    **Returns**
    - `lv.line` The created line widget.

    Create a line widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement line widget (also tough to implement)
    widget = lv.line(lv.screen_active())
    # if "options" in element:
    #     points = element["options"].get("points", [])
    #     widget.set_points(points)
    return widget

def create_list(element) -> lv.list:
    """
    **Params**
    - `element` The JSON element to create the list widget from.

    **Returns**
    - `lv.list` The created list widget.

    Create a list widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement list widget
    widget = lv.list(lv.screen_active())
    return widget

def create_menu(element) -> lv.menu:
    """
    **Params**
    - `element` The JSON element to create the menu widget from.

    **Returns**
    - `lv.menu` The created menu widget.

    Create a menu widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement menu widget
    widget = lv.menu(lv.screen_active())
    return widget

def create_messagebox(element) -> lv.msgbox:
    """
    **Params**
    - `element` The JSON element to create the messagebox widget from.

    **Returns**
    - `lv.msgbox` The created messagebox widget.

    Create a messagebox widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement messagebox widget
    widget = lv.msgbox(lv.screen_active())
    return widget

def create_roller(element) -> lv.roller:
    """
    **Params**
    - `element` The JSON element to create the roller widget from.

    **Returns**
    - `lv.roller` The created roller widget.

    Create a roller widget from a JSON element.

    **Example**
    ```json
    {
        "type": "roller",
        "options": {
            "entries": ["Option 1", "Option 2", "Option 3"],
            "mode": "infinite",
            "visible_rows": 3
        }
    }
    ```
    """
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

def create_scale(element) -> lv.scale:
    """
    **Params**
    - `element` The JSON element to create the scale widget from.

    **Returns**
    - `lv.scale` The created scale widget.

    Create a scale widget from a JSON element.

    **Example**
    ```json
    {
        "type": "scale",
        "options": {
            "mode": "horizontal_bottom",
            "show_label": true,
            "total_ticks": 100,
            "major_ticks": 10,
            "major_range": 100,
            "minor_range": 10,
            "sections": 10,
            "labels": ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J"]
        }
    }
    ```
    """
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

def create_slider(element) -> lv.slider:
    """
    **Params**
    - `element` The JSON element to create the slider widget from.

    **Returns**
    - `lv.slider` The created slider widget.

    Create a slider widget from a JSON element.

    **Example**
    ```json
    {
        "type": "slider",
        "options": {
            "range_min": 0,
            "range_max": 100,
            "value": 50
        }
    }
    ```
    """
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

def create_spangroup(element) -> lv.spangroup:
    """
    **Params**
    - `element` The JSON element to create the spangroup widget from.

    **Returns**
    - `lv.spangroup` The created spangroup widget.

    Create a spangroup widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement span widget
    widget = lv.spangroup(lv.screen_active())
    return widget

def create_spinbox(element) -> lv.spinbox:
    """
    **Params**
    - `element` The JSON element to create the spinbox widget from.

    **Returns**
    - `lv.spinbox` The created spinbox widget.

    Create a spinbox widget from a JSON element.

    **Example**
    ```json
    {
        "type": "spinbox",
        "options": {
            "range_min": 0,
            "range_max": 100,
            "step": 1,
            "value": 50
        }
    }
    ```
    """
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

def create_spinner(element) -> lv.spinner:
    """
    **Params**
    - `element` The JSON element to create the spinner widget from.

    **Returns**
    - `lv.spinner` The created spinner widget.

    Create a spinner widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement spinner widget
    widget = lv.spinner(lv.screen_active())
    return widget

def create_switch(element) -> lv.switch:
    """
    **Params**
    - `element` The JSON element to create the switch widget from.

    **Returns**
    - `lv.switch` The created switch widget.

    Create a switch widget from a JSON element.

    **Example**
    ```json
    {
        "type": "switch",
        "options": {
            "state": "checked"
        }
    }
    ```
    """
    widget = lv.switch(lv.screen_active())
    if "options" in element:
        state = element["options"].get("state", 'default')
        sw_state = getattr(lv.STATE, state.upper(), lv.STATE.DEFAULT)
        widget.add_state(sw_state)
    else:
        widget.add_state(lv.STATE.DEFAULT)
    return widget

def create_table(element) -> lv.table:
    """
    **Params**
    - `element` The JSON element to create the table widget from.

    **Returns**
    - `lv.table` The created table widget.

    Create a table widget from a JSON element.

    **Example**
    ```json
    {
        "type": "table",
        "options": {
            "column_count": 3,
            "row_count": 3,
            "column_widths": [50, 100, 150],
            "cell_contents": [
                ["A1", "B1", "C1"],
                ["A2", "B2", "C2"],
                ["A3", "B3", "C3"]
            ]
        }
    }
    ```
    """
    widget = lv.table(lv.screen_active())
    if "options" in element:
        col_cnt = element["options"].get("column_count", 1)
        row_cnt = element["options"].get("row_count", 1)
        col_widths = element["options"].get("column_widths", [random.randint(10, 50) for _ in range(col_cnt)])
        cell_contents = element["options"].get("cell_contents", [[random.choice(ascii_letters) for _ in range(col_cnt)] for _ in range(row_cnt)])
        widget.set_column_count(col_cnt)
        widget.set_row_count(row_cnt)
        for i, width in enumerate(col_widths):
            widget.set_column_width(i, width)
        # Iterate over the array of arrays of string (cell_content) and set the cell value starting with row 0, col 0
        for i, row in enumerate(cell_contents):
            for j, content in enumerate(row):
                widget.set_cell_value(i, j, content)
    else:
        widget.set_column_count(random.randint(1, 3))
        widget.set_row_count(random.randint(1, 3))
    return widget

def create_tabview(element) -> lv.tabview:
    """
    **Params**
    - `element` The JSON element to create the tabview widget from.

    **Returns**
    - `lv.tabview` The created tabview widget.

    Create a tabview widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement tabview widget
    widget = lv.tabview(lv.screen_active())
    return widget

def create_textarea(element) -> lv.textarea:
    """
    **Params**
    - `element` The JSON element to create the textarea widget from.

    **Returns**
    - `lv.textarea` The created textarea widget.

    Create a textarea widget from a JSON element.

    **Example**
    ```json
    {
        "type": "textarea",
        "options": {
            "text": "Hello, World!"
        }
    }
    ```
    """
    widget = lv.textarea(lv.screen_active())
    if "options" in element:
        text = element["options"].get("text", " ".join([c for _ in range(random.randint(10, 100)) for c in ascii_letters]))
        widget.set_text(text)
    else:
        widget.set_text(" ".join([c for _ in range(random.randint(10, 100)) for c in ascii_letters]))
    return widget

def create_tileview(element) -> lv.tileview:
    """
    **Params**
    - `element` The JSON element to create the tileview widget from.

    **Returns**
    - `lv.tileview` The created tileview widget.

    Create a tileview widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement tileview widget
    widget = lv.tileview(lv.screen_active())
    return widget

def create_window(element) -> lv.win:
    """
    **Params**
    - `element` The JSON element to create the window widget from.

    **Returns**
    - `lv.win` The created window widget.

    Create a window widget from a JSON element. **(not implemented yet)**
    """
    # TODO Implement window widget
    widget = lv.win(lv.screen_active())
    return widget

widget_mapping = {
    "arc": create_arc,
    "bar": create_bar,
    "button": create_button,
    "buttonmatrix": create_buttonmatrix,
    "calendar": create_calendar,
    "canvas": create_canvas,
    "chart": create_chart,
    "checkbox": create_checkbox,
    "dropdown": create_dropdown,
    "image": create_image,
    "imagebutton": create_imagebutton,
    "keyboard": create_keyboard,
    "label": create_label,
    "led": create_led,
    "line": create_line,
    "list": create_list,
    "menu": create_menu,
    "messagebox": create_messagebox,
    "roller": create_roller,
    "scale": create_scale,
    "slider": create_slider,
    "spangroup": create_spangroup,
    "spinbox": create_spinbox,
    "spinner": create_spinner,
    "switch": create_switch,
    "table": create_table,
    "tabview": create_tabview,
    "textarea": create_textarea,
    "tileview": create_tileview,
    "window": create_window
}
"""A mapping of widget types to their respective creation methods"""