import cli
import screenshot
from random_ui import RandomUI

ui = None

def main():
    global ui
    args = cli.process_arguments()
    # display_driver.init()
    ui = RandomUI(args.width, args.height, args.widget_count, args.widget_types, args.output_file, args.layout)
    print(ui.width, ui.height, ui.widget_count, ui.widget_types, ui.output_file, ui.layout)
    ui.create_random_ui()
    screenshot.take_screenshot(ui.container, args.output_file)

if __name__ == "__main__":
    main()

# Create a button with a label

# scr = lv.obj()
# btn = lv.button(scr)
# btn.align(lv.ALIGN.CENTER, 0, 0)
# label = lv.label(btn)
# label.set_text('Hello World!')
# lv.screen_load(scr)

# # Test screenshot
# snapshot = None
# snapshot = lv.snapshot_take(scr, lv.COLOR_FORMAT.NATIVE)
# # Determine the size of the snapshot data
# data_size = snapshot.data_size

# # Read snapshot data into a buffer
# buffer = snapshot.data.__dereference__(data_size)

# # Save the snapshot data to a file
# with open('screenshot.raw', 'wb') as f:
#     f.write(buffer)
