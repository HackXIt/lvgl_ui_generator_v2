# LVGL UI Generator v2

A project to generate a user interface using LVGL and capturing a screenshot alongside an annotation file with widget metadata (bounding box).

LVGL UI Generator version 2 is an updated version of the UI generator that uses micropython and corresponding LVGL bindings as a base. This version is more flexible, easier to use and more maintenable than the [original version](https://github.com/HackXIt/lvgl_ui_generator).

It has two modes of operation:
- **Random mode**: Generates a random UI with a specified number of widgets placed on a white background. It requires a provided list of widget types to randomly choose from.
- **Design mode**: Generates a UI based on a provided JSON design file. The design file describes the whole window, including styles, widgets and certain properties. There is a special `random` widget, which can be used to randomize widget creation in certain areas of the design. This mode is useful in creating more realistic looking user interfaces, as the random mode does not accomodate for styles regarding the containers.

# Prerequisites & Installation

In order to run the UI generator, you need to compile the micropython binary with the LVGL bindings. To make this process easier, the project has a `tasks.py` file, which already contains necessary routines via the usage of [`invoke`](https://www.pyinvoke.org/).

To use the [`invoke`](https://www.pyinvoke.org/) package, you will need to setup a virtual environment and install the dependencies using the provided [poetry project file (`pyproject.toml`)](pyproject.toml).

Since `lv_micropython` is included as a submodule, you will need to initialize the submodules **before** running the build task. 

⚠️ **Be aware, that initializing this submodule can take quite a while to complete, due to all the additional source dependencies being downloaded.** _(including unnecessary sources for various MCUs, ports and architectures)_

As of yet, there is no way to speed this up, but it is generally a one-time operation.

## Initializing the micropython submodule

Run the following command to initialize the submodule:

```shell
git submodule update --init --recursive
```

Make sure to grab a cup of coffee or tea ☕, as this operation can take quite a while to complete.

## Setting up the virtual environment

1. Install `poetry` package manager. See corresponding [documentation](https://python-poetry.org/docs/#installation) for more information.
2. Run `poetry install` to install the dependencies.

## Compiling the micropython binary

Run `poetry run invoke build` to compile the micropython binary with the LVGL bindings, using the provided `lv_conf.h` file.

<details>
<summary>Example build output</summary>

```shell
$ poetry run inv build
make: Entering directory '/home/rini-debian/git-stash/lvgl-ui-detector/lvgl_ui_generator_v2/lv_micropython/mpy-cross'
Use make V=1 or set BUILD_VERBOSE in your environment to increase build verbosity.
GEN build/genhdr/mpversion.h
CC ../py/modsys.c
CC main.c
LINK build/mpy-cross
   text    data     bss     dec     hex filename
 305806   13856     856  320518   4e406 build/mpy-cross
make: Leaving directory '/home/rini-debian/git-stash/lvgl-ui-detector/lvgl_ui_generator_v2/lv_micropython/mpy-cross'
make: Entering directory '/home/rini-debian/git-stash/lvgl-ui-detector/lvgl_ui_generator_v2/lv_micropython/ports/unix'
Use make V=1 or set BUILD_VERBOSE in your environment to increase build verbosity.
Updating submodules: lib/mbedtls lib/berkeley-db-1.xx lib/micropython-lib
Synchronizing submodule url for '../../lib/berkeley-db-1.xx'
Synchronizing submodule url for '../../lib/mbedtls'
Synchronizing submodule url for '../../lib/micropython-lib'
make: Leaving directory '/home/rini-debian/git-stash/lvgl-ui-detector/lvgl_ui_generator_v2/lv_micropython/ports/unix'
make: Entering directory '/home/rini-debian/git-stash/lvgl-ui-detector/lvgl_ui_generator_v2/lv_micropython/ports/unix'
Use make V=1 or set BUILD_VERBOSE in your environment to increase build verbosity.
LVGL-GEN build-standard/lvgl/lv_mpy.c
GEN build-standard/genhdr/mpversion.h
GEN build-standard/genhdr/qstr.i.last
GEN build-standard/genhdr/qstr.split
GEN build-standard/genhdr/moduledefs.split
GEN build-standard/genhdr/root_pointers.split
GEN build-standard/genhdr/compressed.split
GEN build-standard/genhdr/root_pointers.collected
GEN build-standard/genhdr/qstrdefs.collected.h
GEN build-standard/genhdr/moduledefs.collected
Root pointer registrations not updated
GEN build-standard/genhdr/compressed.collected
Module registrations not updated
QSTR not updated
Compressed data not updated
CC ../../py/modsys.c
CC ../../extmod/moduplatform.c
CC build-standard/lvgl/lv_mpy.c
CC ../../lib/lv_bindings/lvgl/src/drivers/evdev/lv_evdev.c
CC ../../lib/lv_bindings/lvgl/src/drivers/windows/lv_windows_input.c
CC ../../lib/lv_bindings/lvgl/src/drivers/windows/lv_windows_display.c
CC ../../lib/lv_bindings/lvgl/src/drivers/windows/lv_windows_context.c
CC ../../lib/lv_bindings/lvgl/src/drivers/display/st7735/lv_st7735.c
CC ../../lib/lv_bindings/lvgl/src/drivers/display/fb/lv_linux_fbdev.c
CC ../../lib/lv_bindings/lvgl/src/drivers/display/ili9341/lv_ili9341.c
CC ../../lib/lv_bindings/lvgl/src/drivers/display/drm/lv_linux_drm.c
CC ../../lib/lv_bindings/lvgl/src/drivers/display/st7796/lv_st7796.c
CC ../../lib/lv_bindings/lvgl/src/drivers/display/st7789/lv_st7789.c
CC ../../lib/lv_bindings/lvgl/src/drivers/display/lcd/lv_lcd_generic_mipi.c
CC ../../lib/lv_bindings/lvgl/src/drivers/nuttx/lv_nuttx_lcd.c
CC ../../lib/lv_bindings/lvgl/src/drivers/nuttx/lv_nuttx_libuv.c
CC ../../lib/lv_bindings/lvgl/src/drivers/nuttx/lv_nuttx_fbdev.c
CC ../../lib/lv_bindings/lvgl/src/drivers/nuttx/lv_nuttx_entry.c
CC ../../lib/lv_bindings/lvgl/src/drivers/nuttx/lv_nuttx_profiler.c
CC ../../lib/lv_bindings/lvgl/src/drivers/nuttx/lv_nuttx_touchscreen.c
CC ../../lib/lv_bindings/lvgl/src/drivers/nuttx/lv_nuttx_cache.c
CC ../../lib/lv_bindings/lvgl/src/drivers/x11/lv_x11_display.c
CC ../../lib/lv_bindings/lvgl/src/drivers/x11/lv_x11_input.c
CC ../../lib/lv_bindings/lvgl/src/drivers/sdl/lv_sdl_window.c
CC ../../lib/lv_bindings/lvgl/src/drivers/sdl/lv_sdl_mouse.c
CC ../../lib/lv_bindings/lvgl/src/drivers/sdl/lv_sdl_keyboard.c
CC ../../lib/lv_bindings/lvgl/src/drivers/sdl/lv_sdl_mousewheel.c
CC ../../lib/lv_bindings/lvgl/src/themes/default/lv_theme_default.c
CC ../../lib/lv_bindings/lvgl/src/themes/lv_theme.c
CC ../../lib/lv_bindings/lvgl/src/themes/simple/lv_theme_simple.c
CC ../../lib/lv_bindings/lvgl/src/themes/mono/lv_theme_mono.c
CC ../../lib/lv_bindings/lvgl/src/tick/lv_tick.c
CC ../../lib/lv_bindings/lvgl/src/lv_init.c
CC ../../lib/lv_bindings/lvgl/src/osal/lv_pthread.c
CC ../../lib/lv_bindings/lvgl/src/osal/lv_cmsis_rtos2.c
CC ../../lib/lv_bindings/lvgl/src/osal/lv_windows.c
CC ../../lib/lv_bindings/lvgl/src/osal/lv_os_none.c
CC ../../lib/lv_bindings/lvgl/src/osal/lv_rtthread.c
CC ../../lib/lv_bindings/lvgl/src/osal/lv_freertos.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_class.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_id_builtin.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_scroll.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_style.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_event.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_refr.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_group.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_pos.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_style_gen.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_tree.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_property.c
CC ../../lib/lv_bindings/lvgl/src/core/lv_obj_draw.c
CC ../../lib/lv_bindings/lvgl/src/others/sysmon/lv_sysmon.c
CC ../../lib/lv_bindings/lvgl/src/others/imgfont/lv_imgfont.c
CC ../../lib/lv_bindings/lvgl/src/others/file_explorer/lv_file_explorer.c
CC ../../lib/lv_bindings/lvgl/src/others/observer/lv_observer.c
CC ../../lib/lv_bindings/lvgl/src/others/snapshot/lv_snapshot.c
CC ../../lib/lv_bindings/lvgl/src/others/monkey/lv_monkey.c
CC ../../lib/lv_bindings/lvgl/src/others/fragment/lv_fragment.c
CC ../../lib/lv_bindings/lvgl/src/others/fragment/lv_fragment_manager.c
CC ../../lib/lv_bindings/lvgl/src/others/gridnav/lv_gridnav.c
CC ../../lib/lv_bindings/lvgl/src/others/ime/lv_ime_pinyin.c
CC ../../lib/lv_bindings/lvgl/src/others/vg_lite_tvg/vg_lite_matrix.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/rtthread/lv_string_rtthread.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/rtthread/lv_sprintf_rtthread.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/rtthread/lv_mem_core_rtthread.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/lv_mem.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/clib/lv_string_clib.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/clib/lv_mem_core_clib.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/clib/lv_sprintf_clib.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/micropython/lv_mem_core_micropython.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/builtin/lv_sprintf_builtin.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/builtin/lv_tlsf.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/builtin/lv_mem_core_builtin.c
CC ../../lib/lv_bindings/lvgl/src/stdlib/builtin/lv_string_builtin.c
CC ../../lib/lv_bindings/lvgl/src/misc/cache/lv_cache_entry.c
CC ../../lib/lv_bindings/lvgl/src/misc/cache/lv_image_cache.c
CC ../../lib/lv_bindings/lvgl/src/misc/cache/_lv_cache_lru_rb.c
CC ../../lib/lv_bindings/lvgl/src/misc/cache/lv_cache.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_profiler_builtin.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_color_op.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_color.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_text.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_bidi.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_style_gen.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_async.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_palette.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_style.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_text_ap.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_array.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_lru.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_anim.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_rb.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_math.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_fs.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_timer.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_log.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_event.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_ll.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_area.c
CC ../../lib/lv_bindings/lvgl/src/misc/lv_anim_timeline.c
CC ../../lib/lv_bindings/lvgl/src/layouts/flex/lv_flex.c
CC ../../lib/lv_bindings/lvgl/src/layouts/grid/lv_grid.c
CC ../../lib/lv_bindings/lvgl/src/layouts/lv_layout.c
CC ../../lib/lv_bindings/lvgl/src/libs/fsdrv/lv_fs_stdio.c
CC ../../lib/lv_bindings/lvgl/src/libs/fsdrv/lv_fs_memfs.c
CC ../../lib/lv_bindings/lvgl/src/libs/fsdrv/lv_fs_fatfs.c
CC ../../lib/lv_bindings/lvgl/src/libs/fsdrv/lv_fs_posix.c
CC ../../lib/lv_bindings/lvgl/src/libs/fsdrv/lv_fs_win32.c
CC ../../lib/lv_bindings/lvgl/src/libs/bin_decoder/lv_bin_decoder.c
CC ../../lib/lv_bindings/lvgl/src/libs/rlottie/lv_rlottie.c
CC ../../lib/lv_bindings/lvgl/src/libs/libpng/lv_libpng.c
CC ../../lib/lv_bindings/lvgl/src/libs/tiny_ttf/lv_tiny_ttf.c
CC ../../lib/lv_bindings/lvgl/src/libs/barcode/code128.c
CC ../../lib/lv_bindings/lvgl/src/libs/barcode/lv_barcode.c
CC ../../lib/lv_bindings/lvgl/src/libs/rle/lv_rle.c
CC ../../lib/lv_bindings/lvgl/src/libs/lz4/lz4.c
CC ../../lib/lv_bindings/lvgl/src/libs/bmp/lv_bmp.c
CC ../../lib/lv_bindings/lvgl/src/libs/lodepng/lv_lodepng.c
CC ../../lib/lv_bindings/lvgl/src/libs/lodepng/lodepng.c
CC ../../lib/lv_bindings/lvgl/src/libs/tjpgd/lv_tjpgd.c
CC ../../lib/lv_bindings/lvgl/src/libs/gif/gifdec.c
CC ../../lib/lv_bindings/lvgl/src/libs/gif/lv_gif.c
CC ../../lib/lv_bindings/lvgl/src/libs/qrcode/qrcodegen.c
CC ../../lib/lv_bindings/lvgl/src/libs/qrcode/lv_qrcode.c
CC ../../lib/lv_bindings/lvgl/src/libs/freetype/lv_freetype_glyph.c
CC ../../lib/lv_bindings/lvgl/src/libs/freetype/lv_freetype_image.c
CC ../../lib/lv_bindings/lvgl/src/libs/freetype/lv_ftsystem.c
CC ../../lib/lv_bindings/lvgl/src/libs/freetype/lv_freetype_outline.c
CC ../../lib/lv_bindings/lvgl/src/libs/freetype/lv_freetype.c
CC ../../lib/lv_bindings/lvgl/src/libs/libjpeg_turbo/lv_libjpeg_turbo.c
CC ../../lib/lv_bindings/lvgl/src/libs/ffmpeg/lv_ffmpeg.c
CC ../../lib/lv_bindings/lvgl/src/display/lv_display.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_8.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_20.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_30.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_44.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_18.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_unscii_8.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_simsun_16_cjk.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_38.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_22.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_fmt_txt.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_32.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_dejavu_16_persian_hebrew.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_binfont_loader.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_28.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_42.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_unscii_16.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_28_compressed.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_36.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_40.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_26.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_34.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_16.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_24.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_48.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_46.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_12.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_14.c
CC ../../lib/lv_bindings/lvgl/src/font/lv_font_montserrat_10.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_image.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_triangle.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_line.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_label.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_mask_rect.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_box_shadow.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_gradient.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_mask.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_triangle.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_transform.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_letter.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/blend/lv_draw_sw_blend_to_argb8888.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/blend/lv_draw_sw_blend.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/blend/lv_draw_sw_blend_to_rgb888.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/blend/lv_draw_sw_blend_to_rgb565.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_arc.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_vector.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_border.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_fill.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_line.c
CC ../../lib/lv_bindings/lvgl/src/draw/sw/lv_draw_sw_img.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_image_decoder.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_vector.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_rect.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_arc.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_line.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_border.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_arc.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_label.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_fill.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_triangle.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_mask_rectangle.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_utils.c
CC ../../lib/lv_bindings/lvgl/src/draw/renesas/dave2d/lv_draw_dave2d_image.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_mask.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_draw_pxp_img.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_draw_pxp_layer.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_pxp_osa.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_pxp_cfg.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_draw_buf_pxp.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_draw_pxp.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_draw_pxp_fill.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/pxp/lv_pxp_utils.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_fill.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_vglite_path.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_border.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_buf_vglite.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_img.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_layer.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_line.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_arc.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_vglite_utils.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_vglite_matrix.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_vglite_buf.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_triangle.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite.c
CC ../../lib/lv_bindings/lvgl/src/draw/nxp/vglite/lv_draw_vglite_label.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw_buf.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_image_buf.c
CC ../../lib/lv_bindings/lvgl/src/draw/sdl/lv_draw_sdl.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_vg_lite_utils.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_mask_rect.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_arc.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_layer.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_border.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_buf_vg_lite.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_img.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_vg_lite_path.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_line.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_label.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_vg_lite_decoder.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_box_shadow.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_fill.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_vector.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_draw_vg_lite_triangle.c
CC ../../lib/lv_bindings/lvgl/src/draw/vg_lite/lv_vg_lite_math.c
CC ../../lib/lv_bindings/lvgl/src/draw/lv_draw.c
CC ../../lib/lv_bindings/lvgl/src/indev/lv_indev.c
CC ../../lib/lv_bindings/lvgl/src/indev/lv_indev_scroll.c
CC ../../lib/lv_bindings/lvgl/src/widgets/dropdown/lv_dropdown.c
CC ../../lib/lv_bindings/lvgl/src/widgets/arc/lv_arc.c
CC ../../lib/lv_bindings/lvgl/src/widgets/keyboard/lv_keyboard.c
CC ../../lib/lv_bindings/lvgl/src/widgets/line/lv_line.c
CC ../../lib/lv_bindings/lvgl/src/widgets/scale/lv_scale.c
CC ../../lib/lv_bindings/lvgl/src/widgets/switch/lv_switch.c
CC ../../lib/lv_bindings/lvgl/src/widgets/animimage/lv_animimage.c
CC ../../lib/lv_bindings/lvgl/src/widgets/slider/lv_slider.c
CC ../../lib/lv_bindings/lvgl/src/widgets/canvas/lv_canvas.c
CC ../../lib/lv_bindings/lvgl/src/widgets/button/lv_button.c
CC ../../lib/lv_bindings/lvgl/src/widgets/checkbox/lv_checkbox.c
CC ../../lib/lv_bindings/lvgl/src/widgets/span/lv_span.c
CC ../../lib/lv_bindings/lvgl/src/widgets/spinner/lv_spinner.c
CC ../../lib/lv_bindings/lvgl/src/widgets/imagebutton/lv_imagebutton.c
CC ../../lib/lv_bindings/lvgl/src/widgets/roller/lv_roller.c
CC ../../lib/lv_bindings/lvgl/src/widgets/tabview/lv_tabview.c
CC ../../lib/lv_bindings/lvgl/src/widgets/label/lv_label.c
CC ../../lib/lv_bindings/lvgl/src/widgets/menu/lv_menu.c
CC ../../lib/lv_bindings/lvgl/src/widgets/textarea/lv_textarea.c
CC ../../lib/lv_bindings/lvgl/src/widgets/tileview/lv_tileview.c
CC ../../lib/lv_bindings/lvgl/src/widgets/image/lv_image.c
CC ../../lib/lv_bindings/lvgl/src/widgets/bar/lv_bar.c
CC ../../lib/lv_bindings/lvgl/src/widgets/buttonmatrix/lv_buttonmatrix.c
CC ../../lib/lv_bindings/lvgl/src/widgets/chart/lv_chart.c
CC ../../lib/lv_bindings/lvgl/src/widgets/msgbox/lv_msgbox.c
CC ../../lib/lv_bindings/lvgl/src/widgets/list/lv_list.c
CC ../../lib/lv_bindings/lvgl/src/widgets/spinbox/lv_spinbox.c
CC ../../lib/lv_bindings/lvgl/src/widgets/win/lv_win.c
CC ../../lib/lv_bindings/lvgl/src/widgets/calendar/lv_calendar_header_arrow.c
CC ../../lib/lv_bindings/lvgl/src/widgets/calendar/lv_calendar_header_dropdown.c
CC ../../lib/lv_bindings/lvgl/src/widgets/calendar/lv_calendar.c
CC ../../lib/lv_bindings/lvgl/src/widgets/led/lv_led.c
CC ../../lib/lv_bindings/lvgl/src/widgets/table/lv_table.c
CC ../../lib/lv_bindings/lvgl/examples/anim/lv_example_anim_2.c
CC ../../lib/lv_bindings/lvgl/examples/anim/lv_example_anim_1.c
CC ../../lib/lv_bindings/lvgl/examples/anim/lv_example_anim_timeline_1.c
CC ../../lib/lv_bindings/lvgl/examples/anim/lv_example_anim_3.c
CC ../../lib/lv_bindings/lvgl/examples/others/imgfont/lv_example_imgfont_1.c
CC ../../lib/lv_bindings/lvgl/examples/others/file_explorer/lv_example_file_explorer_3.c
CC ../../lib/lv_bindings/lvgl/examples/others/file_explorer/lv_example_file_explorer_1.c
CC ../../lib/lv_bindings/lvgl/examples/others/file_explorer/lv_example_file_explorer_2.c
CC ../../lib/lv_bindings/lvgl/examples/others/observer/lv_example_observer_2.c
CC ../../lib/lv_bindings/lvgl/examples/others/observer/lv_example_observer_5.c
CC ../../lib/lv_bindings/lvgl/examples/others/observer/lv_example_observer_3.c
CC ../../lib/lv_bindings/lvgl/examples/others/observer/lv_example_observer_4.c
CC ../../lib/lv_bindings/lvgl/examples/others/observer/lv_example_observer_6.c
CC ../../lib/lv_bindings/lvgl/examples/others/observer/lv_example_observer_1.c
CC ../../lib/lv_bindings/lvgl/examples/others/snapshot/lv_example_snapshot_1.c
CC ../../lib/lv_bindings/lvgl/examples/others/monkey/lv_example_monkey_1.c
CC ../../lib/lv_bindings/lvgl/examples/others/monkey/lv_example_monkey_2.c
CC ../../lib/lv_bindings/lvgl/examples/others/monkey/lv_example_monkey_3.c
CC ../../lib/lv_bindings/lvgl/examples/others/fragment/lv_example_fragment_1.c
CC ../../lib/lv_bindings/lvgl/examples/others/fragment/lv_example_fragment_2.c
CC ../../lib/lv_bindings/lvgl/examples/others/gridnav/lv_example_gridnav_1.c
CC ../../lib/lv_bindings/lvgl/examples/others/gridnav/lv_example_gridnav_4.c
CC ../../lib/lv_bindings/lvgl/examples/others/gridnav/lv_example_gridnav_3.c
CC ../../lib/lv_bindings/lvgl/examples/others/gridnav/lv_example_gridnav_2.c
CC ../../lib/lv_bindings/lvgl/examples/others/ime/lv_example_ime_pinyin_2.c
CC ../../lib/lv_bindings/lvgl/examples/others/ime/lv_example_ime_pinyin_1.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_8.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_11.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_9.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_1.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_13.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_5.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_3.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_6.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_12.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_10.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_14.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_15.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_7.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_2.c
CC ../../lib/lv_bindings/lvgl/examples/styles/lv_example_style_4.c
CC ../../lib/lv_bindings/lvgl/examples/assets/img_star.c
CC ../../lib/lv_bindings/lvgl/examples/assets/imgbtn_mid.c
CC ../../lib/lv_bindings/lvgl/examples/assets/img_hand.c
CC ../../lib/lv_bindings/lvgl/examples/assets/img_caret_down.c
CC ../../lib/lv_bindings/lvgl/examples/assets/animimg002.c
CC ../../lib/lv_bindings/lvgl/examples/assets/img_skew_strip.c
CC ../../lib/lv_bindings/lvgl/examples/assets/img_cogwheel_rgb.c
CC ../../lib/lv_bindings/lvgl/examples/assets/animimg001.c
CC ../../lib/lv_bindings/lvgl/examples/assets/imgbtn_right.c
CC ../../lib/lv_bindings/lvgl/examples/assets/animimg003.c
CC ../../lib/lv_bindings/lvgl/examples/assets/imgbtn_left.c
CC ../../lib/lv_bindings/lvgl/examples/assets/emoji/img_emoji_F617.c
CC ../../lib/lv_bindings/lvgl/examples/assets/img_cogwheel_indexed16.c
CC ../../lib/lv_bindings/lvgl/examples/assets/img_cogwheel_argb.c
CC ../../lib/lv_bindings/lvgl/examples/scroll/lv_example_scroll_2.c
CC ../../lib/lv_bindings/lvgl/examples/scroll/lv_example_scroll_4.c
CC ../../lib/lv_bindings/lvgl/examples/scroll/lv_example_scroll_3.c
CC ../../lib/lv_bindings/lvgl/examples/scroll/lv_example_scroll_6.c
CC ../../lib/lv_bindings/lvgl/examples/scroll/lv_example_scroll_1.c
CC ../../lib/lv_bindings/lvgl/examples/scroll/lv_example_scroll_5.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/flex/lv_example_flex_3.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/flex/lv_example_flex_1.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/flex/lv_example_flex_4.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/flex/lv_example_flex_2.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/flex/lv_example_flex_6.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/flex/lv_example_flex_5.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/grid/lv_example_grid_5.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/grid/lv_example_grid_2.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/grid/lv_example_grid_1.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/grid/lv_example_grid_4.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/grid/lv_example_grid_6.c
CC ../../lib/lv_bindings/lvgl/examples/layouts/grid/lv_example_grid_3.c
CC ../../lib/lv_bindings/lvgl/examples/libs/rlottie/lv_example_rlottie_2.c
CC ../../lib/lv_bindings/lvgl/examples/libs/rlottie/lv_example_rlottie_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/rlottie/lv_example_rlottie_approve.c
CC ../../lib/lv_bindings/lvgl/examples/libs/libpng/lv_example_libpng_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/tiny_ttf/lv_example_tiny_ttf_3.c
CC ../../lib/lv_bindings/lvgl/examples/libs/tiny_ttf/lv_example_tiny_ttf_2.c
CC ../../lib/lv_bindings/lvgl/examples/libs/tiny_ttf/ubuntu_font.c
CC ../../lib/lv_bindings/lvgl/examples/libs/tiny_ttf/lv_example_tiny_ttf_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/barcode/lv_example_barcode_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/bmp/lv_example_bmp_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/lodepng/lv_example_lodepng_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/lodepng/img_wink_png.c
CC ../../lib/lv_bindings/lvgl/examples/libs/tjpgd/lv_example_tjpgd_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/gif/img_bulb_gif.c
CC ../../lib/lv_bindings/lvgl/examples/libs/gif/lv_example_gif_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/qrcode/lv_example_qrcode_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/freetype/lv_example_freetype_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/libjpeg_turbo/lv_example_libjpeg_turbo_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/ffmpeg/lv_example_ffmpeg_1.c
CC ../../lib/lv_bindings/lvgl/examples/libs/ffmpeg/lv_example_ffmpeg_2.c
CC ../../lib/lv_bindings/lvgl/examples/get_started/lv_example_get_started_1.c
CC ../../lib/lv_bindings/lvgl/examples/get_started/lv_example_get_started_3.c
CC ../../lib/lv_bindings/lvgl/examples/get_started/lv_example_get_started_4.c
CC ../../lib/lv_bindings/lvgl/examples/get_started/lv_example_get_started_2.c
CC ../../lib/lv_bindings/lvgl/examples/event/lv_example_event_1.c
CC ../../lib/lv_bindings/lvgl/examples/event/lv_example_event_2.c
CC ../../lib/lv_bindings/lvgl/examples/event/lv_example_event_4.c
CC ../../lib/lv_bindings/lvgl/examples/event/lv_example_event_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/dropdown/lv_example_dropdown_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/dropdown/lv_example_dropdown_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/dropdown/lv_example_dropdown_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/arc/lv_example_arc_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/arc/lv_example_arc_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/keyboard/lv_example_keyboard_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/keyboard/lv_example_keyboard_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/line/lv_example_line_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/scale/lv_example_scale_5.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/scale/lv_example_scale_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/scale/lv_example_scale_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/scale/lv_example_scale_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/scale/lv_example_scale_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/switch/lv_example_switch_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/slider/lv_example_slider_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/slider/lv_example_slider_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/slider/lv_example_slider_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/slider/lv_example_slider_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_5.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_7.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_8.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/canvas/lv_example_canvas_6.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/button/lv_example_button_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/button/lv_example_button_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/button/lv_example_button_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/checkbox/lv_example_checkbox_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/checkbox/lv_example_checkbox_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/span/lv_example_span_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/spinner/lv_example_spinner_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/imagebutton/lv_example_imagebutton_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/roller/lv_example_roller_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/roller/lv_example_roller_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/roller/lv_example_roller_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/tabview/lv_example_tabview_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/tabview/lv_example_tabview_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/label/lv_example_label_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/label/lv_example_label_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/label/lv_example_label_5.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/label/lv_example_label_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/label/lv_example_label_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/menu/lv_example_menu_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/menu/lv_example_menu_5.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/menu/lv_example_menu_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/menu/lv_example_menu_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/menu/lv_example_menu_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/textarea/lv_example_textarea_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/textarea/lv_example_textarea_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/textarea/lv_example_textarea_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/animimg/lv_example_animimg_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/tileview/lv_example_tileview_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/image/lv_example_image_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/image/lv_example_image_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/image/lv_example_image_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/image/lv_example_image_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/obj/lv_example_obj_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/obj/lv_example_obj_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/bar/lv_example_bar_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/bar/lv_example_bar_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/bar/lv_example_bar_6.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/bar/lv_example_bar_5.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/bar/lv_example_bar_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/bar/lv_example_bar_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/bar/lv_example_bar_7.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/buttonmatrix/lv_example_buttonmatrix_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/buttonmatrix/lv_example_buttonmatrix_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/buttonmatrix/lv_example_buttonmatrix_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_6.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_3.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_5.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_4.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_7.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/chart/lv_example_chart_8.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/msgbox/lv_example_msgbox_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/list/lv_example_list_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/list/lv_example_list_2.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/spinbox/lv_example_spinbox_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/win/lv_example_win_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/calendar/lv_example_calendar_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/led/lv_example_led_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/table/lv_example_table_1.c
CC ../../lib/lv_bindings/lvgl/examples/widgets/table/lv_example_table_2.c
CC main.c
LINK build-standard/micropython
   text    data     bss     dec     hex filename
1741466  225840    7472 1974778  1e21fa build-standard/micropython
make: Leaving directory '/home/rini-debian/git-stash/lvgl-ui-detector/lvgl_ui_generator_v2/lv_micropython/ports/unix'
```

</details>

# Usage

```shell
usage: src/main.py [-h] [-m, --mode mode] [-?, --usage] [-n, --normalize] [-o, --output_file output_file]

Process CLI arguments for the UI generator.

optional args:
  -h, --help                        show this message and exit
  -m, --mode mode                   the mode to run the program in
  -?, --usage                       Print usage information for that mode.
  -n, --normalize                   normalize the bounding boxes
  -o, --output_file output_file     The output file (screenshot)
```

## TL;DR

To quickly generate a user interface without prior knowledge of the CLI, use the following commands to copy & paste:

### Random mode

Run via `invoke`:
```shell
poetry run invoke generate-random
```

or via `poetry`:
```shell
poetry run micropython src/main.py -m random --normalize -o screenshot.jpg -W 640 -H 640 -c 4 -l none --random-state -t arc bar button buttonmatrix calendar checkbox dropdown label roller scale slider spinbox switch table textarea
```

or directly:
```shell
./lv_micropython/ports/unix/build-standard/micropython src/main.py -m random --normalize -o screenshot.jpg -W 640 -H 640 -c 4 -l none --random-state -t arc bar button buttonmatrix calendar checkbox dropdown label roller scale slider spinbox switch table textarea
```

### Design mode

Run via `invoke`:
```shell
poetry run invoke generate-design
```

or via `poetry`:
```shell
poetry run micropython src/main.py -m design --normalize -f ./designs/widgets_showcase.json -o screenshot.jpg
```

or directly:
```shell
./lv_micropython/ports/unix/build-standard/micropython src/main.py -m design --normalize -f ./designs/widgets_showcase.json -o screenshot.jpg
```

## Usage of random mode

```shell
usage: src/main.py [-h] [-m, --mode mode] [-?, --usage] [-n, --normalize] [-o, --output_file output_file] [-W, --width width] [-H, --height height] [-c, --widget_count widget_count] [-t, --widget_types widget_types+] [-l, --layout layout] [--random-state]

Process CLI arguments for the UI generator.

optional args:
  -h, --help                        show this message and exit
  -m, --mode                        mode the mode to run the program in
  -?, --usage                       Print usage information for that mode.
  -n, --normalize                   normalize the bounding boxes
  -o, --output_file output_file     The output file (screenshot)
  -W, --width width                 the width of the UI
  -H, --height height               the height of the UI
  -c, --widget_count widget_count   the count of widgets
  -t, --widget_types widget_types+  A list of widget types
  -l, --layout layout               the layout option
  --random-state                    Use a random state for each created widget (experimental)
```

### Widget types

Not all widget types of LittlevGL are implemented yet. You may use non-implemented widget types, but they probably will not be displayed properly or simply exist in their default state, if they have one.

The names of widget types are the lowercase names of the classes in the LittlevGL library, e.g. `lv_arc` is `arc`.

<details>

<summary>Implemented types</summary>

- Arc
- Bar
- Button
- Buttonmatrix
- Calendar
- Checkbox
- Dropdown
- Label
- Roller
- Scale
- Slider
- Spinbox
- Switch
- Table
- Textarea

</details>

### Layouts

The generator supports different layouts to structure the widgets inside the container. The following layouts are available:

- `none`: No layout, widgets are placed using absolute positioning. This is the default layout and recommended to use. To avoid overlapping widgets, the generator will try to find a free spot using a approximated spatial map of the UI.
- `flex`: A layout, which will align widgets in either row or column, fitting as needed. The flex mode used is hardcoded to ROW_WRAP, which means that the widgets will be placed in a row, and if the row is full, the next widget will be placed in the next row.
- `grid`: A layout, which will align widgets in a grid. The grid layout is not yet implemented, since it is very error-prone in the way widgets are randomly created and placed.

### Style randomization

The generator will always randomize the style of each widget upon creation.

It does so by randomly choosing multiple properties from a list of hardcoded properties and setting a random value for each of them. The hardcoded list can be found in the `randomize_style()` function of `src/random_ui.py`, but for convenience is also provided below.

The generator will randomize at least 3 properties, up to the length of the hardcoded property list.

The properties are applied to the widget by first creating a style object, then setting the properties on the style object and finally applying the style to the widget. This should avoid issues with properties not being available or applicable for certain widget types.

<details>

<summary> List of style properties used for randomization</summary>

- `set_bg_color` -> `lv.color_hex(random.randint(0, 0xFFFFFF))`
- `set_bg_opa` -> `random.randint(0, 100)`
- `set_border_color` -> `lv.color_hex(random.randint(0, 0xFFFFFF))`
- `set_border_opa` -> `random.randint(0, 100)`
- `set_border_width` -> `random.randint(0, 10)`
- `set_outline_width` -> `random.randint(0, 10)`
- `set_outline_color` -> `lv.color_hex(random.randint(0, 0xFFFFFF))`
- `set_outline_opa` -> `random.randint(0, 100)`
- `set_shadow_width` -> `random.randint(0, 15)`
- `set_shadow_offset_x` -> `random.randint(0, 10)`
- `set_shadow_offset_y` -> `random.randint(0, 10)`
- `set_shadow_color` -> `lv.color_hex(random.randint(0, 0xFFFFFF))`
- `set_shadow_opa` -> `random.randint(0, 100)`
- `set_line_width` -> `random.randint(0, 10)`
- `set_line_dash_width` -> `random.randint(0, 10)`
- `set_line_dash_gap` -> `random.randint(0, 10)`
- `set_line_rounded` -> `random.choice([True, False])`
- `set_line_color` -> `lv.color_hex(random.randint(0, 0xFFFFFF))`
- `set_line_opa` -> `random.randint(0, 100)`
- `set_text_color` -> `lv.color_hex(random.randint(0, 0xFFFFFF))`
- `set_text_opa` -> `random.randint(0, 100)`
- `set_text_letter_space` -> `random.randint(0, 10)`
- `set_text_line_space` -> `random.randint(0, 10)`
- `set_opa` -> `random.randint(0, 100)`
- `set_align` -> `random.choice([lv.ALIGN.CENTER, lv.ALIGN.TOP_LEFT, lv.ALIGN.TOP_RIGHT, lv.ALIGN.TOP_MID, lv.ALIGN.BOTTOM_LEFT, lv.ALIGN.BOTTOM_RIGHT, lv.ALIGN.BOTTOM_MID, lv.ALIGN.LEFT_MID, lv.ALIGN.RIGHT_MID, lv.ALIGN.DEFAULT])`
- `set_pad_all` -> `random.randint(0, 10)`
- `set_pad_hor` -> `random.randint(0, 10)`
- `set_pad_ver` -> `random.randint(0, 10)`
- `set_pad_gap` -> `random.randint(0, 10)`
- `set_pad_top` -> `random.randint(0, 10)`
- `set_pad_bottom` -> `random.randint(0, 10)`
- `set_pad_left` -> `random.randint(0, 10)`
- `set_pad_right` -> `random.randint(0, 10)`
- `set_pad_row` -> `random.randint(0, 10)`
- `set_pad_column` -> `random.randint(0, 10)`
- `set_margin_top` -> `random.randint(0, 10)`
- `set_margin_bottom` -> `random.randint(0, 10)`
- `set_margin_left` -> `random.randint(0, 10)`
- `set_margin_right` -> `random.randint(0, 10`

</details>

### State randomization

The `--random-state` flag will randomize the state of each widget upon creation. 

This is an experimental feature, as it is not always desired to be used. Additionally, randomizing the state of a widget may lead to a widget not being displayed, due to random choice of a state that is either not supported by the widget or the state hiding the widget in general.
It may also simply not affect the widget at all, which is another reason I have provided this as an optional flag.

<details>

<summary>List of widget states used for randomization</summary>

- `lv.STATE.CHECKED`
- `lv.STATE.DISABLED`
- `lv.STATE.FOCUSED`
- `lv.STATE.PRESSED`
- `lv.STATE.HOVERED`
- `lv.STATE.EDITED`

</details>

## Design mode

```shell
usage: src/main.py [-h] [-m, --mode mode] [-?, --usage] [-n, --normalize] [-o, --output_file output_file] [-f, --file file]

Process CLI arguments for the UI generator.

optional args:
  -h, --help                            show this message and exit
  -m, --mode mode                       the mode to run the program in
  -?, --usage                           Print usage information for that mode.
  -n, --normalize                       normalize the bounding boxes
  -o, --output_file output_file         The output file (screenshot)
  -f, --file                            file path to JSON design file
```

### Design file specification

Design files need to be valid according to the [JSON schema (`design_file.schema.json`)](schema/design_file.schema.json).

If design files are invalid, the design parser will throw a `ValueError` whenever it encounters required objects that are missing or have the wrong type.
For widget definition, not all properties are required and if some are missing, the generator will make up for it by randomly choosing an appropriate value.

For example, if you create the `label` widget and do not provide a `text` property, the generator will choose a random amount of symbols from the displayable ASCII table and set it as the text of the label.

The overall structure of the design file should look like this:

```json
{
    "$schema": "./schema/design_file.schema.json",
    "ui": {
        "window": {
            "width": 640,
            "height": 640,
            "title": "Example design file"
        },
        "root": {
            "id": "main_container",
            "type": "container",
            "options": {
                "layout_type": "none"
            },
            "style": [
                "main_container_style"
            ],
            "children": [
                ...
            ]
        },
        "styles": {
            ...
        }
    }
}
```

Have a look at the [designs folder](designs) for examples of design files. The [widgets_showcase.json](designs/widgets_showcase.json) file is a good starting point to see usage of all implemented widget types.

#### General design file rules & notes

Writing a design parser is a bit complicated, so there are some rules to follow when creating a design file:

1. It is mandatory that the first widget object in `root` is a container, as the root widget is always a container _(in any UI framework as far as I am aware)_. **Unexpected/error behavior will occur if this is not the case.**
2. The title of the window is not mandatory and also not used by the generator. It is only there for reference to the user possibly looking through dozens of design files.
3. The `styles` object is optional and can be omitted if no styles are defined.
4. Added styles are referenced by their name in the `style` array of each widget. If a style is not found, the generator will throw a `ValueError`.
5. A style defines a list of properties that are applied to widgets via the usage of a `lv.style_t` object. The possible properties are the same as documented in the [LittlevGL API for styles](https://docs.lvgl.io/9.1/API/misc/lv_style_gen.html#). Properties are verified by checking if the specified name has a corresponding `setter` attribute in the `lv.style_t` object. This is done by appending `set_` to the property name, thus you are required to use the property setter function names without the `set_` prefix. For example, to set the background color of a widget, you would use the property `bg_color`. The generator will then look for the `set_bg_color` attribute in the `lv.style_t` object and apply the converted value to it.
6. If a provided `property` inside a `style` object does not actually correspond to an available attribute in `lv.style_t`, the generator will ignore it and continue.
7. Values supplied to style properties are converted according to the required type of the property. Some properties taking in special objects, like colors, require a specific string to be supplied (e.g. `#AABBCC` for any color property or `top-left` for the `align` property). You can checkout the details of the value conversion in the function `convert_value()` of `design_parser.py`.
8. If value conversion fails, the property is ignored and the generator will ignore it and continue.
9. The `id` property is mandatory for widgets of type `container`, as it is required to reference the container inside the `children` array, when the special widget type `random` is used.
10. The special widget type `random` may be used to supply a list of widget types for the generator to randomly choose from and then create a random widget in similar fashion to the random mode. This is useful for randomizing widgets in certain areas of the UI, while keeping the rest of the UI static.

#### Validating design files

You can validate your design files against the available JSON schema in the repository by using the `jsonschema` package in python. Keep in mind, that `micropython` does not have this package and you will need to use the regular python interpreter to do this.

This is usually more descriptive than the error messages provided by the generator.

Here is a simple script to validate a design file:

<details>

<summary>validate_design.py</summary>

```python
def load_json_file(filepath: str):
    import json
    with open(filepath, 'r') as f:
        return json.load(f)

def verify_design_from_file(design_file: str, schema_file: str) -> tuple[bool, Exception]:
    from jsonschema import validate
    from jsonschema.exceptions import ValidationError
    design = load_json_file(design_file)
    schema = load_json_file(schema_file)
    try:
        validate(instance=design, schema=schema)
        print(f"Provided design file {design_file} is valid.")
        return True, None
    except ValidationError as e:
        print(f"Provided design file {design_file} is invalid:\n{e}")
        return False, e

if __name__ == '__main__':
    verify_design_from_file('path/to/design_file.json', 'path/to/design_file.schema.json')
```

</details>

# Development

Inside the `stubs` folder is the `lvgl.pyi` stubs file, which contains type hints for the [LVGL micropython bindings](https://github.com/lvgl/lv_binding_micropython). This is useful for development in an IDE that supports type hinting, like VS Code with the Python extension.

The `settings.json` file in the `.vscode` folder contains the necessary settings to enable type hinting for the `lvgl.pyi` file in Visual Studio Code.

The stubs file was generated by [kdschlosser](https://github.com/kdschlosser) and supplied to me during a [discussion on the LVGL forum](https://forum.lvgl.io/t/how-does-one-create-micropython-stubs-of-lvgl-bindings-for-unix-port/15233).

The used stub generator for this file can be viewed [in this PR](https://github.com/lvgl/lvgl/pull/5677) and is generally not merged yet into LVGL, so it is not complete and may cause errors.

The created stubs file also does not cover all functions and classes of the LittlevGL bindings, but generally covers enough and linting errors are more of a nuisance than a real issue.

# Known issues

- Creating a screenshot using the [`snapshot` API of LittlevGL](https://docs.lvgl.io/9.1/others/snapshot.html) certainly causes memory leakage due to the manually added JPEG encoding mechanism in `screenshot.py` and dereferencing of the data buffer. It is hard to deal with this without a proper JPG encoder library built into micropython binary. The memory leakage is not too severe and I attempted to mitigate it by attempting to always free the snapshot buffer using `lv.snapshot_free()` but it is not fool-proof.
- The generator may sometimes cause a memory allocation error when attempting to create the JPG buffer for the screenshot. This is due to the fact that the JPG buffer is created in heap and knowingly it is limited in size. The generator will attempt to free the buffer after the screenshot is taken, but it is not guaranteed that the buffer is freed properly. This is a known issue and there is no solution as of yet. You can try to run the generator again and it might work again after the OS has cleared up some memory.
- The JPG output of the screenshot may sometimes be corrupted or the image data is heavily distorted. This is due to race conditions between creating the snapshot buffer and LVGL re-rendering the UI. It is currently not possible to mitigate this issue without writing a custom C library for LVGL which will handle the snapshot creation and JPEG encoding in a more controlled manner. The LVGL bindings do not have exposed APIs to handle this inside micropython as far as I know.

# License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.