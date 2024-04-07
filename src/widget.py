import lvgl as lv
import random
from global_definitions import ascii_letters

# NOTE ------------ WIDGET CREATION METHODS ------------
def create_arc(element) -> lv.arc:
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
    widget = lv.buttonmatrix(lv.screen_active())
    if "options" in element:
        map = element["options"].get("map", [random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
        widget.set_map(map)
    else:
        widget.set_map([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
    return widget

def create_calendar(element) -> lv.calendar:
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

def create_chart(element) -> lv.chart:
    # TODO Implement chart widget (also tough to implement)
    widget = lv.chart(lv.screen_active())
    return widget

def create_canvas(element) -> lv.canvas:
    # TODO Implement canvas widget
    widget = lv.canvas(lv.screen_active())
    return widget

def create_checkbox(element) -> lv.checkbox:
    widget = lv.checkbox(lv.screen_active())
    if "options" in element:
        state = element["options"].get("state", "disabled")
        cb_state = getattr(lv.STATE, state.upper(), lv.STATE.DISABLED)
        widget.add_state(cb_state)
    else:
        widget.add_state(lv.STATE.DEFAULT)
    return widget

def create_dropdown(element) -> lv.dropdown:
    widget = lv.dropdown(lv.screen_active())
    if "options" in element:
        entries = element["options"].get("entries", [])
        if len(entries) == 0:
            for i in range(random.randint(1, 10)):
                entries.append("".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
        widget.set_options("\n".join(entries))
    return widget

def create_image(element) -> lv.image:
    # TODO Implement image widget
    widget = lv.image(lv.screen_active())
    # widget.set_src(lv.SYMBOL.OK)
    return widget

def create_imagebutton(element) -> lv.imagebutton:
    # TODO Implement image_button widget
    widget = lv.imagebutton(lv.screen_active())
    return widget

def create_keyboard(element) -> lv.keyboard:
    # TODO Implement keyboard widget
    widget = lv.keyboard(lv.screen_active())
    return widget

def create_label(element) -> lv.label:
    widget = lv.label(lv.screen_active())
    if "options" in element:
        text = element["options"].get("text", "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))]))
    else:
        text = "".join([random.choice(ascii_letters) for _ in range(random.randint(1, 10))])
    widget.set_text(text)
    return widget

def create_led(element) -> lv.led:
    widget = lv.led(lv.screen_active())
    if "options" in element:
        brightness = element["options"].get("brightness", 100)
        widget.set_brightness(brightness)
    else:
        widget.set_brightness(random.randint(0, 100))
    return widget

def create_line(element) -> lv.line:
    # TODO Implement line widget (also tough to implement)
    widget = lv.line(lv.screen_active())
    # if "options" in element:
    #     points = element["options"].get("points", [])
    #     widget.set_points(points)
    return widget

def create_list(element) -> lv.list:
    # TODO Implement list widget
    widget = lv.list(lv.screen_active())
    return widget

def create_menu(element) -> lv.menu:
    # TODO Implement menu widget
    widget = lv.menu(lv.screen_active())
    return widget

def create_messagebox(element) -> lv.msgbox:
    # TODO Implement messagebox widget
    widget = lv.msgbox(lv.screen_active())
    return widget

def create_roller(element) -> lv.roller:
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
    # TODO Implement span widget
    widget = lv.spangroup(lv.screen_active())
    return widget

def create_spinbox(element) -> lv.spinbox:
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
    # TODO Implement spinner widget
    widget = lv.spinner(lv.screen_active())
    return widget

def create_switch(element) -> lv.switch:
    widget = lv.switch(lv.screen_active())
    if "options" in element:
        state = element["options"].get("state", False)
        sw_state = getattr(lv.STATE, state.upper(), lv.STATE.DISABLED)
        widget.add_state(sw_state)
    else:
        widget.add_state(lv.STATE.DEFAULT)
    return widget

def create_table(element) -> lv.table:
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

def create_tabview(element) -> lv.tabview:
    # TODO Implement tabview widget
    widget = lv.tabview(lv.screen_active())
    return widget

def create_textarea(element) -> lv.textarea:
    widget = lv.textarea(lv.screen_active())
    if "options" in element:
        text = element["options"].get("text", str([c for _ in range(random.randint(10, 100)) for c in ascii_letters]))
        widget.set_text(text)
    else:
        widget.set_text(str([c for _ in range(random.randint(10, 100)) for c in ascii_letters]))
    return widget

def create_tileview(element) -> lv.tileview:
    # TODO Implement tileview widget
    widget = lv.tileview(lv.screen_active())
    return widget

def create_window(element) -> lv.win:
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