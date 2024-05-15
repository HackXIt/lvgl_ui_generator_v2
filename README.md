# lvgl_ui_generator_v2

A project to generate a user interface using LVGL and capturing a screenshot alongside an annotation file with widget metadata (bounding box).

LVGL UI Generator version 2 is an updated version of the UI generator that uses micropython and corresponding LVGL bindings as a base. This version is more flexible, easier to use and more maintenable than the [original version](https://github.com/HackXIt/lvgl_ui_generator).

It has two modes of operation:
- **Random mode**: Generates a random UI with a specified number of widgets placed on a white background. It requires a provided list of widget types to randomly choose from.
- **Design mode**: Generates a UI based on a provided JSON design file. The design file describes the whole window, including styles, widgets and certain properties. There is a special `random` widget, which can be used to randomize widget creation in certain areas of the design. This mode is useful in creating more realistic looking user interfaces, as the random mode does not accomodate for styles regarding the containers.

# Usage

## TL;DR

## Random mode

### Layouts

## Design mode

### Design file specification

# Installation & Environment setup

## Dependencies

# Known issues

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.