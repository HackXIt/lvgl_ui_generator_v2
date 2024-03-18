import cli
import screenshot
from random_ui import RandomUI

ui = None
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 800

def main():
    global ui
    args = cli.process_arguments()
    ui = RandomUI(args.width, args.height, args.widget_count, args.widget_types, args.output_file, args.layout)
    print(ui.width, ui.height, ui.widget_count, ui.widget_types, ui.output_file, ui.layout)
    ui.create_random_ui()
    screenshot.take_screenshot(ui.container, args.output_file)

if __name__ == "__main__":
    main()