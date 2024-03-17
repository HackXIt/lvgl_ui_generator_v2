import display_driver
import cli
import screenshot
import random_ui

def main():
    args = cli.process_arguments()
    display_driver.init()
    container = random_ui.create_random_ui(args)
    screenshot.take_screenshot(container, args.output_file)

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
