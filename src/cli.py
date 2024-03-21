import argparse

def process_arguments():
    # Create the parser
    parser = argparse.ArgumentParser(description='Process some integers.')

    # Add arguments
    parser.add_argument('-W', '--width', type=int, default=420, required=True, help='the width of the UI')
    parser.add_argument('-H', '--height', type=int, default=320, required=True, help='the height of the UI')
    parser.add_argument('-c', '--widget_count', type=int, default=1, required=True, help='the count of widgets')
    parser.add_argument('-t', '--widget_types', type=str, nargs='+', required=True, help='A list of widget types')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='the output file')
    parser.add_argument('-d', '--delay_count', type=int, help='screenshot delay')
    parser.add_argument('-l', '--layout', type=str, required=True, help='the layout option')
    parser.add_argument('-n', '--normalize', action='store_true', help='normalize the bounding boxes')

    # Parse the arguments
    args = parser.parse_args()

    # Perform any needed validation on the arguments
    # if args.width <= 0 or args.height <= 0 or args.widget_count <= 0 or not args.widget_types:
    #     parser.error('Invalid arguments')
    
    # Return the parsed arguments and widget types (if necessary)
    return args

if __name__ == "__main__":
    args = process_arguments()
    print(args)