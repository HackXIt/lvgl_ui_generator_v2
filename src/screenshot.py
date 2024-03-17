import lvgl as lv

def take_screenshot(container, output_file):
    snapshot = lv.snapshot_take(container, lv.COLOR_FORMAT.NATIVE)
    data_size = snapshot.data_size
    buffer = snapshot.data.__dereference__(data_size)
    with open(output_file, 'wb') as f:
        f.write(buffer)