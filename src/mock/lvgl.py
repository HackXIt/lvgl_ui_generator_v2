import mock

lv = mock.MagicMock()
"""
This is a mock object for the `lvgl` module.

This mock object is used to circumvent the `ImportError` that occurs when importing the unknown module in a non-MicroPython environment. (Like when generating documentation with `pdoc`)

The actual `lvgl` module is used to create user interfaces with the unix port of [lv_micropython](https://github.com/lvgl/lv_micropython)

The `lv_micropython` project is a fork of the [MicroPython project](https://github.com/micropython/micropython) that includes the [bindings for LittlevGL](https://github.com/lvgl/lv_binding_micropython).

Further details about [LVGL] can be found in the [official documentation](https://docs.lvgl.io/master/) as well as [the official GitHub repository](https://github.com/lvgl/lvgl).
"""