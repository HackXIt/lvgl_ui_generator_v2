import argparse
import numpy as np
from PIL import Image

def parse_args():
    parser = argparse.ArgumentParser(description='Convert a binary RGB565 or RGB888 image file to a JPEG image.')
    parser.add_argument('-W', '--width', type=int, required=True, help='Width of the image.')
    parser.add_argument('-H', '--height', type=int, required=True, help='Height of the image.')
    parser.add_argument('-i', '--input', type=str, default='screenshot.bin', help='Input file name.')
    parser.add_argument('-o', '--output', type=str, default='screenshot.jpg', help='Output file name.')
    return parser.parse_args()

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

def main():
    args = parse_args()

    # Constants for image dimensions
    WIDTH, HEIGHT = args.width, args.height

    # Load the raw image data from the file
    with open(args.input, 'rb') as file:
        raw_data = file.read()

    # Determine whether the data is RGB565 or RGB888 based on its size
    expected_size_565 = WIDTH * HEIGHT * 2  # 2 bytes per pixel for RGB565
    expected_size_888 = WIDTH * HEIGHT * 3  # 3 bytes per pixel for RGB888

    if len(raw_data) == expected_size_565:
        print("Converting RGB565 to RGB888...")
        image_data_565 = np.frombuffer(raw_data, dtype=np.uint16).reshape((HEIGHT, WIDTH))
        rgb888_data = np.zeros((HEIGHT, WIDTH, 3), dtype=np.uint8)
        for y in range(HEIGHT):
            for x in range(WIDTH):
                rgb888_data[y, x] = rgb565_to_rgb888(image_data_565[y, x])
    elif len(raw_data) == expected_size_888:
        print("Assuming RGB888 and converting to JPEG...")
        bgr888_data = np.frombuffer(raw_data, dtype=np.uint8).reshape((HEIGHT, WIDTH, 3))
        rgb888_data = bgr888_data[..., ::-1]
    else:
        raise ValueError(f"The size ({len(raw_data)}) of the raw data does not match expected sizes for RGB565 ({expected_size_565}) or RGB888 ({expected_size_888}).")

    # Create the image using Pillow
    img = Image.fromarray(rgb888_data, 'RGB')

    # Save the image
    img.save(args.output)
    print(f"Conversion completed. Image saved as {args.output}.")

if __name__ == '__main__':
    main()
