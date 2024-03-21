import cli
from screenshot import take_screenshot
from yolo import write_yolo_normalized, write_yolo_pixel
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
    take_screenshot(ui.container, args.output_file)
    if args.normalize:
        write_yolo_normalized(ui, output_file=args.output_file.replace('.jpg', '.txt'), width=int(args.width), height=int(args.height))
    else:
        write_yolo_pixel(ui, output_file=args.output_file.replace('.jpg', '.txt'))

if __name__ == "__main__":
    main()