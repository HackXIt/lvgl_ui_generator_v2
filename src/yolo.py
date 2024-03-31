from random_ui import RandomUI
from design_parser import UiLoader
from ui import UI

def write_yolo_pixel(ui: UI, output_file: str):
    """
    This function writes the .txt file in the YOLO format using pixel values, with the widget's bounding boxes and class labels.
    """
    ui.verify_objects()
    with open(output_file, 'w') as f:
        for widget in ui['objects']:
            x, y, w, h = widget['x'], widget['y'], widget['width'], widget['height']
            f.write(f"{widget['class']} {x} {y} {w} {h}\n")

def write_yolo_normalized(ui: UI, output_file: str, width: int, height: int):
    """
    This function writes the .txt file in the YOLO format using normalized values, with the widget's bounding boxes and class labels.
    """
    ui.verify_objects()
    for widget in ui['objects']:
        widget['x'] /= width
        widget['y'] /= height
        widget['width'] /= width
        widget['height'] /= height
    with open(output_file, 'w') as f:
        for widget in ui['objects']:
            x, y, w, h = widget['x'], widget['y'], widget['width'], widget['height']
            f.write(f"{widget['class']} {x} {y} {w} {h}\n")
