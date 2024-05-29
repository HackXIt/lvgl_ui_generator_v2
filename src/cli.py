import argparse
import sys

def process_design_arguments(parser: argparse.ArgumentParser, print_help: bool = False):
    """
    **Params:**
    - `parser` The parser object to process the arguments with.
    - `print_help` A flag to determine if the help message for this mode should be printed. Default is False.

    **Returns:**
    - `args.Namespace` The parsed arguments for the design mode, including the initial general arguments.

    Process the arguments for the design mode subparser.
    """
    parser.add_argument('-f', '--file', required=True, type=str, help='path to JSON design file')
    if print_help:
        parser.usage(True)
        sys.exit(0)
    args = parser.parse_args()
    return args

def process_generator_arguments(parser: argparse.ArgumentParser, print_help: bool = False):
    """
    **Params:**
    - `parser` The parser object to process the arguments with.
    - `print_help` A flag to determine if the help message for this mode should be printed. Default is False.

    **Returns:**
    - `args.Namespace` The parsed arguments for the generator mode, including the initial general arguments.

    Process the arguments for the generator mode subparser.
    """
    parser.add_argument('-W', '--width', type=int, default=420, required=True, help='the width of the UI')
    parser.add_argument('-H', '--height', type=int, default=320, required=True, help='the height of the UI')
    parser.add_argument('-c', '--widget_count', type=int, default=1, required=True, help='the count of widgets')
    parser.add_argument('-t', '--widget_types', type=str, nargs='+', required=True, help='A list of widget types')
    parser.add_argument('-l', '--layout', type=str, required=True, help='the layout option')
    parser.add_argument('--random-state', action='store_true', help='Use a random state for each created widget (experimental)')
    if print_help:
        parser.usage(True)
        sys.exit(0)
    args = parser.parse_args()
    return args

def process_arguments():
    """
    **Returns:**
    - `args.Namespace` The parsed arguments for the UI generator.

    Process the arguments for the UI generator.
    """
    # Create the parser
    parser = argparse.ArgumentParser(description='Process CLI arguments for the UI generator.')
    parser.add_argument('-m', '--mode', type=str, help='the mode to run the program in')
    parser.add_argument('-?', '--usage', required=False, action='store_true', help='Print usage information for that mode.')
    parser.add_argument('-n', '--normalize', action='store_true', help='normalize the bounding boxes')
    parser.add_argument('-o', '--output_file', type=str, required=True, help='The output file (screenshot)')
    # NOTE Micropythons argparse is very limited and does not support groups, which is why this is a bit of a workaround
    args = parser.parse_known_args()[0] # NOTE Parse initially to determine mode and then parse again with the correct mode

    if args.mode == 'design':
        return process_design_arguments(parser, args.usage)
    elif args.mode == 'random':
        return process_generator_arguments(parser, args.usage)
    raise ValueError('Invalid mode argument provided. Please provide either "design" or "random" as the mode.')

if __name__ == "__main__":
    args = process_arguments()
    print(args)