import numpy as np
from PIL import Image

# Constants for image dimensions
WIDTH, HEIGHT = 420, 320

# Load the raw RGB565 data from the file
with open('screenshot.raw', 'rb') as file:
    raw_data = file.read()

# Convert raw RGB565 data to a NumPy array
image_data_565 = np.frombuffer(raw_data, dtype=np.uint16).reshape((HEIGHT, WIDTH))

# Function to convert RGB565 to RGB888
def rgb565_to_rgb888(rgb565):
    # Mask out the components
    r = (rgb565 & 0xF800) >> 11
    g = (rgb565 & 0x07E0) >> 5
    b = (rgb565 & 0x001F)
    
    # Convert the components to 8-bit values
    r = (r * 255) // 31
    g = (g * 255) // 63
    b = (b * 255) // 31
    return r, g, b

# Create an empty array for RGB888 data
rgb888_data = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)

# Convert RGB565 to RGB888
for y in range(HEIGHT):
    for x in range(WIDTH):
        # Get the pixel in RGB565 format
        rgb565_pixel = image_data_565[y, x]
        
        # Convert it to RGB888
        r, g, b = rgb565_to_rgb888(rgb565_pixel)
        
        # Place it in the new array
        rgb888_data[y, x] = [r, g, b]

# Create the image using Pillow
img = Image.fromarray(rgb888_data, 'RGB')

# Save the image
img.save('screenshot.jpg')
