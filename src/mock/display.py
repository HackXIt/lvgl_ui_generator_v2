import mock

driver = mock.MagicMock()
"""
This is a mock object for the `display_driver_utils` module.

This mock object is used to circumvent the `ImportError` that occurs when importing the unknown module in a non-MicroPython environment. (Like when generating documentation with `pdoc`)

The actual `display_driver_utils` module is used to create the screen for the LVGL UI Generator v2 project.

Further details about this can be viewed in the [official GitHub repository of `lv_micropython`](https://github.com/lvgl/lv_micropython).
"""