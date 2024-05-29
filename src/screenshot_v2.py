import sys
if sys.implementation.name == "micropython":
    import jpeg
    import lvgl as lv
else:
    import mock
    from .mock.lvgl import lv
    from .mock.jpeg import jpeg

def bgr_to_rgb(data):
    """
    **Params**
    - `data` A flat bytearray in BGR format.

    Swap the BGR values to RGB in a flat bytearray.
    """
    # Assume data is a flat bytearray in BGR format
    for i in range(0, len(data), 3):
        data[i], data[i+2] = data[i+2], data[i]  # Swap the B and R values
    return data

def take_screenshot(output_file: str, quality:int = 100):
    """
    **Params**
    - `output_file` The file path to save the screenshot to.
    - `quality` The quality of the JPG image (0-100).

    Take a screenshot of a container using the LVGL snapshot API and save it to a JPG file.
    """
    disp = lv.display_get_default()
    width = disp.get_horizontal_resolution()
    height = disp.get_vertical_resolution()
    scrn = lv.screen_active()
    lv.timer_handler()
    snapshot = lv.snapshot_take(scrn, lv.COLOR_FORMAT.RGB888)
    print(f"Snapshot: {snapshot} ({type(snapshot)}, {snapshot.data_size} bytes)")
    data = snapshot.data.__dereference__(snapshot.data_size)
    # data = bgr_to_rgb(buffer)
    try:
        jpeg.encode(data, output_file, width, height, quality)
    except MemoryError as e:
        print(e)
    finally:
        snapshot.destroy()