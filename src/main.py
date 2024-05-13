import cli
from screenshot import take_screenshot
from yolo import write_yolo_normalized, write_yolo_pixel
from random_ui import RandomUI
from design_parser import UiLoader

ui = None
# WINDOW_WIDTH = 800
# WINDOW_HEIGHT = 800

def main():
    global ui
    args = cli.process_arguments()
    root_widget = None
    if args.mode == 'design':
        print('Design mode')
        loader = UiLoader(args.file)
        loader.initialize_screen()
        loader.parse_ui()
        ui = loader.get_ui()
        root_widget = loader.get_root_widget()
        ui["width"] = loader.width
        ui["height"] = loader.height
    elif args.mode == 'random':
        print('Random mode')
        random_state = args.random_state if args.random_state else False
        generator = RandomUI(args.width, args.height, args.widget_count, args.widget_types, args.output_file, args.layout, random_state)
        print(f"Width: {generator.width}, Height: {generator.height}, Widget Count: {generator.widget_count}, Widget Types: {generator.widget_types}, Output File: {generator.output_file}, Layout: {generator.layout}")
        generator.create_random_ui()
        ui = generator.get_ui()
        root_widget = generator.get_root_widget()
        ui["width"] = args.width
        ui["height"] = args.height
    if ui is None:
        raise ValueError('UI object is None')
    if root_widget is None:
        raise ValueError('Root widget is None')
    print("Taking screenshot...")
    take_screenshot(root_widget, args.output_file)
    if args.normalize:
        write_yolo_normalized(ui, output_file=args.output_file.replace('.jpg', '.txt'), width=ui['width'], height=ui['height'])
    else:
        write_yolo_pixel(ui, output_file=args.output_file.replace('.jpg', '.txt'))
    if args.mode == 'design':
        print('Design mode cleanup')
        loader.cleanup()
    elif args.mode == 'random':
        print('Random mode cleanup')
        generator.cleanup()

if __name__ == "__main__":
    main()