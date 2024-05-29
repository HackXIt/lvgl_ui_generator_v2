import mock

jpeg = mock.MagicMock()
"""
This is a mock object for the `jpeg` module.

This mock object is used to circumvent the `ImportError` that occurs when importing the unknown module in a non-MicroPython environment. (Like when generating documentation with `pdoc`)

The actual `jpeg` module is used to encode JPEG images for screenshots.

It is compiled from the [libjpeg source project](https://github.com/libjpeg-turbo/libjpeg-turbo) and linked to the micropython binary.

Further details about this can also be found in the [LVGL forum post where this was discussed](https://tinyurl.com/lvgl-jpeg-encode-forum-post).
"""
jpeg.encode = mock.MagicMock()