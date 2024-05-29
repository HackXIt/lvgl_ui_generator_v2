pdoc = {}

pdoc['write_yolo_pixel'] = """
**Params:**
- `ui` The UI object.
- `output_file` The file path to save the YOLO .txt file to.

This function writes the .txt file in the YOLO format using pixel values, with the widget's bounding boxes and class labels.
"""
pdoc['write_yolo_normalized'] = """
**Params:**
- `ui` The UI object.
- `output_file` The file path to save the YOLO .txt file to.

This function writes the .txt file in the YOLO format using normalized values, with the widget's bounding boxes and class labels.
"""

import sys
if sys.implementation.name == "micropython":
    from ui import UI
else:
    from .ui import UI

def write_yolo_pixel(ui: UI, output_file: str):
    """
    **Params:**
    - `ui` The UI object.
    - `output_file` The file path to save the YOLO .txt file to.

    This function writes the .txt file in the YOLO format using pixel values, with the widget's bounding boxes and class labels.
    """
    ui.verify_objects()
    with open(output_file, 'w') as f:
        for widget in ui['objects']:
            x, y, w, h = widget['x'], widget['y'], widget['width'], widget['height']
            f.write(f"{widget['class']} {x} {y} {w} {h}\n")

def write_yolo_normalized(ui: UI, output_file: str, width: int, height: int):
    """
    **Params:**
    - `ui` The UI object.
    - `output_file` The file path to save the YOLO .txt file to.

    This function writes the .txt file in the YOLO format using normalized values, with the widget's bounding boxes and class labels.
    """
    ui.verify_objects()
    for widget in ui['objects']:
        print(f"X: {widget['x']} ({type(widget['x'])}), Y: {widget['y']} ({type(widget['y'])}), Width: {widget['width']} ({type(widget['width'])}), Height: {widget['height']} ({type(widget['height'])})")
        widget['x'] = float(widget['x']) / float(width)
        widget['y'] = float(widget['y']) / float(height)
        widget['width'] = float(widget['width']) / float(width)
        widget['height'] = float(widget['height']) / float(height)
    with open(output_file, 'w') as f:
        for widget in ui['objects']:
            x, y, w, h = widget['x'], widget['y'], widget['width'], widget['height']
            f.write(f"{widget['class']} {x} {y} {w} {h}\n")
