from typing import Union, ClassVar, Callable, List, Any, TypedDict


DPI_DEF: int = ...
DRAW_BUF_STRIDE_ALIGN: int = ...
DRAW_BUF_ALIGN: int = ...
ANIM_REPEAT_INFINITE: int = ...
ANIM_PLAYTIME_INFINITE: int = ...
SIZE_CONTENT: int = ...
COLOR_DEPTH: int = ...
IMAGE_HEADER_MAGIC: int = ...
STRIDE_AUTO: int = ...
GRID_CONTENT: int = ...
GRID_TEMPLATE_LAST: int = ...
SCALE_NONE: int = ...
RADIUS_CIRCLE: int = ...
LABEL_DOT_NUM: int = ...
LABEL_POS_LAST: int = ...
LABEL_TEXT_SELECTION_OFF: int = ...
BUTTONMATRIX_BUTTON_NONE: int = ...
CHART_POINT_NONE: int = ...
DROPDOWN_POS_LAST: int = ...
SCALE_TOTAL_TICK_COUNT_DEFAULT: int = ...
SCALE_MAJOR_TICK_EVERY_DEFAULT: int = ...
SCALE_LABEL_ENABLED_DEFAULT: int = ...
TEXTAREA_CURSOR_LAST: int = ...
TABLE_CELL_NONE: int = ...


class RESULT(object):
    """
    No Docstrings Yet
    """
    INVALID: ClassVar[int] = ...
    OK: ClassVar[int] = ...


class LOG_LEVEL(object):
    """
    No Docstrings Yet
    """
    TRACE: ClassVar[int] = ...
    INFO: ClassVar[int] = ...
    WARN: ClassVar[int] = ...
    ERROR: ClassVar[int] = ...
    USER: ClassVar[int] = ...
    NONE: ClassVar[int] = ...


class ALIGN(object):
    """
    No Docstrings Yet
    """
    DEFAULT: ClassVar[int] = ...
    TOP_LEFT: ClassVar[int] = ...
    TOP_MID: ClassVar[int] = ...
    TOP_RIGHT: ClassVar[int] = ...
    BOTTOM_LEFT: ClassVar[int] = ...
    BOTTOM_MID: ClassVar[int] = ...
    BOTTOM_RIGHT: ClassVar[int] = ...
    LEFT_MID: ClassVar[int] = ...
    RIGHT_MID: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    OUT_TOP_LEFT: ClassVar[int] = ...
    OUT_TOP_MID: ClassVar[int] = ...
    OUT_TOP_RIGHT: ClassVar[int] = ...
    OUT_BOTTOM_LEFT: ClassVar[int] = ...
    OUT_BOTTOM_MID: ClassVar[int] = ...
    OUT_BOTTOM_RIGHT: ClassVar[int] = ...
    OUT_LEFT_TOP: ClassVar[int] = ...
    OUT_LEFT_MID: ClassVar[int] = ...
    OUT_LEFT_BOTTOM: ClassVar[int] = ...
    OUT_RIGHT_TOP: ClassVar[int] = ...
    OUT_RIGHT_MID: ClassVar[int] = ...
    OUT_RIGHT_BOTTOM: ClassVar[int] = ...


class DIR(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    ALL: ClassVar[int] = ...


class COORD(object):
    """
    No Docstrings Yet
    """
    MAX: ClassVar[int] = ...
    MIN: ClassVar[int] = ...


class OPA(object):
    """
    No Docstrings Yet
    """
    TRANSP: ClassVar[int] = ...
    _0: ClassVar[int] = ...
    _10: ClassVar[int] = ...
    _20: ClassVar[int] = ...
    _30: ClassVar[int] = ...
    _40: ClassVar[int] = ...
    _50: ClassVar[int] = ...
    _60: ClassVar[int] = ...
    _70: ClassVar[int] = ...
    _80: ClassVar[int] = ...
    _90: ClassVar[int] = ...
    _100: ClassVar[int] = ...
    COVER: ClassVar[int] = ...


class COLOR_FORMAT(object):
    """
    No Docstrings Yet
    """
    UNKNOWN: ClassVar[int] = ...
    RAW: ClassVar[int] = ...
    RAW_ALPHA: ClassVar[int] = ...
    L8: ClassVar[int] = ...
    I1: ClassVar[int] = ...
    I2: ClassVar[int] = ...
    I4: ClassVar[int] = ...
    I8: ClassVar[int] = ...
    A8: ClassVar[int] = ...
    RGB565: ClassVar[int] = ...
    ARGB8565: ClassVar[int] = ...
    RGB565A8: ClassVar[int] = ...
    RGB888: ClassVar[int] = ...
    ARGB8888: ClassVar[int] = ...
    XRGB8888: ClassVar[int] = ...
    A1: ClassVar[int] = ...
    A2: ClassVar[int] = ...
    A4: ClassVar[int] = ...
    YUV_START: ClassVar[int] = ...
    I420: ClassVar[int] = ...
    I422: ClassVar[int] = ...
    I444: ClassVar[int] = ...
    I400: ClassVar[int] = ...
    NV21: ClassVar[int] = ...
    NV12: ClassVar[int] = ...
    YUY2: ClassVar[int] = ...
    UYVY: ClassVar[int] = ...
    YUV_END: ClassVar[int] = ...
    NATIVE: ClassVar[int] = ...
    NATIVE_WITH_ALPHA: ClassVar[int] = ...


class FONT_GLYPH_FORMAT(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    A1: ClassVar[int] = ...
    A2: ClassVar[int] = ...
    A4: ClassVar[int] = ...
    A8: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    VECTOR: ClassVar[int] = ...
    SVG: ClassVar[int] = ...
    CUSTOM: ClassVar[int] = ...


class FONT_SUBPX(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    HOR: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    BOTH: ClassVar[int] = ...


class FONT_KERNING(object):
    """
    No Docstrings Yet
    """
    NORMAL: ClassVar[int] = ...
    NONE: ClassVar[int] = ...


class TEXT_FLAG(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    EXPAND: ClassVar[int] = ...
    FIT: ClassVar[int] = ...


class TEXT_ALIGN(object):
    """
    No Docstrings Yet
    """
    AUTO: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...


class BASE_DIR(object):
    """
    No Docstrings Yet
    """
    LTR: ClassVar[int] = ...
    RTL: ClassVar[int] = ...
    AUTO: ClassVar[int] = ...
    NEUTRAL: ClassVar[int] = ...
    WEAK: ClassVar[int] = ...


class BLEND_MODE(object):
    """
    No Docstrings Yet
    """
    NORMAL: ClassVar[int] = ...
    ADDITIVE: ClassVar[int] = ...
    SUBTRACTIVE: ClassVar[int] = ...
    MULTIPLY: ClassVar[int] = ...


class TEXT_DECOR(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    UNDERLINE: ClassVar[int] = ...
    STRIKETHROUGH: ClassVar[int] = ...


class BORDER_SIDE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    FULL: ClassVar[int] = ...
    INTERNAL: ClassVar[int] = ...


class GRAD_DIR(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    VER: ClassVar[int] = ...
    HOR: ClassVar[int] = ...


class STYLE(object):
    """
    No Docstrings Yet
    """
    PROP_INV: ClassVar[int] = ...
    WIDTH: ClassVar[int] = ...
    HEIGHT: ClassVar[int] = ...
    LENGTH: ClassVar[int] = ...
    MIN_WIDTH: ClassVar[int] = ...
    MAX_WIDTH: ClassVar[int] = ...
    MIN_HEIGHT: ClassVar[int] = ...
    MAX_HEIGHT: ClassVar[int] = ...
    X: ClassVar[int] = ...
    Y: ClassVar[int] = ...
    ALIGN: ClassVar[int] = ...
    RADIUS: ClassVar[int] = ...
    PAD_TOP: ClassVar[int] = ...
    PAD_BOTTOM: ClassVar[int] = ...
    PAD_LEFT: ClassVar[int] = ...
    PAD_RIGHT: ClassVar[int] = ...
    PAD_ROW: ClassVar[int] = ...
    PAD_COLUMN: ClassVar[int] = ...
    LAYOUT: ClassVar[int] = ...
    MARGIN_TOP: ClassVar[int] = ...
    MARGIN_BOTTOM: ClassVar[int] = ...
    MARGIN_LEFT: ClassVar[int] = ...
    MARGIN_RIGHT: ClassVar[int] = ...
    BG_COLOR: ClassVar[int] = ...
    BG_OPA: ClassVar[int] = ...
    BG_GRAD_DIR: ClassVar[int] = ...
    BG_MAIN_STOP: ClassVar[int] = ...
    BG_GRAD_STOP: ClassVar[int] = ...
    BG_GRAD_COLOR: ClassVar[int] = ...
    BG_MAIN_OPA: ClassVar[int] = ...
    BG_GRAD_OPA: ClassVar[int] = ...
    BG_GRAD: ClassVar[int] = ...
    BASE_DIR: ClassVar[int] = ...
    BG_IMAGE_SRC: ClassVar[int] = ...
    BG_IMAGE_OPA: ClassVar[int] = ...
    BG_IMAGE_RECOLOR: ClassVar[int] = ...
    BG_IMAGE_RECOLOR_OPA: ClassVar[int] = ...
    BG_IMAGE_TILED: ClassVar[int] = ...
    CLIP_CORNER: ClassVar[int] = ...
    BORDER_WIDTH: ClassVar[int] = ...
    BORDER_COLOR: ClassVar[int] = ...
    BORDER_OPA: ClassVar[int] = ...
    BORDER_SIDE: ClassVar[int] = ...
    BORDER_POST: ClassVar[int] = ...
    OUTLINE_WIDTH: ClassVar[int] = ...
    OUTLINE_COLOR: ClassVar[int] = ...
    OUTLINE_OPA: ClassVar[int] = ...
    OUTLINE_PAD: ClassVar[int] = ...
    SHADOW_WIDTH: ClassVar[int] = ...
    SHADOW_COLOR: ClassVar[int] = ...
    SHADOW_OPA: ClassVar[int] = ...
    SHADOW_OFFSET_X: ClassVar[int] = ...
    SHADOW_OFFSET_Y: ClassVar[int] = ...
    SHADOW_SPREAD: ClassVar[int] = ...
    IMAGE_OPA: ClassVar[int] = ...
    IMAGE_RECOLOR: ClassVar[int] = ...
    IMAGE_RECOLOR_OPA: ClassVar[int] = ...
    LINE_WIDTH: ClassVar[int] = ...
    LINE_DASH_WIDTH: ClassVar[int] = ...
    LINE_DASH_GAP: ClassVar[int] = ...
    LINE_ROUNDED: ClassVar[int] = ...
    LINE_COLOR: ClassVar[int] = ...
    LINE_OPA: ClassVar[int] = ...
    ARC_WIDTH: ClassVar[int] = ...
    ARC_ROUNDED: ClassVar[int] = ...
    ARC_COLOR: ClassVar[int] = ...
    ARC_OPA: ClassVar[int] = ...
    ARC_IMAGE_SRC: ClassVar[int] = ...
    TEXT_COLOR: ClassVar[int] = ...
    TEXT_OPA: ClassVar[int] = ...
    TEXT_FONT: ClassVar[int] = ...
    TEXT_LETTER_SPACE: ClassVar[int] = ...
    TEXT_LINE_SPACE: ClassVar[int] = ...
    TEXT_DECOR: ClassVar[int] = ...
    TEXT_ALIGN: ClassVar[int] = ...
    OPA: ClassVar[int] = ...
    OPA_LAYERED: ClassVar[int] = ...
    COLOR_FILTER_DSC: ClassVar[int] = ...
    COLOR_FILTER_OPA: ClassVar[int] = ...
    ANIM: ClassVar[int] = ...
    ANIM_DURATION: ClassVar[int] = ...
    TRANSITION: ClassVar[int] = ...
    BLEND_MODE: ClassVar[int] = ...
    TRANSFORM_WIDTH: ClassVar[int] = ...
    TRANSFORM_HEIGHT: ClassVar[int] = ...
    TRANSLATE_X: ClassVar[int] = ...
    TRANSLATE_Y: ClassVar[int] = ...
    TRANSFORM_SCALE_X: ClassVar[int] = ...
    TRANSFORM_SCALE_Y: ClassVar[int] = ...
    TRANSFORM_ROTATION: ClassVar[int] = ...
    TRANSFORM_PIVOT_X: ClassVar[int] = ...
    TRANSFORM_PIVOT_Y: ClassVar[int] = ...
    TRANSFORM_SKEW_X: ClassVar[int] = ...
    TRANSFORM_SKEW_Y: ClassVar[int] = ...
    BITMAP_MASK_SRC: ClassVar[int] = ...
    ROTARY_SENSITIVITY: ClassVar[int] = ...
    FLEX_FLOW: ClassVar[int] = ...
    FLEX_MAIN_PLACE: ClassVar[int] = ...
    FLEX_CROSS_PLACE: ClassVar[int] = ...
    FLEX_TRACK_PLACE: ClassVar[int] = ...
    FLEX_GROW: ClassVar[int] = ...
    GRID_COLUMN_ALIGN: ClassVar[int] = ...
    GRID_ROW_ALIGN: ClassVar[int] = ...
    GRID_ROW_DSC_ARRAY: ClassVar[int] = ...
    GRID_COLUMN_DSC_ARRAY: ClassVar[int] = ...
    GRID_CELL_COLUMN_POS: ClassVar[int] = ...
    GRID_CELL_COLUMN_SPAN: ClassVar[int] = ...
    GRID_CELL_X_ALIGN: ClassVar[int] = ...
    GRID_CELL_ROW_POS: ClassVar[int] = ...
    GRID_CELL_ROW_SPAN: ClassVar[int] = ...
    GRID_CELL_Y_ALIGN: ClassVar[int] = ...
    PROP_ANY: ClassVar[int] = ...


class STYLE_RES(object):
    """
    No Docstrings Yet
    """
    NOT_FOUND: ClassVar[int] = ...
    FOUND: ClassVar[int] = ...


class FS_RES(object):
    """
    No Docstrings Yet
    """
    OK: ClassVar[int] = ...
    HW_ERR: ClassVar[int] = ...
    FS_ERR: ClassVar[int] = ...
    NOT_EX: ClassVar[int] = ...
    FULL: ClassVar[int] = ...
    LOCKED: ClassVar[int] = ...
    DENIED: ClassVar[int] = ...
    BUSY: ClassVar[int] = ...
    TOUT: ClassVar[int] = ...
    NOT_IMP: ClassVar[int] = ...
    OUT_OF_MEM: ClassVar[int] = ...
    INV_PARAM: ClassVar[int] = ...
    UNKNOWN: ClassVar[int] = ...


class FS_MODE(object):
    """
    No Docstrings Yet
    """
    WR: ClassVar[int] = ...
    RD: ClassVar[int] = ...


class SCROLLBAR_MODE(object):
    """
    No Docstrings Yet
    """
    OFF: ClassVar[int] = ...
    ON: ClassVar[int] = ...
    ACTIVE: ClassVar[int] = ...
    AUTO: ClassVar[int] = ...


class SCROLL_SNAP(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    START: ClassVar[int] = ...
    END: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...


class KEY(object):
    """
    No Docstrings Yet
    """
    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    ESC: ClassVar[int] = ...
    DEL: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    ENTER: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    END: ClassVar[int] = ...


class STATE(object):
    """
    No Docstrings Yet
    """
    DEFAULT: ClassVar[int] = ...
    CHECKED: ClassVar[int] = ...
    FOCUSED: ClassVar[int] = ...
    FOCUS_KEY: ClassVar[int] = ...
    EDITED: ClassVar[int] = ...
    HOVERED: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...
    SCROLLED: ClassVar[int] = ...
    DISABLED: ClassVar[int] = ...
    USER_1: ClassVar[int] = ...
    USER_2: ClassVar[int] = ...
    USER_3: ClassVar[int] = ...
    USER_4: ClassVar[int] = ...
    ANY: ClassVar[int] = ...


class PART(object):
    """
    No Docstrings Yet
    """
    MAIN: ClassVar[int] = ...
    SCROLLBAR: ClassVar[int] = ...
    INDICATOR: ClassVar[int] = ...
    KNOB: ClassVar[int] = ...
    SELECTED: ClassVar[int] = ...
    ITEMS: ClassVar[int] = ...
    CURSOR: ClassVar[int] = ...
    CUSTOM_FIRST: ClassVar[int] = ...
    ANY: ClassVar[int] = ...


class FONT_FMT_TXT_CMAP(object):
    """
    No Docstrings Yet
    """
    FORMAT0_FULL: ClassVar[int] = ...
    SPARSE_FULL: ClassVar[int] = ...
    FORMAT0_TINY: ClassVar[int] = ...
    SPARSE_TINY: ClassVar[int] = ...


class ANIM_IMAGE_PART(object):
    """
    No Docstrings Yet
    """
    MAIN: ClassVar[int] = ...


class SPAN_OVERFLOW(object):
    """
    No Docstrings Yet
    """
    CLIP: ClassVar[int] = ...
    ELLIPSIS: ClassVar[int] = ...


class SPAN_MODE(object):
    """
    No Docstrings Yet
    """
    FIXED: ClassVar[int] = ...
    EXPAND: ClassVar[int] = ...
    BREAK: ClassVar[int] = ...


class PART_TEXTAREA(object):
    """
    No Docstrings Yet
    """
    PLACEHOLDER: ClassVar[int] = ...


class DRAW_SW_MASK_RES(object):
    """
    No Docstrings Yet
    """
    TRANSP: ClassVar[int] = ...
    FULL_COVER: ClassVar[int] = ...
    CHANGED: ClassVar[int] = ...
    UNKNOWN: ClassVar[int] = ...


class DRAW_SW_MASK_TYPE(object):
    """
    No Docstrings Yet
    """
    LINE: ClassVar[int] = ...
    ANGLE: ClassVar[int] = ...
    RADIUS: ClassVar[int] = ...
    FADE: ClassVar[int] = ...
    MAP: ClassVar[int] = ...


class DRAW_SW_MASK_LINE_SIDE(object):
    """
    No Docstrings Yet
    """
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    TOP: ClassVar[int] = ...
    BOTTOM: ClassVar[int] = ...


class ANIM(object):
    """
    No Docstrings Yet
    """
    OFF: ClassVar[int] = ...
    ON: ClassVar[int] = ...


class RB_COLOR(object):
    """
    No Docstrings Yet
    """
    RED: ClassVar[int] = ...
    BLACK: ClassVar[int] = ...


class PALETTE(object):
    """
    No Docstrings Yet
    """
    RED: ClassVar[int] = ...
    PINK: ClassVar[int] = ...
    PURPLE: ClassVar[int] = ...
    DEEP_PURPLE: ClassVar[int] = ...
    INDIGO: ClassVar[int] = ...
    BLUE: ClassVar[int] = ...
    LIGHT_BLUE: ClassVar[int] = ...
    CYAN: ClassVar[int] = ...
    TEAL: ClassVar[int] = ...
    GREEN: ClassVar[int] = ...
    LIGHT_GREEN: ClassVar[int] = ...
    LIME: ClassVar[int] = ...
    YELLOW: ClassVar[int] = ...
    AMBER: ClassVar[int] = ...
    ORANGE: ClassVar[int] = ...
    DEEP_ORANGE: ClassVar[int] = ...
    BROWN: ClassVar[int] = ...
    BLUE_GREY: ClassVar[int] = ...
    GREY: ClassVar[int] = ...
    NONE: ClassVar[int] = ...


class THREAD_PRIO(object):
    """
    No Docstrings Yet
    """
    LOWEST: ClassVar[int] = ...
    LOW: ClassVar[int] = ...
    MID: ClassVar[int] = ...
    HIGH: ClassVar[int] = ...
    HIGHEST: ClassVar[int] = ...


class CACHE_RESERVE_COND(object):
    """
    No Docstrings Yet
    """
    OK: ClassVar[int] = ...
    TOO_LARGE: ClassVar[int] = ...
    NEED_VICTIM: ClassVar[int] = ...
    ERROR: ClassVar[int] = ...


class LAYOUT(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    FLEX: ClassVar[int] = ...
    GRID: ClassVar[int] = ...


class FLEX_ALIGN(object):
    """
    No Docstrings Yet
    """
    START: ClassVar[int] = ...
    END: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    SPACE_EVENLY: ClassVar[int] = ...
    SPACE_AROUND: ClassVar[int] = ...
    SPACE_BETWEEN: ClassVar[int] = ...


class FLEX_FLOW(object):
    """
    No Docstrings Yet
    """
    ROW: ClassVar[int] = ...
    COLUMN: ClassVar[int] = ...
    ROW_WRAP: ClassVar[int] = ...
    ROW_REVERSE: ClassVar[int] = ...
    ROW_WRAP_REVERSE: ClassVar[int] = ...
    COLUMN_WRAP: ClassVar[int] = ...
    COLUMN_REVERSE: ClassVar[int] = ...
    COLUMN_WRAP_REVERSE: ClassVar[int] = ...


class GRID_ALIGN(object):
    """
    No Docstrings Yet
    """
    START: ClassVar[int] = ...
    CENTER: ClassVar[int] = ...
    END: ClassVar[int] = ...
    STRETCH: ClassVar[int] = ...
    SPACE_EVENLY: ClassVar[int] = ...
    SPACE_AROUND: ClassVar[int] = ...
    SPACE_BETWEEN: ClassVar[int] = ...


class EVENT(object):
    """
    No Docstrings Yet
    """
    ALL: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...
    PRESSING: ClassVar[int] = ...
    PRESS_LOST: ClassVar[int] = ...
    SHORT_CLICKED: ClassVar[int] = ...
    LONG_PRESSED: ClassVar[int] = ...
    LONG_PRESSED_REPEAT: ClassVar[int] = ...
    CLICKED: ClassVar[int] = ...
    RELEASED: ClassVar[int] = ...
    SCROLL_BEGIN: ClassVar[int] = ...
    SCROLL_THROW_BEGIN: ClassVar[int] = ...
    SCROLL_END: ClassVar[int] = ...
    SCROLL: ClassVar[int] = ...
    GESTURE: ClassVar[int] = ...
    KEY: ClassVar[int] = ...
    ROTARY: ClassVar[int] = ...
    FOCUSED: ClassVar[int] = ...
    DEFOCUSED: ClassVar[int] = ...
    LEAVE: ClassVar[int] = ...
    HIT_TEST: ClassVar[int] = ...
    INDEV_RESET: ClassVar[int] = ...
    COVER_CHECK: ClassVar[int] = ...
    REFR_EXT_DRAW_SIZE: ClassVar[int] = ...
    DRAW_MAIN_BEGIN: ClassVar[int] = ...
    DRAW_MAIN: ClassVar[int] = ...
    DRAW_MAIN_END: ClassVar[int] = ...
    DRAW_POST_BEGIN: ClassVar[int] = ...
    DRAW_POST: ClassVar[int] = ...
    DRAW_POST_END: ClassVar[int] = ...
    DRAW_TASK_ADDED: ClassVar[int] = ...
    VALUE_CHANGED: ClassVar[int] = ...
    INSERT: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    READY: ClassVar[int] = ...
    CANCEL: ClassVar[int] = ...
    CREATE: ClassVar[int] = ...
    DELETE: ClassVar[int] = ...
    CHILD_CHANGED: ClassVar[int] = ...
    CHILD_CREATED: ClassVar[int] = ...
    CHILD_DELETED: ClassVar[int] = ...
    SCREEN_UNLOAD_START: ClassVar[int] = ...
    SCREEN_LOAD_START: ClassVar[int] = ...
    SCREEN_LOADED: ClassVar[int] = ...
    SCREEN_UNLOADED: ClassVar[int] = ...
    SIZE_CHANGED: ClassVar[int] = ...
    STYLE_CHANGED: ClassVar[int] = ...
    LAYOUT_CHANGED: ClassVar[int] = ...
    GET_SELF_SIZE: ClassVar[int] = ...
    INVALIDATE_AREA: ClassVar[int] = ...
    RESOLUTION_CHANGED: ClassVar[int] = ...
    COLOR_FORMAT_CHANGED: ClassVar[int] = ...
    REFR_REQUEST: ClassVar[int] = ...
    REFR_START: ClassVar[int] = ...
    REFR_READY: ClassVar[int] = ...
    RENDER_START: ClassVar[int] = ...
    RENDER_READY: ClassVar[int] = ...
    FLUSH_START: ClassVar[int] = ...
    FLUSH_FINISH: ClassVar[int] = ...
    FLUSH_WAIT_START: ClassVar[int] = ...
    FLUSH_WAIT_FINISH: ClassVar[int] = ...
    VSYNC: ClassVar[int] = ...
    PREPROCESS: ClassVar[int] = ...


class FS_SEEK(object):
    """
    No Docstrings Yet
    """
    SET: ClassVar[int] = ...
    CUR: ClassVar[int] = ...
    END: ClassVar[int] = ...


class DRAW_TASK_TYPE(object):
    """
    No Docstrings Yet
    """
    FILL: ClassVar[int] = ...
    BORDER: ClassVar[int] = ...
    BOX_SHADOW: ClassVar[int] = ...
    LABEL: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    LAYER: ClassVar[int] = ...
    LINE: ClassVar[int] = ...
    ARC: ClassVar[int] = ...
    TRIANGLE: ClassVar[int] = ...
    MASK_RECTANGLE: ClassVar[int] = ...
    MASK_BITMAP: ClassVar[int] = ...
    VECTOR: ClassVar[int] = ...


class DRAW_TASK_STATE(object):
    """
    No Docstrings Yet
    """
    WAITING: ClassVar[int] = ...
    QUEUED: ClassVar[int] = ...
    IN_PROGRESS: ClassVar[int] = ...
    READY: ClassVar[int] = ...


class DISPLAY_ROTATION(object):
    """
    No Docstrings Yet
    """
    _0: ClassVar[int] = ...
    _90: ClassVar[int] = ...
    _180: ClassVar[int] = ...
    _270: ClassVar[int] = ...


class DISPLAY_RENDER_MODE(object):
    """
    No Docstrings Yet
    """
    PARTIAL: ClassVar[int] = ...
    DIRECT: ClassVar[int] = ...
    FULL: ClassVar[int] = ...


class SCR_LOAD_ANIM(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    OVER_LEFT: ClassVar[int] = ...
    OVER_RIGHT: ClassVar[int] = ...
    OVER_TOP: ClassVar[int] = ...
    OVER_BOTTOM: ClassVar[int] = ...
    MOVE_LEFT: ClassVar[int] = ...
    MOVE_RIGHT: ClassVar[int] = ...
    MOVE_TOP: ClassVar[int] = ...
    MOVE_BOTTOM: ClassVar[int] = ...
    FADE_IN: ClassVar[int] = ...
    FADE_ON: ClassVar[int] = ...
    FADE_OUT: ClassVar[int] = ...
    OUT_LEFT: ClassVar[int] = ...
    OUT_RIGHT: ClassVar[int] = ...
    OUT_TOP: ClassVar[int] = ...
    OUT_BOTTOM: ClassVar[int] = ...


class LAYER_TYPE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    SIMPLE: ClassVar[int] = ...
    TRANSFORM: ClassVar[int] = ...


class GROUP_REFOCUS_POLICY(object):
    """
    No Docstrings Yet
    """
    NEXT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...


class INDEV_TYPE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    POINTER: ClassVar[int] = ...
    KEYPAD: ClassVar[int] = ...
    BUTTON: ClassVar[int] = ...
    ENCODER: ClassVar[int] = ...


class INDEV_STATE(object):
    """
    No Docstrings Yet
    """
    RELEASED: ClassVar[int] = ...
    PRESSED: ClassVar[int] = ...


class INDEV_MODE(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    TIMER: ClassVar[int] = ...
    EVENT: ClassVar[int] = ...


class COVER_RES(object):
    """
    No Docstrings Yet
    """
    COVER: ClassVar[int] = ...
    NOT_COVER: ClassVar[int] = ...
    MASKED: ClassVar[int] = ...


class FONT_FMT_TXT(object):
    """
    No Docstrings Yet
    """
    PLAIN: ClassVar[int] = ...
    COMPRESSED: ClassVar[int] = ...
    COMPRESSED_NO_PREFILTER: ClassVar[int] = ...


class SUBJECT_TYPE(object):
    """
    No Docstrings Yet
    """
    INVALID: ClassVar[int] = ...
    NONE: ClassVar[int] = ...
    INT: ClassVar[int] = ...
    POINTER: ClassVar[int] = ...
    COLOR: ClassVar[int] = ...
    GROUP: ClassVar[int] = ...
    STRING: ClassVar[int] = ...


class GRIDNAV_CTRL(object):
    """
    No Docstrings Yet
    """
    NONE: ClassVar[int] = ...
    ROLLOVER: ClassVar[int] = ...
    SCROLL_FIRST: ClassVar[int] = ...


class SYMBOL(object):
    """
    No Docstrings Yet
    """
    BULLET: ClassVar[int] = ...
    AUDIO: ClassVar[int] = ...
    VIDEO: ClassVar[int] = ...
    LIST: ClassVar[int] = ...
    OK: ClassVar[int] = ...
    CLOSE: ClassVar[int] = ...
    POWER: ClassVar[int] = ...
    SETTINGS: ClassVar[int] = ...
    HOME: ClassVar[int] = ...
    DOWNLOAD: ClassVar[int] = ...
    DRIVE: ClassVar[int] = ...
    REFRESH: ClassVar[int] = ...
    MUTE: ClassVar[int] = ...
    VOLUME_MID: ClassVar[int] = ...
    VOLUME_MAX: ClassVar[int] = ...
    IMAGE: ClassVar[int] = ...
    TINT: ClassVar[int] = ...
    PREV: ClassVar[int] = ...
    PLAY: ClassVar[int] = ...
    PAUSE: ClassVar[int] = ...
    STOP: ClassVar[int] = ...
    NEXT: ClassVar[int] = ...
    EJECT: ClassVar[int] = ...
    LEFT: ClassVar[int] = ...
    RIGHT: ClassVar[int] = ...
    PLUS: ClassVar[int] = ...
    MINUS: ClassVar[int] = ...
    EYE_OPEN: ClassVar[int] = ...
    EYE_CLOSE: ClassVar[int] = ...
    WARNING: ClassVar[int] = ...
    SHUFFLE: ClassVar[int] = ...
    UP: ClassVar[int] = ...
    DOWN: ClassVar[int] = ...
    LOOP: ClassVar[int] = ...
    DIRECTORY: ClassVar[int] = ...
    UPLOAD: ClassVar[int] = ...
    CALL: ClassVar[int] = ...
    CUT: ClassVar[int] = ...
    COPY: ClassVar[int] = ...
    SAVE: ClassVar[int] = ...
    BARS: ClassVar[int] = ...
    ENVELOPE: ClassVar[int] = ...
    CHARGE: ClassVar[int] = ...
    PASTE: ClassVar[int] = ...
    BELL: ClassVar[int] = ...
    KEYBOARD: ClassVar[int] = ...
    GPS: ClassVar[int] = ...
    FILE: ClassVar[int] = ...
    WIFI: ClassVar[int] = ...
    BATTERY_FULL: ClassVar[int] = ...
    BATTERY_3: ClassVar[int] = ...
    BATTERY_2: ClassVar[int] = ...
    BATTERY_1: ClassVar[int] = ...
    BATTERY_EMPTY: ClassVar[int] = ...
    USB: ClassVar[int] = ...
    BLUETOOTH: ClassVar[int] = ...
    TRASH: ClassVar[int] = ...
    EDIT: ClassVar[int] = ...
    BACKSPACE: ClassVar[int] = ...
    SD_CARD: ClassVar[int] = ...
    NEW_LINE: ClassVar[int] = ...
    DUMMY: ClassVar[int] = ...


class _C_Pointer_type(TypedDict, total=False):
    ptr_val: Any = ...
    str_val: Union[str, bytearray, bytes, List[int]] = ...
    int_val: int = ...
    uint_val: int = ...


class C_Pointer(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _C_Pointer_type) -> "C_Pointer":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def ptr_val(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @ptr_val.setter
    def ptr_val(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def str_val(self) -> Union[str, bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @str_val.setter
    def str_val(self, value: Union[str, bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def int_val(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @int_val.setter
    def int_val(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def uint_val(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @uint_val.setter
    def uint_val(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _color_t_type(TypedDict, total=False):
    blue: int = ...
    green: int = ...
    red: int = ...


class color_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _color_t_type) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def to_int(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def eq(self, c2: "color_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def mix(self, c2: "color_t", mix: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def brightness(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def to_32(self, opa: "opa_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...

    def to_u16(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def to_u32(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def lighten(self, lvl: "opa_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def darken(self, lvl: "opa_t", /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def to_hsv(self, /) -> "color_hsv_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def blue(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @blue.setter
    def blue(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def green(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @green.setter
    def green(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def red(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @red.setter
    def red(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _grad_dsc_t_type(TypedDict, total=False):
    stops: List["gradient_stop_t"] = ...
    stops_count: int = ...
    dir: "grad_dir_t" = ...


class grad_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _grad_dsc_t_type) -> "grad_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def gradient_color_calculate(
        self,
        range: int,
        frac: int,
        color_out: "grad_color_t",
        opa_out: "opa_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def gradient_get(self, w: int, h: int, /) -> "grad_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def stops(self) -> List["gradient_stop_t"]:
        """
        No Docstrings Yet
        """
        ...

    @stops.setter
    def stops(self, value: List["gradient_stop_t"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def stops_count(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @stops_count.setter
    def stops_count(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dir(self) -> "grad_dir_t":
        """
        No Docstrings Yet
        """
        ...

    @dir.setter
    def dir(self, value: "grad_dir_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _gradient_stop_t_type(TypedDict, total=False):
    color: "color_t" = ...
    opa: "opa_t" = ...
    frac: int = ...


class gradient_stop_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _gradient_stop_t_type) -> "gradient_stop_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def frac(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @frac.setter
    def frac(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _font_t_type(TypedDict, total=False):
    get_glyph_dsc: Callable = ...
    get_glyph_bitmap: Callable = ...
    release_glyph: Callable = ...
    line_height: int = ...
    base_line: int = ...
    subpx: int = ...
    kerning: int = ...
    underline_position: int = ...
    underline_thickness: int = ...
    dsc: Any = ...
    fallback: "font_t" = ...
    user_data: Any = ...


class font_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _font_t_type) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_line_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_glyph_dsc(
        self,
        arg0: "font_glyph_dsc_t",
        letter: int,
        letter_next: int,
        /
    ) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_glyph_width(self, letter: int, letter_next: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def set_kerning(self, kerning: "font_kerning_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_glyph_dsc_fmt_txt(
        self,
        arg0: "font_glyph_dsc_t",
        letter: int,
        letter_next: int,
        /
    ) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @property
    def get_glyph_dsc(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @get_glyph_dsc.setter
    def get_glyph_dsc(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def get_glyph_bitmap(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @get_glyph_bitmap.setter
    def get_glyph_bitmap(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def release_glyph(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @release_glyph.setter
    def release_glyph(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def line_height(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @line_height.setter
    def line_height(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base_line(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @base_line.setter
    def base_line(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def subpx(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @subpx.setter
    def subpx(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def kerning(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @kerning.setter
    def kerning(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def underline_position(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @underline_position.setter
    def underline_position(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def underline_thickness(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @underline_thickness.setter
    def underline_thickness(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @dsc.setter
    def dsc(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def fallback(self) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    @fallback.setter
    def fallback(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _font_glyph_dsc_t_type(TypedDict, total=False):
    resolved_font: "font_t" = ...
    adv_w: int = ...
    box_w: int = ...
    box_h: int = ...
    ofs_x: int = ...
    ofs_y: int = ...
    format: "font_glyph_format_t" = ...
    is_placeholder: int = ...
    glyph_index: int = ...
    entry: "cache_entry_t" = ...


class font_glyph_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _font_glyph_dsc_t_type) -> "font_glyph_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_glyph_bitmap(self, arg0: int, arg1: "draw_buf_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_bitmap_fmt_txt(self, arg0: int, arg1: "draw_buf_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @property
    def resolved_font(self) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    @resolved_font.setter
    def resolved_font(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def adv_w(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @adv_w.setter
    def adv_w(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def box_w(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @box_w.setter
    def box_w(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def box_h(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @box_h.setter
    def box_h(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @ofs_x.setter
    def ofs_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @ofs_y.setter
    def ofs_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def format(self) -> "font_glyph_format_t":
        """
        No Docstrings Yet
        """
        ...

    @format.setter
    def format(self, value: "font_glyph_format_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def is_placeholder(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @is_placeholder.setter
    def is_placeholder(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def glyph_index(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @glyph_index.setter
    def glyph_index(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def entry(self) -> "cache_entry_t":
        """
        No Docstrings Yet
        """
        ...

    @entry.setter
    def entry(self, value: "cache_entry_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _cache_entry_t_type(TypedDict, total=False):
    ...


class cache_entry_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _cache_entry_t_type) -> "cache_entry_t":
        """
        No Docstrings Yet
        """
        ...

    def get_ref(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_node_size(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def is_invalid(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_cache(self, /) -> "cache_t":
        """
        No Docstrings Yet
        """
        ...

    def init(self, cache: "cache_t", node_size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_buf_t_type(TypedDict, total=False):
    header: "image" = ...
    data_size: int = ...
    data: Union[bytearray, bytes, List[int]] = ...
    unaligned_data: Any = ...


class draw_buf_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_buf_t_type) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def has_flag(self, flag: "image", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_flag(self, flag: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def clear_flag(self, flag: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def from_image(self, img: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def to_image(self, img: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def invalidate_cache(self, area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def clear(self, a: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def copy(
        self,
        dest_area: "area_t",
        src: "draw_buf_t",
        src_area: "area_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def init(
        self,
        w: int,
        h: int,
        cf: "color_format_t",
        stride: int,
        data: Any,
        data_size: int,
        /
    ) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def dup(self, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    def reshape(
        self,
        cf: "color_format_t",
        w: int,
        h: int,
        stride: int,
        /
    ) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    def destroy(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def goto_xy(self, x: int, y: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def adjust_stride(self, stride: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def premultiply(self, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def set_palette(self, index: int, color: "color32_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def header(self) -> "image":
        """
        No Docstrings Yet
        """
        ...

    @header.setter
    def header(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def data_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @data_size.setter
    def data_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def data(self) -> Union[bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @data.setter
    def data(self, value: Union[bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def unaligned_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @unaligned_data.setter
    def unaligned_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _color_filter_dsc_t_type(TypedDict, total=False):
    filter_cb: Callable = ...
    user_data: Any = ...


class color_filter_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _color_filter_dsc_t_type) -> "color_filter_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def filter_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @filter_cb.setter
    def filter_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _anim_t_type(TypedDict, total=False):
    var: Any = ...
    exec_cb: Callable = ...
    custom_exec_cb: Callable = ...
    start_cb: Callable = ...
    completed_cb: Callable = ...
    deleted_cb: Callable = ...
    get_value_cb: Callable = ...
    user_data: Any = ...
    path_cb: Callable = ...
    start_value: int = ...
    current_value: int = ...
    end_value: int = ...
    duration: int = ...
    act_time: int = ...
    playback_delay: int = ...
    playback_duration: int = ...
    repeat_delay: int = ...
    repeat_cnt: int = ...
    parameter: "anim_parameter_t" = ...
    early_apply: int = ...
    last_timer_run: int = ...
    playback_now: int = ...
    run_round: int = ...
    start_cb_called: int = ...


class anim_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _anim_t_type) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def set_var(self, var: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_exec_cb(self, exec_cb: "anim_exec_xcb_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_duration(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_time(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_delay(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_values(self, start: int, end: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_custom_exec_cb(self, exec_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_path_cb(self, path_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_start_cb(self, start_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_get_value_cb(self, get_value_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_completed_cb(self, completed_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_deleted_cb(self, deleted_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_playback_duration(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_playback_time(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_playback_delay(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_repeat_count(self, cnt: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_repeat_delay(self, duration: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_early_apply(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_user_data(self, var: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bezier3_param(self, x1: int, y1: int, x2: int, y2: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_delay(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_time(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_repeat_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def custom_delete(self, exec_cb: Callable, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def custom_get(self, exec_cb: Callable, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def start(self, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...

    def get_playtime(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_linear(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_ease_in(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_ease_out(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_ease_in_out(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_overshoot(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_bounce(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_step(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def path_custom_bezier3(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    @property
    def var(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @var.setter
    def var(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def exec_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @exec_cb.setter
    def exec_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def custom_exec_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @custom_exec_cb.setter
    def custom_exec_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @start_cb.setter
    def start_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def completed_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @completed_cb.setter
    def completed_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def deleted_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @deleted_cb.setter
    def deleted_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def get_value_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @get_value_cb.setter
    def get_value_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def path_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @path_cb.setter
    def path_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_value(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @start_value.setter
    def start_value(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def current_value(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @current_value.setter
    def current_value(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_value(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @end_value.setter
    def end_value(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def duration(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @duration.setter
    def duration(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def act_time(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @act_time.setter
    def act_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def playback_delay(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @playback_delay.setter
    def playback_delay(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def playback_duration(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @playback_duration.setter
    def playback_duration(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def repeat_delay(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @repeat_delay.setter
    def repeat_delay(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def repeat_cnt(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @repeat_cnt.setter
    def repeat_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def parameter(self) -> "anim_parameter_t":
        """
        No Docstrings Yet
        """
        ...

    @parameter.setter
    def parameter(self, value: "anim_parameter_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def early_apply(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @early_apply.setter
    def early_apply(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_timer_run(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @last_timer_run.setter
    def last_timer_run(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def playback_now(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @playback_now.setter
    def playback_now(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def run_round(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @run_round.setter
    def run_round(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_cb_called(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @start_cb_called.setter
    def start_cb_called(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _anim_parameter_t_type(TypedDict, total=False):
    bezier3: "anim_bezier3_para_t" = ...


class anim_parameter_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _anim_parameter_t_type) -> "anim_parameter_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def bezier3(self) -> "anim_bezier3_para_t":
        """
        No Docstrings Yet
        """
        ...

    @bezier3.setter
    def bezier3(self, value: "anim_bezier3_para_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _anim_bezier3_para_t_type(TypedDict, total=False):
    x1: int = ...
    y1: int = ...
    x2: int = ...
    y2: int = ...


class anim_bezier3_para_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _anim_bezier3_para_t_type
    ) -> "anim_bezier3_para_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def x1(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @x1.setter
    def x1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y1(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y1.setter
    def y1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def x2(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @x2.setter
    def x2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y2(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y2.setter
    def y2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _style_transition_dsc_t_type(TypedDict, total=False):
    props: "style_prop_t" = ...
    user_data: Any = ...
    path_xcb: Callable = ...
    time: int = ...
    delay: int = ...


class style_transition_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _style_transition_dsc_t_type
    ) -> "style_transition_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(
        self,
        props: List["style_prop_t"],
        path_cb: Callable,
        time: int,
        delay: int,
        tr: "style_transition_dsc_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def props(self) -> "style_prop_t":
        """
        No Docstrings Yet
        """
        ...

    @props.setter
    def props(self, value: "style_prop_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def path_xcb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @path_xcb.setter
    def path_xcb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def time(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @time.setter
    def time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def delay(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @delay.setter
    def delay(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _display_t_type(TypedDict, total=False):
    hor_res: int = ...
    ver_res: int = ...
    physical_hor_res: int = ...
    physical_ver_res: int = ...
    offset_x: int = ...
    offset_y: int = ...
    dpi: int = ...
    buf_1: "draw_buf_t" = ...
    buf_2: "draw_buf_t" = ...
    buf_act: "draw_buf_t" = ...
    flush_cb: Callable = ...
    flush_wait_cb: Callable = ...
    flushing: int = ...
    flushing_last: int = ...
    last_area: int = ...
    last_part: int = ...
    render_mode: "display_render_mode_t" = ...
    antialiasing: int = ...
    rendering_in_progress: int = ...
    color_format: "color_format_t" = ...
    inv_areas: List["area_t"] = ...
    inv_area_joined: List[int] = ...
    inv_p: int = ...
    inv_en_cnt: int = ...
    sync_areas: "ll_t" = ...
    _static_buf1: "draw_buf_t" = ...
    _static_buf2: "draw_buf_t" = ...
    layer_head: "layer_t" = ...
    layer_init: Callable = ...
    layer_deinit: Callable = ...
    screens: List["obj"] = ...
    act_scr: "obj" = ...
    prev_scr: "obj" = ...
    scr_to_load: "obj" = ...
    bottom_layer: "obj" = ...
    top_layer: "obj" = ...
    sys_layer: "obj" = ...
    screen_cnt: int = ...
    draw_prev_over_act: int = ...
    del_prev: int = ...
    driver_data: Any = ...
    user_data: Any = ...
    event_list: "event_list_t" = ...
    sw_rotate: int = ...
    rotation: int = ...
    theme: "theme_t" = ...
    refr_timer: "timer_t" = ...
    last_activity_time: int = ...
    refreshed_area: "area_t" = ...


class display_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _display_t_type) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def dpx(self, n: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def draw_dispatch_layer(self, layer: "layer_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_default(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_next(self, /) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    def set_resolution(self, hor_res: int, ver_res: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_physical_resolution(self, hor_res: int, ver_res: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_offset(self, hor_res: int, ver_res: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_rotation(self, rotation: "display_rotation_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_dpi(self, dpi: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_horizontal_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_vertical_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_physical_horizontal_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_physical_vertical_resolution(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_offset_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_offset_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_rotation(self, /) -> "display_rotation_t":
        """
        No Docstrings Yet
        """
        ...

    def get_dpi(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def set_buffers(
        self,
        buf1: Any,
        buf2: Any,
        buf_size: int,
        render_mode: "display_render_mode_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_draw_buffers(
        self,
        buf1: "draw_buf_t",
        buf2: "draw_buf_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_render_mode(self, render_mode: "display_render_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flush_cb(self, flush_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flush_wait_cb(self, wait_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_color_format(self, color_format: "color_format_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_color_format(self, /) -> "color_format_t":
        """
        No Docstrings Yet
        """
        ...

    def set_antialiasing(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_antialiasing(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def flush_ready(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def flush_is_last(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def is_double_buffered(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_screen_active(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_screen_prev(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_layer_top(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_layer_sys(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_layer_bottom(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def add_event_cb(
        self,
        event_cb: Callable,
        filter: "event_code_t",
        disp: "display_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_event_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_event_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def delete_event(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def remove_event_cb_with_user_data(
        self,
        event_cb: Callable,
        disp: "display_t",
        /
    ) -> int:
        """
        No Docstrings Yet
        """
        ...

    def send_event(self, code: "event_code_t", param: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def set_theme(self, th: "theme_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_theme(self, /) -> "theme_t":
        """
        No Docstrings Yet
        """
        ...

    def get_inactive_time(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def trigger_activity(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def enable_invalidation(self, en: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def is_invalidation_enabled(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_refr_timer(self, /) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    def delete_refr_timer(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_user_data(self, disp: "display_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_driver_data(self, disp: "display_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_driver_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_buf_active(self, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def hor_res(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @hor_res.setter
    def hor_res(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ver_res(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @ver_res.setter
    def ver_res(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def physical_hor_res(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @physical_hor_res.setter
    def physical_hor_res(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def physical_ver_res(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @physical_ver_res.setter
    def physical_ver_res(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def offset_x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @offset_x.setter
    def offset_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def offset_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @offset_y.setter
    def offset_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dpi(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @dpi.setter
    def dpi(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buf_1(self) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @buf_1.setter
    def buf_1(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buf_2(self) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @buf_2.setter
    def buf_2(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buf_act(self) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @buf_act.setter
    def buf_act(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flush_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @flush_cb.setter
    def flush_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flush_wait_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @flush_wait_cb.setter
    def flush_wait_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flushing(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @flushing.setter
    def flushing(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flushing_last(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @flushing_last.setter
    def flushing_last(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_area(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @last_area.setter
    def last_area(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_part(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @last_part.setter
    def last_part(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def render_mode(self) -> "display_render_mode_t":
        """
        No Docstrings Yet
        """
        ...

    @render_mode.setter
    def render_mode(self, value: "display_render_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def antialiasing(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @antialiasing.setter
    def antialiasing(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rendering_in_progress(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @rendering_in_progress.setter
    def rendering_in_progress(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color_format(self) -> "color_format_t":
        """
        No Docstrings Yet
        """
        ...

    @color_format.setter
    def color_format(self, value: "color_format_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def inv_areas(self) -> List["area_t"]:
        """
        No Docstrings Yet
        """
        ...

    @inv_areas.setter
    def inv_areas(self, value: List["area_t"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def inv_area_joined(self) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    @inv_area_joined.setter
    def inv_area_joined(self, value: List[int]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def inv_p(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @inv_p.setter
    def inv_p(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def inv_en_cnt(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @inv_en_cnt.setter
    def inv_en_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sync_areas(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @sync_areas.setter
    def sync_areas(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def _static_buf1(self) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @_static_buf1.setter
    def _static_buf1(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def _static_buf2(self) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @_static_buf2.setter
    def _static_buf2(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layer_head(self) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    @layer_head.setter
    def layer_head(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layer_init(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @layer_init.setter
    def layer_init(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layer_deinit(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @layer_deinit.setter
    def layer_deinit(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def screens(self) -> List["obj"]:
        """
        No Docstrings Yet
        """
        ...

    @screens.setter
    def screens(self, value: List["obj"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def act_scr(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @act_scr.setter
    def act_scr(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def prev_scr(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @prev_scr.setter
    def prev_scr(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scr_to_load(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @scr_to_load.setter
    def scr_to_load(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bottom_layer(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @bottom_layer.setter
    def bottom_layer(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def top_layer(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @top_layer.setter
    def top_layer(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sys_layer(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @sys_layer.setter
    def sys_layer(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def screen_cnt(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @screen_cnt.setter
    def screen_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def draw_prev_over_act(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @draw_prev_over_act.setter
    def draw_prev_over_act(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def del_prev(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @del_prev.setter
    def del_prev(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def driver_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @driver_data.setter
    def driver_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def event_list(self) -> "event_list_t":
        """
        No Docstrings Yet
        """
        ...

    @event_list.setter
    def event_list(self, value: "event_list_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sw_rotate(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @sw_rotate.setter
    def sw_rotate(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rotation(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @rotation.setter
    def rotation(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def theme(self) -> "theme_t":
        """
        No Docstrings Yet
        """
        ...

    @theme.setter
    def theme(self, value: "theme_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def refr_timer(self) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    @refr_timer.setter
    def refr_timer(self, value: "timer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_activity_time(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @last_activity_time.setter
    def last_activity_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def refreshed_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @refreshed_area.setter
    def refreshed_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _area_t_type(TypedDict, total=False):
    x1: int = ...
    y1: int = ...
    x2: int = ...
    y2: int = ...


class area_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _area_t_type) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def copy(self, src: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def set(self, x1: int, y1: int, x2: int, y2: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_width(self, w: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_height(self, w: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_size(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def increase(self, w_extra: int, h_extra: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def move(self, w_extra: int, h_extra: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def align(
        self,
        to_align: "area_t",
        align: "align_t",
        ofs_x: int,
        ofs_y: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def x1(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @x1.setter
    def x1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y1(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y1.setter
    def y1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def x2(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @x2.setter
    def x2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y2(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y2.setter
    def y2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _ll_t_type(TypedDict, total=False):
    n_size: int = ...
    head: "ll_node_t" = ...
    tail: "ll_node_t" = ...


class ll_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _ll_t_type) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def n_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @n_size.setter
    def n_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def head(self) -> "ll_node_t":
        """
        No Docstrings Yet
        """
        ...

    @head.setter
    def head(self, value: "ll_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tail(self) -> "ll_node_t":
        """
        No Docstrings Yet
        """
        ...

    @tail.setter
    def tail(self, value: "ll_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _layer_t_type(TypedDict, total=False):
    draw_buf: "draw_buf_t" = ...
    buf_area: "area_t" = ...
    color_format: "color_format_t" = ...
    _clip_area: "area_t" = ...
    draw_task_head: "draw_task_t" = ...
    parent: "layer_t" = ...
    next: "layer_t" = ...
    all_tasks_added: bool = ...
    user_data: Any = ...


class layer_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _layer_t_type) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def draw_buf(self) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @draw_buf.setter
    def draw_buf(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buf_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @buf_area.setter
    def buf_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color_format(self) -> "color_format_t":
        """
        No Docstrings Yet
        """
        ...

    @color_format.setter
    def color_format(self, value: "color_format_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def _clip_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @_clip_area.setter
    def _clip_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def draw_task_head(self) -> "draw_task_t":
        """
        No Docstrings Yet
        """
        ...

    @draw_task_head.setter
    def draw_task_head(self, value: "draw_task_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def parent(self) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    @parent.setter
    def parent(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def next(self) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    @next.setter
    def next(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def all_tasks_added(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @all_tasks_added.setter
    def all_tasks_added(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_task_t_type(TypedDict, total=False):
    next: "draw_task_t" = ...
    type: "draw_task_type_t" = ...
    area: "area_t" = ...
    _real_area: "area_t" = ...
    clip_area_original: "area_t" = ...
    clip_area: "area_t" = ...
    state: int = ...
    draw_dsc: Any = ...
    preferred_draw_unit_id: int = ...
    preference_score: int = ...


class draw_task_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_task_t_type) -> "draw_task_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_dependent_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_fill_dsc(self, /) -> "draw_fill_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_border_dsc(self, /) -> "draw_border_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_box_shadow_dsc(self, /) -> "draw_box_shadow_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_label_dsc(self, /) -> "draw_label_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_image_dsc(self, /) -> "draw_image_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_arc_dsc(self, /) -> "draw_arc_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_line_dsc(self, /) -> "draw_line_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_triangle_dsc(self, /) -> "draw_triangle_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_mask_rect_dsc(self, /) -> "draw_mask_rect_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def next(self) -> "draw_task_t":
        """
        No Docstrings Yet
        """
        ...

    @next.setter
    def next(self, value: "draw_task_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def type(self) -> "draw_task_type_t":
        """
        No Docstrings Yet
        """
        ...

    @type.setter
    def type(self, value: "draw_task_type_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @area.setter
    def area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def _real_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @_real_area.setter
    def _real_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def clip_area_original(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @clip_area_original.setter
    def clip_area_original(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def clip_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @clip_area.setter
    def clip_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def state(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @state.setter
    def state(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def draw_dsc(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @draw_dsc.setter
    def draw_dsc(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def preferred_draw_unit_id(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @preferred_draw_unit_id.setter
    def preferred_draw_unit_id(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def preference_score(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @preference_score.setter
    def preference_score(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _array_t_type(TypedDict, total=False):
    data: Union[bytearray, bytes, List[int]] = ...
    size: int = ...
    capacity: int = ...
    element_size: int = ...


class array_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _array_t_type) -> "array_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def size(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def capacity(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def is_empty(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def is_full(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def clear(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def front(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def back(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def init(self, capacity: int, element_size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def resize(self, new_capacity: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def deinit(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def copy(self, source: "array_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def remove(self, index: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def erase(self, start: int, end: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def concat(self, other: "array_t", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def push_back(self, element: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def assign(self, index: int, value: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def at(self, index: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def event_send(self, e: "event_t", preprocess: bool, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def event_add(
        self,
        cb: Callable,
        filter: "event_code_t",
        list: "event_list_t",
        /
    ) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def event_remove_dsc(self, dsc: "event_dsc_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def event_get_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def event_get_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def event_remove(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def event_remove_all(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def data(self) -> Union[bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @data.setter
    def data(self, value: Union[bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def capacity(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @capacity.setter
    def capacity(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def element_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @element_size.setter
    def element_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _theme_t_type(TypedDict, total=False):
    apply_cb: Callable = ...
    parent: "theme_t" = ...
    user_data: Any = ...
    disp: "display_t" = ...
    color_primary: "color_t" = ...
    color_secondary: "color_t" = ...
    font_small: "font_t" = ...
    font_normal: "font_t" = ...
    font_large: "font_t" = ...
    flags: int = ...


class theme_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _theme_t_type) -> "theme_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def set_parent(self, parent: "theme_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_apply_cb(self, apply_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def apply_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @apply_cb.setter
    def apply_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def parent(self) -> "theme_t":
        """
        No Docstrings Yet
        """
        ...

    @parent.setter
    def parent(self, value: "theme_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def disp(self) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    @disp.setter
    def disp(self, value: "display_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color_primary(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color_primary.setter
    def color_primary(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color_secondary(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color_secondary.setter
    def color_secondary(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def font_small(self) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    @font_small.setter
    def font_small(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def font_normal(self) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    @font_normal.setter
    def font_normal(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def font_large(self) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    @font_large.setter
    def font_large(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flags(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @flags.setter
    def flags(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _timer_t_type(TypedDict, total=False):
    period: int = ...
    last_run: int = ...
    timer_cb: Callable = ...
    user_data: Any = ...
    repeat_count: int = ...
    paused: int = ...
    auto_delete: int = ...


class timer_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _timer_t_type) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_paused(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def pause(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def resume(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_cb(self, timer_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_period(self, period: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def ready(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_repeat_count(self, repeat_count: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_auto_delete(self, auto_delete: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_user_data(self, timer: "timer_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def reset(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_next(self, /) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def period(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @period.setter
    def period(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_run(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @last_run.setter
    def last_run(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def timer_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @timer_cb.setter
    def timer_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def repeat_count(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @repeat_count.setter
    def repeat_count(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def paused(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @paused.setter
    def paused(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def auto_delete(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @auto_delete.setter
    def auto_delete(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _event_t_type(TypedDict, total=False):
    current_target: Any = ...
    original_target: Any = ...
    code: "event_code_t" = ...
    user_data: Any = ...
    param: Any = ...
    prev: "event_t" = ...
    deleted: int = ...
    stop_processing: int = ...
    stop_bubbling: int = ...


class event_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _event_t_type) -> "event_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_target(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_current_target(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_code(self, /) -> "event_code_t":
        """
        No Docstrings Yet
        """
        ...

    def get_param(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def stop_bubbling(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def stop_processing(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_current_target_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_target_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_indev(self, /) -> "indev_t":
        """
        No Docstrings Yet
        """
        ...

    def get_layer(self, /) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    def get_old_size(self, /) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    def get_key(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_rotary_diff(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_anim(self, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...

    def set_ext_draw_size(self, size: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_self_size_info(self, /) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    def get_hit_test_info(self, /) -> "hit_test_info_t":
        """
        No Docstrings Yet
        """
        ...

    def get_cover_area(self, /) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    def set_cover_res(self, res: "cover_res_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_draw_task(self, /) -> "draw_task_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def current_target(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @current_target.setter
    def current_target(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def original_target(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @original_target.setter
    def original_target(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def code(self) -> "event_code_t":
        """
        No Docstrings Yet
        """
        ...

    @code.setter
    def code(self, value: "event_code_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def param(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @param.setter
    def param(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def prev(self) -> "event_t":
        """
        No Docstrings Yet
        """
        ...

    @prev.setter
    def prev(self, value: "event_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def deleted(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @deleted.setter
    def deleted(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def stop_processing(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @stop_processing.setter
    def stop_processing(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def stop_bubbling(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @stop_bubbling.setter
    def stop_bubbling(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _point_t_type(TypedDict, total=False):
    x: int = ...
    y: int = ...


class point_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _point_t_type) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def to_precise(self, /) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...

    def set(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def swap(self, p2: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def transform(
        self,
        angle: int,
        scale_x: int,
        scale_y: int,
        pivot: "point_t",
        zoom_first: bool,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def array_transform(
        self,
        count: int,
        angle: int,
        scale_x: int,
        scale_y: int,
        pivot: "point_t",
        zoom_first: bool,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @x.setter
    def x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y.setter
    def y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _style_t_type(TypedDict, total=False):
    values_and_props: Any = ...
    has_group: int = ...
    prop_cnt: int = ...


class style_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _style_t_type) -> "style_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def is_const(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_prop_inlined(
        self,
        prop: "style_prop_t",
        value: "style_value_t",
        /
    ) -> "style_res_t":
        """
        No Docstrings Yet
        """
        ...

    def set_size(self, width: int, height: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_all(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_hor(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_ver(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_gap(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_scale(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def reset(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def remove_prop(self, prop: "style_prop_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_prop(self, prop: "style_prop_t", value: "style_value_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_prop(
        self,
        prop: "style_prop_t",
        value: "style_value_t",
        /
    ) -> "style_res_t":
        """
        No Docstrings Yet
        """
        ...

    def is_empty(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_min_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_max_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_min_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_max_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_length(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_align(self, value: "align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_height(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_translate_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_translate_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_scale_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_scale_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_rotation(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_pivot_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_pivot_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_skew_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transform_skew_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_top(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_bottom(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_left(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_right(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_row(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pad_column(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_margin_top(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_margin_bottom(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_margin_left(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_margin_right(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_grad_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_grad_dir(self, value: "grad_dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_main_stop(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_grad_stop(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_main_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_grad_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_grad(self, value: "grad_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_image_src(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_image_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_image_recolor(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_image_recolor_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_image_tiled(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_border_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_border_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_border_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_border_side(self, value: "border_side_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_border_post(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_outline_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_outline_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_outline_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_outline_pad(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_shadow_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_shadow_offset_x(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_shadow_offset_y(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_shadow_spread(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_shadow_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_shadow_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_image_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_image_recolor(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_image_recolor_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_line_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_line_dash_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_line_dash_gap(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_line_rounded(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_line_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_line_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_arc_width(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_arc_rounded(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_arc_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_arc_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_arc_image_src(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_color(self, value: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_font(self, value: "font_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_letter_space(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_line_space(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_decor(self, value: "text_decor_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_align(self, value: "text_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_radius(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_clip_corner(self, value: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_opa_layered(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_color_filter_dsc(self, value: "color_filter_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_color_filter_opa(self, value: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_anim(self, value: "anim_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_anim_duration(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_transition(self, value: "style_transition_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_blend_mode(self, value: "blend_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_layout(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_base_dir(self, value: "base_dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bitmap_mask_src(self, value: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_rotary_sensitivity(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_flow(self, value: "flex_flow_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_main_place(self, value: "flex_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_cross_place(self, value: "flex_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_track_place(self, value: "flex_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_grow(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_column_dsc_array(self, value: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_column_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_row_dsc_array(self, value: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_row_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_cell_column_pos(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_cell_x_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_cell_column_span(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_cell_row_pos(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_cell_y_align(self, value: "grid_align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_cell_row_span(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def values_and_props(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @values_and_props.setter
    def values_and_props(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def has_group(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @has_group.setter
    def has_group(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def prop_cnt(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @prop_cnt.setter
    def prop_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _style_value_t_type(TypedDict, total=False):
    num: int = ...
    ptr: Any = ...
    color: "color_t" = ...


class style_value_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _style_value_t_type) -> "style_value_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def num(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @num.setter
    def num(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ptr(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @ptr.setter
    def ptr(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_rect_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    bg_opa: "opa_t" = ...
    bg_color: "color_t" = ...
    bg_grad: "grad_dsc_t" = ...
    bg_image_src: Any = ...
    bg_image_symbol_font: Any = ...
    bg_image_recolor: "color_t" = ...
    bg_image_opa: "opa_t" = ...
    bg_image_recolor_opa: "opa_t" = ...
    bg_image_tiled: int = ...
    border_color: "color_t" = ...
    border_width: int = ...
    border_opa: "opa_t" = ...
    border_side: "border_side_t" = ...
    border_post: int = ...
    outline_color: "color_t" = ...
    outline_width: int = ...
    outline_pad: int = ...
    outline_opa: "opa_t" = ...
    shadow_color: "color_t" = ...
    shadow_width: int = ...
    shadow_offset_x: int = ...
    shadow_offset_y: int = ...
    shadow_spread: int = ...
    shadow_opa: "opa_t" = ...


class draw_rect_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_rect_dsc_t_type) -> "draw_rect_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_opa.setter
    def bg_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_color.setter
    def bg_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_grad(self) -> "grad_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_grad.setter
    def bg_grad(self, value: "grad_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_src(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @bg_image_src.setter
    def bg_image_src(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_symbol_font(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @bg_image_symbol_font.setter
    def bg_image_symbol_font(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_recolor(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_image_recolor.setter
    def bg_image_recolor(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_image_opa.setter
    def bg_image_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_recolor_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_image_recolor_opa.setter
    def bg_image_recolor_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_image_tiled(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @bg_image_tiled.setter
    def bg_image_tiled(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @border_color.setter
    def border_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @border_width.setter
    def border_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @border_opa.setter
    def border_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_side(self) -> "border_side_t":
        """
        No Docstrings Yet
        """
        ...

    @border_side.setter
    def border_side(self, value: "border_side_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def border_post(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @border_post.setter
    def border_post(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @outline_color.setter
    def outline_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @outline_width.setter
    def outline_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_pad(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @outline_pad.setter
    def outline_pad(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outline_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @outline_opa.setter
    def outline_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @shadow_color.setter
    def shadow_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @shadow_width.setter
    def shadow_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_offset_x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @shadow_offset_x.setter
    def shadow_offset_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_offset_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @shadow_offset_y.setter
    def shadow_offset_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_spread(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @shadow_spread.setter
    def shadow_spread(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def shadow_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @shadow_opa.setter
    def shadow_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_dsc_base_t_type(TypedDict, total=False):
    obj: "obj" = ...
    part: int = ...
    id1: int = ...
    id2: int = ...
    layer: "layer_t" = ...
    dsc_size: int = ...
    user_data: Any = ...


class draw_dsc_base_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_dsc_base_t_type) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def obj(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @obj.setter
    def obj(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def part(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @part.setter
    def part(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def id1(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @id1.setter
    def id1(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def id2(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @id2.setter
    def id2(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layer(self) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    @layer.setter
    def layer(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @dsc_size.setter
    def dsc_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_label_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    text: Union[str, bytearray, bytes, List[int]] = ...
    font: "font_t" = ...
    sel_start: int = ...
    sel_end: int = ...
    color: "color_t" = ...
    sel_color: "color_t" = ...
    sel_bg_color: "color_t" = ...
    line_space: int = ...
    letter_space: int = ...
    ofs_x: int = ...
    ofs_y: int = ...
    opa: "opa_t" = ...
    bidi_dir: "base_dir_t" = ...
    align: "text_align_t" = ...
    flag: "text_flag_t" = ...
    decor: "text_decor_t" = ...
    blend_mode: "blend_mode_t" = ...
    text_local: int = ...
    hint: "draw_label_hint_t" = ...


class draw_label_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_label_dsc_t_type) -> "draw_label_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def text(self) -> Union[str, bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @text.setter
    def text(self, value: Union[str, bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def font(self) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    @font.setter
    def font(self, value: "font_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_start(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @sel_start.setter
    def sel_start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_end(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @sel_end.setter
    def sel_end(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @sel_color.setter
    def sel_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sel_bg_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @sel_bg_color.setter
    def sel_bg_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def line_space(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @line_space.setter
    def line_space(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def letter_space(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @letter_space.setter
    def letter_space(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @ofs_x.setter
    def ofs_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @ofs_y.setter
    def ofs_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bidi_dir(self) -> "base_dir_t":
        """
        No Docstrings Yet
        """
        ...

    @bidi_dir.setter
    def bidi_dir(self, value: "base_dir_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def align(self) -> "text_align_t":
        """
        No Docstrings Yet
        """
        ...

    @align.setter
    def align(self, value: "text_align_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flag(self) -> "text_flag_t":
        """
        No Docstrings Yet
        """
        ...

    @flag.setter
    def flag(self, value: "text_flag_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def decor(self) -> "text_decor_t":
        """
        No Docstrings Yet
        """
        ...

    @decor.setter
    def decor(self, value: "text_decor_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blend_mode(self) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def text_local(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @text_local.setter
    def text_local(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def hint(self) -> "draw_label_hint_t":
        """
        No Docstrings Yet
        """
        ...

    @hint.setter
    def hint(self, value: "draw_label_hint_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_label_hint_t_type(TypedDict, total=False):
    line_start: int = ...
    y: int = ...
    coord_y: int = ...


class draw_label_hint_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_label_hint_t_type) -> "draw_label_hint_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def line_start(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @line_start.setter
    def line_start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y.setter
    def y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def coord_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @coord_y.setter
    def coord_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_image_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    src: Any = ...
    header: "image" = ...
    rotation: int = ...
    scale_x: int = ...
    scale_y: int = ...
    skew_x: int = ...
    skew_y: int = ...
    pivot: "point_t" = ...
    recolor: "color_t" = ...
    recolor_opa: "opa_t" = ...
    opa: "opa_t" = ...
    blend_mode: "blend_mode_t" = ...
    antialias: int = ...
    tile: int = ...
    sup: "draw_image_sup_t" = ...
    original_area: "area_t" = ...
    bitmap_mask_src: "image" = ...


class draw_image_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_image_dsc_t_type) -> "draw_image_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def src(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @src.setter
    def src(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def header(self) -> "image":
        """
        No Docstrings Yet
        """
        ...

    @header.setter
    def header(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rotation(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @rotation.setter
    def rotation(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scale_x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @scale_x.setter
    def scale_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scale_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @scale_y.setter
    def scale_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def skew_x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @skew_x.setter
    def skew_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def skew_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @skew_y.setter
    def skew_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pivot(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @pivot.setter
    def pivot(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def recolor(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @recolor.setter
    def recolor(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def recolor_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @recolor_opa.setter
    def recolor_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blend_mode(self) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def antialias(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @antialias.setter
    def antialias(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tile(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @tile.setter
    def tile(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sup(self) -> "draw_image_sup_t":
        """
        No Docstrings Yet
        """
        ...

    @sup.setter
    def sup(self, value: "draw_image_sup_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def original_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @original_area.setter
    def original_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bitmap_mask_src(self) -> "image":
        """
        No Docstrings Yet
        """
        ...

    @bitmap_mask_src.setter
    def bitmap_mask_src(self, value: "image") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_image_sup_t_type(TypedDict, total=False):
    alpha_color: "color_t" = ...
    palette: "color32_t" = ...
    palette_size: int = ...


class draw_image_sup_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_image_sup_t_type) -> "draw_image_sup_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def alpha_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @alpha_color.setter
    def alpha_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def palette(self) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...

    @palette.setter
    def palette(self, value: "color32_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def palette_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @palette_size.setter
    def palette_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _color32_t_type(TypedDict, total=False):
    blue: int = ...
    green: int = ...
    red: int = ...
    alpha: int = ...


class color32_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _color32_t_type) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def eq(self, c2: "color32_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def color_premultiply(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def color_mix32(self, bg: "color32_t", /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def blue(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @blue.setter
    def blue(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def green(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @green.setter
    def green(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def red(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @red.setter
    def red(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def alpha(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @alpha.setter
    def alpha(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_line_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    p1: "point_precise_t" = ...
    p2: "point_precise_t" = ...
    color: "color_t" = ...
    width: int = ...
    dash_width: int = ...
    dash_gap: int = ...
    opa: "opa_t" = ...
    blend_mode: "blend_mode_t" = ...
    round_start: int = ...
    round_end: int = ...
    raw_end: int = ...


class draw_line_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_line_dsc_t_type) -> "draw_line_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def p1(self) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...

    @p1.setter
    def p1(self, value: "point_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def p2(self) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...

    @p2.setter
    def p2(self, value: "point_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dash_width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @dash_width.setter
    def dash_width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dash_gap(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @dash_gap.setter
    def dash_gap(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blend_mode(self) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def round_start(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @round_start.setter
    def round_start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def round_end(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @round_end.setter
    def round_end(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def raw_end(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @raw_end.setter
    def raw_end(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _point_precise_t_type(TypedDict, total=False):
    x: "value_precise_t" = ...
    y: "value_precise_t" = ...


class point_precise_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _point_precise_t_type) -> "point_precise_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def from_precise(self, /) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    def set(self, x: "value_precise_t", y: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def swap(self, p2: "point_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def x(self) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    @x.setter
    def x(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y(self) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    @y.setter
    def y(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_arc_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    color: "color_t" = ...
    width: int = ...
    start_angle: "value_precise_t" = ...
    end_angle: "value_precise_t" = ...
    center: "point_t" = ...
    radius: int = ...
    img_src: Any = ...
    opa: "opa_t" = ...
    rounded: int = ...


class draw_arc_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_arc_dsc_t_type) -> "draw_arc_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_angle(self) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    @start_angle.setter
    def start_angle(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_angle(self) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    @end_angle.setter
    def end_angle(self, value: "value_precise_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def center(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @center.setter
    def center(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def img_src(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @img_src.setter
    def img_src(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rounded(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @rounded.setter
    def rounded(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _event_dsc_t_type(TypedDict, total=False):
    cb: Callable = ...
    user_data: Any = ...
    filter: int = ...


class event_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _event_dsc_t_type) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_cb(self, /) -> "event_cb_t":
        """
        No Docstrings Yet
        """
        ...

    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @cb.setter
    def cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def filter(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @filter.setter
    def filter(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _group_t_type(TypedDict, total=False):
    obj_ll: "ll_t" = ...
    obj_focus: List["obj"] = ...
    focus_cb: Callable = ...
    edge_cb: Callable = ...
    user_data: Any = ...
    frozen: int = ...
    editing: int = ...
    refocus_policy: int = ...
    wrap: int = ...


class group_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _group_t_type) -> "group_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_default(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_obj(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def remove_all_objs(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def focus_next(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def focus_prev(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def focus_freeze(self, arg0: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def send_data(self, c: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def set_focus_cb(self, focus_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_edge_cb(self, edge_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_refocus_policy(self, policy: "group_refocus_policy_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_editing(self, arg0: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_wrap(self, arg0: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_focused(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_focus_cb(self, /) -> "group_focus_cb_t":
        """
        No Docstrings Yet
        """
        ...

    def get_edge_cb(self, /) -> "group_edge_cb_t":
        """
        No Docstrings Yet
        """
        ...

    def get_editing(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_wrap(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_obj_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    @property
    def obj_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @obj_ll.setter
    def obj_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def obj_focus(self) -> List["obj"]:
        """
        No Docstrings Yet
        """
        ...

    @obj_focus.setter
    def obj_focus(self, value: List["obj"]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def focus_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @focus_cb.setter
    def focus_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def edge_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @edge_cb.setter
    def edge_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def frozen(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @frozen.setter
    def frozen(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def editing(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @editing.setter
    def editing(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def refocus_policy(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @refocus_policy.setter
    def refocus_policy(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def wrap(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @wrap.setter
    def wrap(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _observer_t_type(TypedDict, total=False):
    subject: "subject_t" = ...
    cb: Callable = ...
    target: Any = ...
    user_data: Any = ...
    auto_free_user_data: int = ...
    notified: int = ...


class observer_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _observer_t_type) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def get_target_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def remove(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_target(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @property
    def subject(self) -> "subject_t":
        """
        No Docstrings Yet
        """
        ...

    @subject.setter
    def subject(self, value: "subject_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @cb.setter
    def cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def target(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @target.setter
    def target(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def auto_free_user_data(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @auto_free_user_data.setter
    def auto_free_user_data(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def notified(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @notified.setter
    def notified(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _subject_t_type(TypedDict, total=False):
    subs_ll: "ll_t" = ...
    type: int = ...
    size: int = ...
    value: "subject_value_t" = ...
    prev_value: "subject_value_t" = ...
    notify_restart_query: int = ...
    user_data: Any = ...


class subject_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _subject_t_type) -> "subject_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init_int(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_int(self, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_int(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_previous_int(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def init_string(
        self,
        buf: Union[str, bytearray, bytes, List[int]],
        prev_buf: Union[str, bytearray, bytes, List[int]],
        size: int,
        value: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def copy_string(
        self,
        buf: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_string(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_previous_string(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def init_pointer(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pointer(self, value: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_pointer(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_previous_pointer(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def init_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_previous_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def init_group(self, list: "subject_t", list_len: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_group_element(self, index: int, /) -> "subject_t":
        """
        No Docstrings Yet
        """
        ...

    def add_observer(
        self,
        observer_cb: Callable,
        subject: "subject_t",
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    def add_observer_obj(
        self,
        observer_cb: Callable,
        obj: "obj",
        subject: "subject_t",
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    def add_observer_with_target(
        self,
        cb: Callable,
        target: Any,
        subject: "subject_t",
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    def remove_all_obj(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def notify(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def subs_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @subs_ll.setter
    def subs_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def type(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @type.setter
    def type(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def value(self) -> "subject_value_t":
        """
        No Docstrings Yet
        """
        ...

    @value.setter
    def value(self, value: "subject_value_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def prev_value(self) -> "subject_value_t":
        """
        No Docstrings Yet
        """
        ...

    @prev_value.setter
    def prev_value(self, value: "subject_value_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def notify_restart_query(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @notify_restart_query.setter
    def notify_restart_query(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _subject_value_t_type(TypedDict, total=False):
    num: int = ...
    pointer: Any = ...
    color: "color_t" = ...


class subject_value_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _subject_value_t_type) -> "subject_value_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def num(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @num.setter
    def num(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pointer(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @pointer.setter
    def pointer(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _cache_t_type(TypedDict, total=False):
    clz: "cache_class_t" = ...
    node_size: int = ...
    max_size: int = ...
    size: int = ...
    ops: "cache_ops_t" = ...
    lock: "mutex_t" = ...


class cache_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _cache_t_type) -> "cache_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def destroy(self, cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def acquire(self, key: Any, cache: "cache_t", /) -> "cache_entry_t":
        """
        No Docstrings Yet
        """
        ...

    def acquire_or_create(
        self,
        key: Any,
        cache: "cache_t",
        /
    ) -> "cache_entry_t":
        """
        No Docstrings Yet
        """
        ...

    def add(self, key: Any, cache: "cache_t", /) -> "cache_entry_t":
        """
        No Docstrings Yet
        """
        ...

    def release(self, entry: "cache_entry_t", cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def reserve(self, reserved_size: int, cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def drop(self, key: Any, cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def drop_all(self, cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def evict_one(self, cache: "cache_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_max_size(self, max_size: int, cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_max_size(self, cache: "cache_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_size(self, cache: "cache_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_free_size(self, cache: "cache_t", /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def set_compare_cb(
        self,
        compare_cb: "cache_compare_cb_t",
        cache: "cache_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_create_cb(self, alloc_cb: Callable, cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_free_cb(self, free_cb: Callable, cache: "cache_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def clz(self) -> "cache_class_t":
        """
        No Docstrings Yet
        """
        ...

    @clz.setter
    def clz(self, value: "cache_class_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def node_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @node_size.setter
    def node_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def max_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @max_size.setter
    def max_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ops(self) -> "cache_ops_t":
        """
        No Docstrings Yet
        """
        ...

    @ops.setter
    def ops(self, value: "cache_ops_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def lock(self) -> "mutex_t":
        """
        No Docstrings Yet
        """
        ...

    @lock.setter
    def lock(self, value: "mutex_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _cache_class_t_type(TypedDict, total=False):
    alloc_cb: Callable = ...
    init_cb: Callable = ...
    destroy_cb: Callable = ...
    get_cb: Callable = ...
    add_cb: Callable = ...
    remove_cb: Callable = ...
    drop_cb: Callable = ...
    drop_all_cb: Callable = ...
    get_victim_cb: Callable = ...
    reserve_cond_cb: Callable = ...


class cache_class_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _cache_class_t_type) -> "cache_class_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def create(
        self,
        node_size: int,
        max_size: int,
        ops: "cache_ops_t",
        /
    ) -> "cache_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def alloc_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @alloc_cb.setter
    def alloc_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def init_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @init_cb.setter
    def init_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def destroy_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @destroy_cb.setter
    def destroy_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def get_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @get_cb.setter
    def get_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def add_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @add_cb.setter
    def add_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def remove_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @remove_cb.setter
    def remove_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @drop_cb.setter
    def drop_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drop_all_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @drop_all_cb.setter
    def drop_all_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def get_victim_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @get_victim_cb.setter
    def get_victim_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def reserve_cond_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @reserve_cond_cb.setter
    def reserve_cond_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...


class _cache_ops_t_type(TypedDict, total=False):
    compare_cb: Callable = ...
    create_cb: Callable = ...
    free_cb: Callable = ...


class cache_ops_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _cache_ops_t_type) -> "cache_ops_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def compare_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @compare_cb.setter
    def compare_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def create_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @create_cb.setter
    def create_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def free_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @free_cb.setter
    def free_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...


class _span_t_type(TypedDict, total=False):
    txt: Union[str, bytearray, bytes, List[int]] = ...
    spangroup: "obj" = ...
    style: "style_t" = ...
    static_flag: int = ...


class span_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _span_t_type) -> "span_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def set_text(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_static(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def txt(self) -> Union[str, bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @txt.setter
    def txt(self, value: Union[str, bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def spangroup(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @spangroup.setter
    def spangroup(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def style(self) -> "style_t":
        """
        No Docstrings Yet
        """
        ...

    @style.setter
    def style(self, value: "style_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def static_flag(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @static_flag.setter
    def static_flag(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _pinyin_dict_t_type(TypedDict, total=False):
    py: Union[str, bytearray, bytes, List[int]] = ...
    py_mb: Union[str, bytearray, bytes, List[int]] = ...


class pinyin_dict_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _pinyin_dict_t_type) -> "pinyin_dict_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def py(self, value: Union[str, bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    py = property(fset=py)

    def py_mb(self, value: Union[str, bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    py_mb = property(fset=py_mb)


class _color16_t_type(TypedDict, total=False):
    blue: int = ...
    green: int = ...
    red: int = ...


class color16_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _color16_t_type) -> "color16_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def premultiply(self, a: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blue(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @blue.setter
    def blue(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def green(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @green.setter
    def green(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def red(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @red.setter
    def red(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _mem_monitor_t_type(TypedDict, total=False):
    total_size: int = ...
    free_cnt: int = ...
    free_size: int = ...
    free_biggest_size: int = ...
    used_cnt: int = ...
    max_used: int = ...
    used_pct: int = ...
    frag_pct: int = ...


class mem_monitor_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _mem_monitor_t_type) -> "mem_monitor_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def core(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def monitor(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def total_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @total_size.setter
    def total_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def free_cnt(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @free_cnt.setter
    def free_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def free_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @free_size.setter
    def free_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def free_biggest_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @free_biggest_size.setter
    def free_biggest_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def used_cnt(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @used_cnt.setter
    def used_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def max_used(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @max_used.setter
    def max_used(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def used_pct(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @used_pct.setter
    def used_pct(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def frag_pct(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @frag_pct.setter
    def frag_pct(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _anim_timeline_t_type(TypedDict, total=False):
    ...


class anim_timeline_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _anim_timeline_t_type) -> "anim_timeline_t":
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add(self, start_time: int, a: "anim_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def start(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def pause(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_reverse(self, reverse: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_progress(self, progress: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_playtime(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_reverse(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_progress(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...


class _rb_t_type(TypedDict, total=False):
    root: "rb_node_t" = ...
    compare: Callable = ...
    size: int = ...


class rb_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _rb_t_type) -> "rb_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, compare: "rb_compare_t", node_size: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def insert(self, key: Any, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    def find(self, key: Any, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    def remove_node(self, node: "rb_node_t", /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def remove(self, key: Any, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def drop_node(self, node: "rb_node_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def drop(self, key: Any, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def minimum(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    def maximum(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    def destroy(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def root(self) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    @root.setter
    def root(self, value: "rb_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def compare(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @compare.setter
    def compare(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _rb_node_t_type(TypedDict, total=False):
    parent: "rb_node_t" = ...
    left: "rb_node_t" = ...
    right: "rb_node_t" = ...
    color: "rb_color_t" = ...
    data: Any = ...


class rb_node_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _rb_node_t_type) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def minimum_from(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    def maximum_from(self, /) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def parent(self) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    @parent.setter
    def parent(self, value: "rb_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def left(self) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    @left.setter
    def left(self, value: "rb_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def right(self) -> "rb_node_t":
        """
        No Docstrings Yet
        """
        ...

    @right.setter
    def right(self, value: "rb_node_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "rb_color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "rb_color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @data.setter
    def data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _fs_drv_t_type(TypedDict, total=False):
    letter: Union[int, str, bytes, bytearray] = ...
    cache_size: int = ...
    ready_cb: Callable = ...
    open_cb: Callable = ...
    close_cb: Callable = ...
    read_cb: Callable = ...
    write_cb: Callable = ...
    seek_cb: Callable = ...
    tell_cb: Callable = ...
    dir_open_cb: Callable = ...
    dir_read_cb: Callable = ...
    dir_close_cb: Callable = ...
    user_data: Any = ...


class fs_drv_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _fs_drv_t_type) -> "fs_drv_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def register(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def letter(self) -> Union[int, str, bytes, bytearray]:
        """
        No Docstrings Yet
        """
        ...

    @letter.setter
    def letter(self, value: Union[int, str, bytes, bytearray]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cache_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @cache_size.setter
    def cache_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ready_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @ready_cb.setter
    def ready_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def open_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @open_cb.setter
    def open_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def close_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @close_cb.setter
    def close_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def read_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @read_cb.setter
    def read_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def write_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @write_cb.setter
    def write_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def seek_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @seek_cb.setter
    def seek_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tell_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @tell_cb.setter
    def tell_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dir_open_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @dir_open_cb.setter
    def dir_open_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dir_read_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @dir_read_cb.setter
    def dir_read_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dir_close_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @dir_close_cb.setter
    def dir_close_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _fs_file_t_type(TypedDict, total=False):
    file_d: Any = ...
    drv: "fs_drv_t" = ...
    cache: "fs_file_cache_t" = ...


class fs_file_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _fs_file_t_type) -> "fs_file_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def open(
        self,
        path: Union[str, bytearray, bytes, List[int]],
        mode: "fs_mode_t",
        /
    ) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    def close(self, /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    def read(self, buf: Any, btr: int, br: List[int], /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    def write(self, buf: Any, btw: int, bw: List[int], /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    def seek(self, pos: int, whence: "fs_whence_t", /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    def tell(self, pos: List[int], /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def file_d(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @file_d.setter
    def file_d(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drv(self) -> "fs_drv_t":
        """
        No Docstrings Yet
        """
        ...

    @drv.setter
    def drv(self, value: "fs_drv_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cache(self) -> "fs_file_cache_t":
        """
        No Docstrings Yet
        """
        ...

    @cache.setter
    def cache(self, value: "fs_file_cache_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _fs_file_cache_t_type(TypedDict, total=False):
    start: int = ...
    end: int = ...
    file_position: int = ...
    buffer: Any = ...


class fs_file_cache_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _fs_file_cache_t_type) -> "fs_file_cache_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def start(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @start.setter
    def start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @end.setter
    def end(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def file_position(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @file_position.setter
    def file_position(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buffer(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @buffer.setter
    def buffer(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _fs_path_ex_t_type(TypedDict, total=False):
    path: List[Union[int, str, bytes, bytearray]] = ...
    buffer: Any = ...
    size: int = ...


class fs_path_ex_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _fs_path_ex_t_type) -> "fs_path_ex_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def make_path_from_buffer(
        self,
        letter: Union[int, str, bytes, bytearray],
        buf: Any,
        size: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def path(self) -> List[Union[int, str, bytes, bytearray]]:
        """
        No Docstrings Yet
        """
        ...

    @path.setter
    def path(self, value: List[Union[int, str, bytes, bytearray]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buffer(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @buffer.setter
    def buffer(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _fs_dir_t_type(TypedDict, total=False):
    dir_d: Any = ...
    drv: "fs_drv_t" = ...


class fs_dir_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _fs_dir_t_type) -> "fs_dir_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def open(
        self,
        path: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    def read(
        self,
        fn: Union[str, bytearray, bytes, List[int]],
        fn_len: int,
        /
    ) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    def close(self, /) -> "fs_res_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def dir_d(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @dir_d.setter
    def dir_d(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def drv(self) -> "fs_drv_t":
        """
        No Docstrings Yet
        """
        ...

    @drv.setter
    def drv(self, value: "fs_drv_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _grad_t_type(TypedDict, total=False):
    color_map: "color_t" = ...
    opa_map: "opa_t" = ...
    size: int = ...


class grad_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _grad_t_type) -> "grad_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def gradient_cleanup(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color_map(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color_map.setter
    def color_map(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa_map(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa_map.setter
    def opa_map(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_fill_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    opa: "opa_t" = ...
    color: "color_t" = ...
    grad: "grad_dsc_t" = ...


class draw_fill_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_fill_dsc_t_type) -> "draw_fill_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def grad(self) -> "grad_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @grad.setter
    def grad(self, value: "grad_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_border_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    color: "color_t" = ...
    width: int = ...
    opa: "opa_t" = ...
    side: "border_side_t" = ...


class draw_border_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_border_dsc_t_type) -> "draw_border_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def side(self) -> "border_side_t":
        """
        No Docstrings Yet
        """
        ...

    @side.setter
    def side(self, value: "border_side_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_box_shadow_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    radius: int = ...
    color: "color_t" = ...
    width: int = ...
    spread: int = ...
    ofs_x: int = ...
    ofs_y: int = ...
    opa: "opa_t" = ...
    bg_cover: int = ...


class draw_box_shadow_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_box_shadow_dsc_t_type
    ) -> "draw_box_shadow_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def spread(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @spread.setter
    def spread(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_x(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @ofs_x.setter
    def ofs_x(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def ofs_y(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @ofs_y.setter
    def ofs_y(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_cover(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @bg_cover.setter
    def bg_cover(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_glyph_dsc_t_type(TypedDict, total=False):
    glyph_data: Any = ...
    format: "font_glyph_format_t" = ...
    letter_coords: "area_t" = ...
    bg_coords: "area_t" = ...
    g: "font_glyph_dsc_t" = ...
    color: "color_t" = ...
    opa: "opa_t" = ...
    _draw_buf: "draw_buf_t" = ...


class draw_glyph_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_glyph_dsc_t_type) -> "draw_glyph_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def glyph_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @glyph_data.setter
    def glyph_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def format(self) -> "font_glyph_format_t":
        """
        No Docstrings Yet
        """
        ...

    @format.setter
    def format(self, value: "font_glyph_format_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def letter_coords(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @letter_coords.setter
    def letter_coords(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_coords(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_coords.setter
    def bg_coords(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def g(self) -> "font_glyph_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @g.setter
    def g(self, value: "font_glyph_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def _draw_buf(self) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    @_draw_buf.setter
    def _draw_buf(self, value: "draw_buf_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_unit_t_type(TypedDict, total=False):
    next: "draw_unit_t" = ...
    target_layer: "layer_t" = ...
    clip_area: "area_t" = ...
    dispatch_cb: Callable = ...
    evaluate_cb: Callable = ...
    delete_cb: Callable = ...


class draw_unit_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_unit_t_type) -> "draw_unit_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def label_iterate_characters(
        self,
        dsc: "draw_label_dsc_t",
        coords: "area_t",
        cb: "draw_glyph_cb_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_fill(self, dsc: "draw_fill_dsc_t", coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_border(self, dsc: "draw_border_dsc_t", coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_box_shadow(
        self,
        dsc: "draw_box_shadow_dsc_t",
        coords: "area_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_image(
        self,
        draw_dsc: "draw_image_dsc_t",
        coords: "area_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_label(self, dsc: "draw_label_dsc_t", coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_arc(self, dsc: "draw_arc_dsc_t", coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_line(self, dsc: "draw_line_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_layer(
        self,
        draw_dsc: "draw_image_dsc_t",
        coords: "area_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_triangle(self, dsc: "draw_triangle_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_mask_rect(
        self,
        dsc: "draw_mask_rect_dsc_t",
        coords: "area_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_transform(
        self,
        dest_area: "area_t",
        src_buf: Any,
        src_w: int,
        src_h: int,
        src_stride: int,
        draw_dsc: "draw_image_dsc_t",
        sup: "draw_image_sup_t",
        cf: "color_format_t",
        dest_buf: Any,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def sw_blend(self, dsc: "draw_sw_blend_dsc_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def next(self) -> "draw_unit_t":
        """
        No Docstrings Yet
        """
        ...

    @next.setter
    def next(self, value: "draw_unit_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def target_layer(self) -> "layer_t":
        """
        No Docstrings Yet
        """
        ...

    @target_layer.setter
    def target_layer(self, value: "layer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def clip_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @clip_area.setter
    def clip_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dispatch_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @dispatch_cb.setter
    def dispatch_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def evaluate_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @evaluate_cb.setter
    def evaluate_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def delete_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @delete_cb.setter
    def delete_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_triangle_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    bg_opa: "opa_t" = ...
    bg_color: "color_t" = ...
    bg_grad: "grad_dsc_t" = ...
    p: List["point_precise_t"] = ...


class draw_triangle_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_triangle_dsc_t_type
    ) -> "draw_triangle_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_opa.setter
    def bg_opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_color.setter
    def bg_color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bg_grad(self) -> "grad_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @bg_grad.setter
    def bg_grad(self, value: "grad_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def p(self) -> List["point_precise_t"]:
        """
        No Docstrings Yet
        """
        ...

    @p.setter
    def p(self, value: List["point_precise_t"]) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_mask_rect_dsc_t_type(TypedDict, total=False):
    base: "draw_dsc_base_t" = ...
    area: "area_t" = ...
    radius: int = ...


class draw_mask_rect_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_mask_rect_dsc_t_type
    ) -> "draw_mask_rect_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def base(self) -> "draw_dsc_base_t":
        """
        No Docstrings Yet
        """
        ...

    @base.setter
    def base(self, value: "draw_dsc_base_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @area.setter
    def area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _indev_t_type(TypedDict, total=False):
    type: "indev_type_t" = ...
    read_cb: Callable = ...
    state: "indev_state_t" = ...
    mode: "indev_mode_t" = ...
    long_pr_sent: int = ...
    reset_query: int = ...
    enabled: int = ...
    wait_until_release: int = ...
    pr_timestamp: int = ...
    longpr_rep_timestamp: int = ...
    driver_data: Any = ...
    user_data: Any = ...
    disp: "display_t" = ...
    read_timer: "timer_t" = ...
    scroll_limit: int = ...
    scroll_throw: int = ...
    gesture_min_velocity: int = ...
    gesture_limit: int = ...
    long_press_time: int = ...
    long_press_repeat_time: int = ...
    rotary_sensitvity: int = ...
    pointer: "indev_pointer_t" = ...
    keypad: "indev_keypad_t" = ...
    cursor: "obj" = ...
    group: "group_t" = ...
    btn_points: "point_t" = ...
    event_list: "event_list_t" = ...
    scroll_throw_anim: "anim_t" = ...


class indev_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _indev_t_type) -> "indev_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_next(self, /) -> "indev_t":
        """
        No Docstrings Yet
        """
        ...

    def read(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def enable(self, enable: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_type(self, indev_type: "indev_type_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_read_cb(self, read_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_user_data(self, indev: "indev_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_driver_data(self, indev: "indev_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_display(self, disp: "display_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_type(self, /) -> "indev_type_t":
        """
        No Docstrings Yet
        """
        ...

    def get_read_cb(self, /) -> "indev_read_cb_t":
        """
        No Docstrings Yet
        """
        ...

    def get_state(self, /) -> "indev_state_t":
        """
        No Docstrings Yet
        """
        ...

    def get_group(self, /) -> "group_t":
        """
        No Docstrings Yet
        """
        ...

    def get_display(self, /) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_driver_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def reset(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def reset_long_press(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_cursor(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_group(self, group: "group_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_button_points(self, points: List["point_t"], /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_point(self, point: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_gesture_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...

    def get_key(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_vect(self, point: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def wait_release(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_read_timer(self, /) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    def set_mode(self, mode: "indev_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_mode(self, /) -> "indev_mode_t":
        """
        No Docstrings Yet
        """
        ...

    def add_event_cb(
        self,
        event_cb: Callable,
        filter: "event_code_t",
        indev: "indev_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_event_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_event_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def remove_event(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def remove_event_cb_with_user_data(
        self,
        event_cb: Callable,
        indev: "indev_t",
        /
    ) -> int:
        """
        No Docstrings Yet
        """
        ...

    def send_event(self, code: "event_code_t", param: Any, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def find_scroll_obj(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @property
    def type(self) -> "indev_type_t":
        """
        No Docstrings Yet
        """
        ...

    @type.setter
    def type(self, value: "indev_type_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def read_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @read_cb.setter
    def read_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def state(self) -> "indev_state_t":
        """
        No Docstrings Yet
        """
        ...

    @state.setter
    def state(self, value: "indev_state_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def mode(self) -> "indev_mode_t":
        """
        No Docstrings Yet
        """
        ...

    @mode.setter
    def mode(self, value: "indev_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def long_pr_sent(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @long_pr_sent.setter
    def long_pr_sent(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def reset_query(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @reset_query.setter
    def reset_query(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def enabled(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @enabled.setter
    def enabled(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def wait_until_release(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @wait_until_release.setter
    def wait_until_release(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pr_timestamp(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @pr_timestamp.setter
    def pr_timestamp(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def longpr_rep_timestamp(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @longpr_rep_timestamp.setter
    def longpr_rep_timestamp(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def driver_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @driver_data.setter
    def driver_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def disp(self) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    @disp.setter
    def disp(self, value: "display_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def read_timer(self) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    @read_timer.setter
    def read_timer(self, value: "timer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_limit(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @scroll_limit.setter
    def scroll_limit(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_throw(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @scroll_throw.setter
    def scroll_throw(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gesture_min_velocity(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @gesture_min_velocity.setter
    def gesture_min_velocity(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gesture_limit(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @gesture_limit.setter
    def gesture_limit(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def long_press_time(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @long_press_time.setter
    def long_press_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def long_press_repeat_time(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @long_press_repeat_time.setter
    def long_press_repeat_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def rotary_sensitvity(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @rotary_sensitvity.setter
    def rotary_sensitvity(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def pointer(self) -> "indev_pointer_t":
        """
        No Docstrings Yet
        """
        ...

    @pointer.setter
    def pointer(self, value: "indev_pointer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def keypad(self) -> "indev_keypad_t":
        """
        No Docstrings Yet
        """
        ...

    @keypad.setter
    def keypad(self, value: "indev_keypad_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cursor(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @cursor.setter
    def cursor(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def group(self) -> "group_t":
        """
        No Docstrings Yet
        """
        ...

    @group.setter
    def group(self, value: "group_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def btn_points(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @btn_points.setter
    def btn_points(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def event_list(self) -> "event_list_t":
        """
        No Docstrings Yet
        """
        ...

    @event_list.setter
    def event_list(self, value: "event_list_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_throw_anim(self) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...

    @scroll_throw_anim.setter
    def scroll_throw_anim(self, value: "anim_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _indev_data_t_type(TypedDict, total=False):
    point: "point_t" = ...
    key: int = ...
    btn_id: int = ...
    enc_diff: int = ...
    state: "indev_state_t" = ...
    continue_reading: bool = ...


class indev_data_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _indev_data_t_type) -> "indev_data_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def point(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @point.setter
    def point(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def key(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @key.setter
    def key(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def btn_id(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @btn_id.setter
    def btn_id(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def enc_diff(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @enc_diff.setter
    def enc_diff(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def state(self) -> "indev_state_t":
        """
        No Docstrings Yet
        """
        ...

    @state.setter
    def state(self, value: "indev_state_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def continue_reading(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @continue_reading.setter
    def continue_reading(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...


class _indev_pointer_t_type(TypedDict, total=False):
    act_point: "point_t" = ...
    last_point: "point_t" = ...
    last_raw_point: "point_t" = ...
    vect: "point_t" = ...
    scroll_sum: "point_t" = ...
    scroll_throw_vect: "point_t" = ...
    scroll_throw_vect_ori: "point_t" = ...
    act_obj: "obj" = ...
    last_obj: "obj" = ...
    scroll_obj: "obj" = ...
    last_pressed: "obj" = ...
    scroll_area: "area_t" = ...
    gesture_sum: "point_t" = ...
    diff: int = ...
    scroll_dir: "dir_t" = ...
    gesture_dir: "dir_t" = ...
    gesture_sent: int = ...


class indev_pointer_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _indev_pointer_t_type) -> "indev_pointer_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def act_point(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @act_point.setter
    def act_point(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_point(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @last_point.setter
    def last_point(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_raw_point(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @last_raw_point.setter
    def last_raw_point(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def vect(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @vect.setter
    def vect(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_sum(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @scroll_sum.setter
    def scroll_sum(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_throw_vect(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @scroll_throw_vect.setter
    def scroll_throw_vect(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_throw_vect_ori(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @scroll_throw_vect_ori.setter
    def scroll_throw_vect_ori(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def act_obj(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @act_obj.setter
    def act_obj(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_obj(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @last_obj.setter
    def last_obj(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_obj(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @scroll_obj.setter
    def scroll_obj(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_pressed(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @last_pressed.setter
    def last_pressed(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @scroll_area.setter
    def scroll_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gesture_sum(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @gesture_sum.setter
    def gesture_sum(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def diff(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @diff.setter
    def diff(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def scroll_dir(self) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...

    @scroll_dir.setter
    def scroll_dir(self, value: "dir_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gesture_dir(self) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...

    @gesture_dir.setter
    def gesture_dir(self, value: "dir_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gesture_sent(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @gesture_sent.setter
    def gesture_sent(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _indev_keypad_t_type(TypedDict, total=False):
    last_state: "indev_state_t" = ...
    last_key: int = ...


class indev_keypad_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _indev_keypad_t_type) -> "indev_keypad_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def last_state(self) -> "indev_state_t":
        """
        No Docstrings Yet
        """
        ...

    @last_state.setter
    def last_state(self, value: "indev_state_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def last_key(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @last_key.setter
    def last_key(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _gd_GIF_type(TypedDict, total=False):
    fd: "fs_file_t" = ...
    data: Union[str, bytearray, bytes, List[int]] = ...
    is_file: int = ...
    f_rw_p: int = ...
    anim_start: int = ...
    width: int = ...
    height: int = ...
    depth: int = ...
    loop_count: int = ...
    gce: "gd_GCE" = ...
    palette: "gd_Palette" = ...
    lct: "gd_Palette" = ...
    gct: "gd_Palette" = ...
    plain_text: Callable = ...
    comment: Callable = ...
    application: Callable = ...
    fx: int = ...
    fy: int = ...
    fw: int = ...
    fh: int = ...
    bgindex: int = ...
    canvas: Union[bytearray, bytes, List[int]] = ...
    frame: Union[bytearray, bytes, List[int]] = ...


class gd_GIF(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _gd_GIF_type) -> "gd_GIF":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def render_frame(
        self,
        buffer: Union[bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_frame(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def rewind(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def close_gif(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def fd(self) -> "fs_file_t":
        """
        No Docstrings Yet
        """
        ...

    @fd.setter
    def fd(self, value: "fs_file_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def data(self) -> Union[str, bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @data.setter
    def data(self, value: Union[str, bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def is_file(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @is_file.setter
    def is_file(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def f_rw_p(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @f_rw_p.setter
    def f_rw_p(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def anim_start(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @anim_start.setter
    def anim_start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @width.setter
    def width(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def height(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @height.setter
    def height(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def depth(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @depth.setter
    def depth(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def loop_count(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @loop_count.setter
    def loop_count(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gce(self) -> "gd_GCE":
        """
        No Docstrings Yet
        """
        ...

    @gce.setter
    def gce(self, value: "gd_GCE") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def palette(self) -> "gd_Palette":
        """
        No Docstrings Yet
        """
        ...

    @palette.setter
    def palette(self, value: "gd_Palette") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def lct(self) -> "gd_Palette":
        """
        No Docstrings Yet
        """
        ...

    @lct.setter
    def lct(self, value: "gd_Palette") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def gct(self) -> "gd_Palette":
        """
        No Docstrings Yet
        """
        ...

    @gct.setter
    def gct(self, value: "gd_Palette") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def plain_text(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @plain_text.setter
    def plain_text(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def comment(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @comment.setter
    def comment(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def application(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @application.setter
    def application(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def fx(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @fx.setter
    def fx(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def fy(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @fy.setter
    def fy(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def fw(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @fw.setter
    def fw(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def fh(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @fh.setter
    def fh(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def bgindex(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @bgindex.setter
    def bgindex(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def canvas(self) -> Union[bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @canvas.setter
    def canvas(self, value: Union[bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def frame(self) -> Union[bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @frame.setter
    def frame(self, value: Union[bytearray, bytes, List[int]]) -> None:
        """
        No Docstrings Yet
        """
        ...


class _gd_GCE_type(TypedDict, total=False):
    delay: int = ...
    tindex: int = ...
    disposal: int = ...
    input: int = ...
    transparency: int = ...


class gd_GCE(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _gd_GCE_type) -> "gd_GCE":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def delay(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @delay.setter
    def delay(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tindex(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @tindex.setter
    def tindex(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def disposal(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @disposal.setter
    def disposal(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def input(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @input.setter
    def input(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def transparency(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @transparency.setter
    def transparency(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _gd_Palette_type(TypedDict, total=False):
    size: int = ...
    colors: List[int] = ...


class gd_Palette(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _gd_Palette_type) -> "gd_Palette":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @size.setter
    def size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def colors(self) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    @colors.setter
    def colors(self, value: List[int]) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_line_param_t_type(TypedDict, total=False):
    dsc: "_draw_sw_mask_common_dsc_t" = ...
    cfg: "draw_sw_mask_line_param_cfg_t" = ...
    origo: "point_t" = ...
    xy_steep: int = ...
    yx_steep: int = ...
    steep: int = ...
    spx: int = ...
    flat: int = ...
    inv: int = ...


class draw_sw_mask_line_param_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_line_param_t_type
    ) -> "draw_sw_mask_line_param_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def points_init(
        self,
        p1x: int,
        p1y: int,
        p2x: int,
        p2y: int,
        side: "draw_sw_mask_line_side_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def angle_init(
        self,
        p1x: int,
        py: int,
        angle: int,
        side: "draw_sw_mask_line_side_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc(self) -> "_draw_sw_mask_common_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @dsc.setter
    def dsc(self, value: "_draw_sw_mask_common_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cfg(self) -> "draw_sw_mask_line_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    @cfg.setter
    def cfg(self, value: "draw_sw_mask_line_param_cfg_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def origo(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @origo.setter
    def origo(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def xy_steep(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @xy_steep.setter
    def xy_steep(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def yx_steep(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @yx_steep.setter
    def yx_steep(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def steep(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @steep.setter
    def steep(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def spx(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @spx.setter
    def spx(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def flat(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @flat.setter
    def flat(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def inv(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @inv.setter
    def inv(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_line_param_cfg_t_type(TypedDict, total=False):
    p1: "point_t" = ...
    p2: "point_t" = ...
    side: "draw_sw_mask_line_side_t" = ...


class draw_sw_mask_line_param_cfg_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_line_param_cfg_t_type
    ) -> "draw_sw_mask_line_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def p1(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @p1.setter
    def p1(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def p2(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @p2.setter
    def p2(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def side(self) -> "draw_sw_mask_line_side_t":
        """
        No Docstrings Yet
        """
        ...

    @side.setter
    def side(self, value: "draw_sw_mask_line_side_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_angle_param_t_type(TypedDict, total=False):
    dsc: "_draw_sw_mask_common_dsc_t" = ...
    cfg: "draw_sw_mask_angle_param_cfg_t" = ...
    start_line: "draw_sw_mask_line_param_t" = ...
    end_line: "draw_sw_mask_line_param_t" = ...
    delta_deg: int = ...


class draw_sw_mask_angle_param_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_angle_param_t_type
    ) -> "draw_sw_mask_angle_param_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(
        self,
        vertex_x: int,
        vertex_y: int,
        start_angle: int,
        end_angle: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc(self) -> "_draw_sw_mask_common_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @dsc.setter
    def dsc(self, value: "_draw_sw_mask_common_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cfg(self) -> "draw_sw_mask_angle_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    @cfg.setter
    def cfg(self, value: "draw_sw_mask_angle_param_cfg_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_line(self) -> "draw_sw_mask_line_param_t":
        """
        No Docstrings Yet
        """
        ...

    @start_line.setter
    def start_line(self, value: "draw_sw_mask_line_param_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_line(self) -> "draw_sw_mask_line_param_t":
        """
        No Docstrings Yet
        """
        ...

    @end_line.setter
    def end_line(self, value: "draw_sw_mask_line_param_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def delta_deg(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @delta_deg.setter
    def delta_deg(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_angle_param_cfg_t_type(TypedDict, total=False):
    vertex_p: "point_t" = ...
    start_angle: int = ...
    end_angle: int = ...


class draw_sw_mask_angle_param_cfg_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_angle_param_cfg_t_type
    ) -> "draw_sw_mask_angle_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def vertex_p(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @vertex_p.setter
    def vertex_p(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def start_angle(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @start_angle.setter
    def start_angle(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def end_angle(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @end_angle.setter
    def end_angle(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_radius_param_t_type(TypedDict, total=False):
    dsc: "_draw_sw_mask_common_dsc_t" = ...
    cfg: "draw_sw_mask_radius_param_cfg_t" = ...
    circle: "_draw_sw_mask_radius_circle_dsc_t" = ...


class draw_sw_mask_radius_param_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_radius_param_t_type
    ) -> "draw_sw_mask_radius_param_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, rect: "area_t", radius: int, inv: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc(self) -> "_draw_sw_mask_common_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @dsc.setter
    def dsc(self, value: "_draw_sw_mask_common_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cfg(self) -> "draw_sw_mask_radius_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    @cfg.setter
    def cfg(self, value: "draw_sw_mask_radius_param_cfg_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def circle(self) -> "_draw_sw_mask_radius_circle_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @circle.setter
    def circle(self, value: "_draw_sw_mask_radius_circle_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_radius_param_cfg_t_type(TypedDict, total=False):
    rect: "area_t" = ...
    radius: int = ...
    outer: int = ...


class draw_sw_mask_radius_param_cfg_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_radius_param_cfg_t_type
    ) -> "draw_sw_mask_radius_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def rect(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @rect.setter
    def rect(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def radius(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @radius.setter
    def radius(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def outer(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @outer.setter
    def outer(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_fade_param_t_type(TypedDict, total=False):
    dsc: "_draw_sw_mask_common_dsc_t" = ...
    cfg: "draw_sw_mask_fade_param_cfg_t" = ...


class draw_sw_mask_fade_param_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_fade_param_t_type
    ) -> "draw_sw_mask_fade_param_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(
        self,
        coords: "area_t",
        opa_top: "opa_t",
        y_top: int,
        opa_bottom: "opa_t",
        y_bottom: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc(self) -> "_draw_sw_mask_common_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @dsc.setter
    def dsc(self, value: "_draw_sw_mask_common_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cfg(self) -> "draw_sw_mask_fade_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    @cfg.setter
    def cfg(self, value: "draw_sw_mask_fade_param_cfg_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_fade_param_cfg_t_type(TypedDict, total=False):
    coords: "area_t" = ...
    y_top: int = ...
    y_bottom: int = ...
    opa_top: "opa_t" = ...
    opa_bottom: "opa_t" = ...


class draw_sw_mask_fade_param_cfg_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_fade_param_cfg_t_type
    ) -> "draw_sw_mask_fade_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def coords(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @coords.setter
    def coords(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y_top(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y_top.setter
    def y_top(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def y_bottom(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @y_bottom.setter
    def y_bottom(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa_top(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa_top.setter
    def opa_top(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa_bottom(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa_bottom.setter
    def opa_bottom(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_map_param_t_type(TypedDict, total=False):
    dsc: "_draw_sw_mask_common_dsc_t" = ...
    cfg: "draw_sw_mask_map_param_cfg_t" = ...


class draw_sw_mask_map_param_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_map_param_t_type
    ) -> "draw_sw_mask_map_param_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    def init(self, coords: "area_t", map: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dsc(self) -> "_draw_sw_mask_common_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @dsc.setter
    def dsc(self, value: "_draw_sw_mask_common_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def cfg(self) -> "draw_sw_mask_map_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    @cfg.setter
    def cfg(self, value: "draw_sw_mask_map_param_cfg_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_mask_map_param_cfg_t_type(TypedDict, total=False):
    coords: "area_t" = ...
    map: "opa_t" = ...


class draw_sw_mask_map_param_cfg_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_mask_map_param_cfg_t_type
    ) -> "draw_sw_mask_map_param_cfg_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def coords(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @coords.setter
    def coords(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def map(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @map.setter
    def map(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _color_hsv_t_type(TypedDict, total=False):
    h: int = ...
    s: int = ...
    v: int = ...


class color_hsv_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _color_hsv_t_type) -> "color_hsv_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def h(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @h.setter
    def h(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def s(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @s.setter
    def s(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def v(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @v.setter
    def v(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _hit_test_info_t_type(TypedDict, total=False):
    point: "point_t" = ...
    res: bool = ...


class hit_test_info_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _hit_test_info_t_type) -> "hit_test_info_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def point(self) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    @point.setter
    def point(self, value: "point_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def res(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @res.setter
    def res(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_sw_blend_dsc_t_type(TypedDict, total=False):
    blend_area: "area_t" = ...
    src_buf: Any = ...
    src_stride: int = ...
    src_color_format: "color_format_t" = ...
    src_area: "area_t" = ...
    opa: "opa_t" = ...
    color: "color_t" = ...
    mask_buf: "opa_t" = ...
    mask_res: "draw_sw_mask_res_t" = ...
    mask_area: "area_t" = ...
    mask_stride: int = ...
    blend_mode: "blend_mode_t" = ...


class draw_sw_blend_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_sw_blend_dsc_t_type
    ) -> "draw_sw_blend_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def blend_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @blend_area.setter
    def blend_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def src_buf(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @src_buf.setter
    def src_buf(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def src_stride(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @src_stride.setter
    def src_stride(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def src_color_format(self) -> "color_format_t":
        """
        No Docstrings Yet
        """
        ...

    @src_color_format.setter
    def src_color_format(self, value: "color_format_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def src_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @src_area.setter
    def src_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def opa(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @opa.setter
    def opa(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def color(self) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    @color.setter
    def color(self, value: "color_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def mask_buf(self) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    @mask_buf.setter
    def mask_buf(self, value: "opa_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def mask_res(self) -> "draw_sw_mask_res_t":
        """
        No Docstrings Yet
        """
        ...

    @mask_res.setter
    def mask_res(self, value: "draw_sw_mask_res_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def mask_area(self) -> "area_t":
        """
        No Docstrings Yet
        """
        ...

    @mask_area.setter
    def mask_area(self, value: "area_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def mask_stride(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @mask_stride.setter
    def mask_stride(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def blend_mode(self) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...

    @blend_mode.setter
    def blend_mode(self, value: "blend_mode_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _sqrt_res_t_type(TypedDict, total=False):
    i: int = ...
    f: int = ...


class sqrt_res_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _sqrt_res_t_type) -> "sqrt_res_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def i(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @i.setter
    def i(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def f(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @f.setter
    def f(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_buf_handlers_t_type(TypedDict, total=False):
    buf_malloc_cb: Callable = ...
    buf_free_cb: Callable = ...
    align_pointer_cb: Callable = ...
    invalidate_cache_cb: Callable = ...
    width_to_stride_cb: Callable = ...


class draw_buf_handlers_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(
        self,
        args: _draw_buf_handlers_t_type
    ) -> "draw_buf_handlers_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def buf_malloc_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @buf_malloc_cb.setter
    def buf_malloc_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def buf_free_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @buf_free_cb.setter
    def buf_free_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def align_pointer_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @align_pointer_cb.setter
    def align_pointer_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def invalidate_cache_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @invalidate_cache_cb.setter
    def invalidate_cache_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def width_to_stride_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @width_to_stride_cb.setter
    def width_to_stride_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...


class _global_t_type(TypedDict, total=False):
    inited: bool = ...
    deinit_in_progress: bool = ...
    disp_ll: "ll_t" = ...
    disp_refresh: "display_t" = ...
    disp_default: "display_t" = ...
    style_trans_ll: "ll_t" = ...
    style_refresh: bool = ...
    style_custom_table_size: int = ...
    style_last_custom_prop_id: int = ...
    style_custom_prop_flag_lookup_table: Union[
        bytearray, bytes, List[int]] = ...
    group_ll: "ll_t" = ...
    group_default: "group_t" = ...
    indev_ll: "ll_t" = ...
    indev_active: "indev_t" = ...
    indev_obj_active: "obj" = ...
    layout_count: int = ...
    layout_list: "layout_dsc_t" = ...
    layout_update_mutex: bool = ...
    memory_zero: int = ...
    math_rand_seed: int = ...
    event_header: "event_t" = ...
    event_last_register_id: int = ...
    timer_state: "timer_state_t" = ...
    anim_state: "anim_state_t" = ...
    tick_state: "tick_state_t" = ...
    draw_buf_handlers: "draw_buf_handlers_t" = ...
    img_decoder_ll: "ll_t" = ...
    draw_info: "draw_global_info_t" = ...


class global_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _global_t_type) -> "global_t":
        """
        No Docstrings Yet
        """
        ...

    @property
    def inited(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @inited.setter
    def inited(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def deinit_in_progress(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @deinit_in_progress.setter
    def deinit_in_progress(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def disp_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @disp_ll.setter
    def disp_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def disp_refresh(self) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    @disp_refresh.setter
    def disp_refresh(self, value: "display_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def disp_default(self) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    @disp_default.setter
    def disp_default(self, value: "display_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def style_trans_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @style_trans_ll.setter
    def style_trans_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def style_refresh(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @style_refresh.setter
    def style_refresh(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def style_custom_table_size(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @style_custom_table_size.setter
    def style_custom_table_size(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def style_last_custom_prop_id(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @style_last_custom_prop_id.setter
    def style_last_custom_prop_id(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def style_custom_prop_flag_lookup_table(self) -> Union[
        bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    @style_custom_prop_flag_lookup_table.setter
    def style_custom_prop_flag_lookup_table(
        self,
        value: Union[bytearray, bytes, List[int]]
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def group_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @group_ll.setter
    def group_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def group_default(self) -> "group_t":
        """
        No Docstrings Yet
        """
        ...

    @group_default.setter
    def group_default(self, value: "group_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def indev_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @indev_ll.setter
    def indev_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def indev_active(self) -> "indev_t":
        """
        No Docstrings Yet
        """
        ...

    @indev_active.setter
    def indev_active(self, value: "indev_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def indev_obj_active(self) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    @indev_obj_active.setter
    def indev_obj_active(self, value: "obj") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layout_count(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @layout_count.setter
    def layout_count(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layout_list(self) -> "layout_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    @layout_list.setter
    def layout_list(self, value: "layout_dsc_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def layout_update_mutex(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @layout_update_mutex.setter
    def layout_update_mutex(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def memory_zero(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @memory_zero.setter
    def memory_zero(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def math_rand_seed(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @math_rand_seed.setter
    def math_rand_seed(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def event_header(self) -> "event_t":
        """
        No Docstrings Yet
        """
        ...

    @event_header.setter
    def event_header(self, value: "event_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def event_last_register_id(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @event_last_register_id.setter
    def event_last_register_id(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def timer_state(self) -> "timer_state_t":
        """
        No Docstrings Yet
        """
        ...

    @timer_state.setter
    def timer_state(self, value: "timer_state_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def anim_state(self) -> "anim_state_t":
        """
        No Docstrings Yet
        """
        ...

    @anim_state.setter
    def anim_state(self, value: "anim_state_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tick_state(self) -> "tick_state_t":
        """
        No Docstrings Yet
        """
        ...

    @tick_state.setter
    def tick_state(self, value: "tick_state_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def draw_buf_handlers(self) -> "draw_buf_handlers_t":
        """
        No Docstrings Yet
        """
        ...

    @draw_buf_handlers.setter
    def draw_buf_handlers(self, value: "draw_buf_handlers_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def img_decoder_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @img_decoder_ll.setter
    def img_decoder_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def draw_info(self) -> "draw_global_info_t":
        """
        No Docstrings Yet
        """
        ...

    @draw_info.setter
    def draw_info(self, value: "draw_global_info_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _layout_dsc_t_type(TypedDict, total=False):
    cb: Callable = ...
    user_data: Any = ...


class layout_dsc_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _layout_dsc_t_type) -> "layout_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @cb.setter
    def cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def user_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @user_data.setter
    def user_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _timer_state_t_type(TypedDict, total=False):
    timer_ll: "ll_t" = ...
    lv_timer_run: bool = ...
    idle_last: int = ...
    timer_deleted: bool = ...
    timer_created: bool = ...
    timer_time_until_next: int = ...
    already_running: bool = ...
    periodic_last_tick: int = ...
    busy_time: int = ...
    idle_period_start: int = ...
    run_cnt: int = ...
    resume_cb: Callable = ...
    resume_data: Any = ...


class timer_state_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _timer_state_t_type) -> "timer_state_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def timer_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @timer_ll.setter
    def timer_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def lv_timer_run(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @lv_timer_run.setter
    def lv_timer_run(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def idle_last(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @idle_last.setter
    def idle_last(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def timer_deleted(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @timer_deleted.setter
    def timer_deleted(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def timer_created(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @timer_created.setter
    def timer_created(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def timer_time_until_next(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @timer_time_until_next.setter
    def timer_time_until_next(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def already_running(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @already_running.setter
    def already_running(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def periodic_last_tick(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @periodic_last_tick.setter
    def periodic_last_tick(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def busy_time(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @busy_time.setter
    def busy_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def idle_period_start(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @idle_period_start.setter
    def idle_period_start(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def run_cnt(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @run_cnt.setter
    def run_cnt(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def resume_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @resume_cb.setter
    def resume_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def resume_data(self) -> Any:
        """
        No Docstrings Yet
        """
        ...

    @resume_data.setter
    def resume_data(self, value: Any) -> None:
        """
        No Docstrings Yet
        """
        ...


class _anim_state_t_type(TypedDict, total=False):
    anim_list_changed: bool = ...
    anim_run_round: bool = ...
    timer: "timer_t" = ...
    anim_ll: "ll_t" = ...


class anim_state_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _anim_state_t_type) -> "anim_state_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def anim_list_changed(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @anim_list_changed.setter
    def anim_list_changed(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def anim_run_round(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @anim_run_round.setter
    def anim_run_round(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def timer(self) -> "timer_t":
        """
        No Docstrings Yet
        """
        ...

    @timer.setter
    def timer(self, value: "timer_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def anim_ll(self) -> "ll_t":
        """
        No Docstrings Yet
        """
        ...

    @anim_ll.setter
    def anim_ll(self, value: "ll_t") -> None:
        """
        No Docstrings Yet
        """
        ...


class _tick_state_t_type(TypedDict, total=False):
    sys_time: int = ...
    sys_irq_flag: int = ...
    tick_get_cb: Callable = ...
    delay_cb: Callable = ...


class tick_state_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _tick_state_t_type) -> "tick_state_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def sys_time(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @sys_time.setter
    def sys_time(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def sys_irq_flag(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @sys_irq_flag.setter
    def sys_irq_flag(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def tick_get_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @tick_get_cb.setter
    def tick_get_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def delay_cb(self) -> Callable:
        """
        No Docstrings Yet
        """
        ...

    @delay_cb.setter
    def delay_cb(self, value: Callable) -> None:
        """
        No Docstrings Yet
        """
        ...


class _draw_global_info_t_type(TypedDict, total=False):
    unit_head: "draw_unit_t" = ...
    used_memory_for_layers_kb: int = ...
    dispatch_req: int = ...
    circle_cache_mutex: "mutex_t" = ...
    task_running: bool = ...


class draw_global_info_t(object):
    """
    Non Docstrings Yet
    """

    def __init__(self, args: _draw_global_info_t_type) -> "draw_global_info_t":
        """
        No Docstrings Yet
        """
        ...

    __SIZE__: ClassVar[int] = ...

    @property
    def unit_head(self) -> "draw_unit_t":
        """
        No Docstrings Yet
        """
        ...

    @unit_head.setter
    def unit_head(self, value: "draw_unit_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def used_memory_for_layers_kb(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @used_memory_for_layers_kb.setter
    def used_memory_for_layers_kb(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def dispatch_req(self) -> int:
        """
        No Docstrings Yet
        """
        ...

    @dispatch_req.setter
    def dispatch_req(self, value: int) -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def circle_cache_mutex(self) -> "mutex_t":
        """
        No Docstrings Yet
        """
        ...

    @circle_cache_mutex.setter
    def circle_cache_mutex(self, value: "mutex_t") -> None:
        """
        No Docstrings Yet
        """
        ...

    @property
    def task_running(self) -> bool:
        """
        No Docstrings Yet
        """
        ...

    @task_running.setter
    def task_running(self, value: bool) -> None:
        """
        No Docstrings Yet
        """
        ...


class obj(object):
    """
    No Docstrings Yet
    """

    class TREE_WALK(object):
        """
        No Docstrings Yet
        """
        NEXT: ClassVar[int] = ...
        SKIP_CHILDREN: ClassVar[int] = ...
        END: ClassVar[int] = ...

    class POINT_TRANSFORM_FLAG(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        RECURSIVE: ClassVar[int] = ...
        INVERSE: ClassVar[int] = ...
        INVERSE_RECURSIVE: ClassVar[int] = ...

    class CLASS_EDITABLE(object):
        """
        No Docstrings Yet
        """
        INHERIT: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
        FALSE: ClassVar[int] = ...

    class CLASS_GROUP_DEF(object):
        """
        No Docstrings Yet
        """
        INHERIT: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...
        FALSE: ClassVar[int] = ...

    class CLASS_THEME_INHERITABLE(object):
        """
        No Docstrings Yet
        """
        FALSE: ClassVar[int] = ...
        TRUE: ClassVar[int] = ...

    class FLAG(object):
        """
        No Docstrings Yet
        """
        HIDDEN: ClassVar[int] = ...
        CLICKABLE: ClassVar[int] = ...
        CLICK_FOCUSABLE: ClassVar[int] = ...
        CHECKABLE: ClassVar[int] = ...
        SCROLLABLE: ClassVar[int] = ...
        SCROLL_ELASTIC: ClassVar[int] = ...
        SCROLL_MOMENTUM: ClassVar[int] = ...
        SCROLL_ONE: ClassVar[int] = ...
        SCROLL_CHAIN_HOR: ClassVar[int] = ...
        SCROLL_CHAIN_VER: ClassVar[int] = ...
        SCROLL_CHAIN: ClassVar[int] = ...
        SCROLL_ON_FOCUS: ClassVar[int] = ...
        SCROLL_WITH_ARROW: ClassVar[int] = ...
        SNAPPABLE: ClassVar[int] = ...
        PRESS_LOCK: ClassVar[int] = ...
        EVENT_BUBBLE: ClassVar[int] = ...
        GESTURE_BUBBLE: ClassVar[int] = ...
        ADV_HITTEST: ClassVar[int] = ...
        IGNORE_LAYOUT: ClassVar[int] = ...
        FLOATING: ClassVar[int] = ...
        SEND_DRAW_TASK_EVENTS: ClassVar[int] = ...
        OVERFLOW_VISIBLE: ClassVar[int] = ...
        FLEX_IN_NEW_TRACK: ClassVar[int] = ...
        LAYOUT_1: ClassVar[int] = ...
        LAYOUT_2: ClassVar[int] = ...
        WIDGET_1: ClassVar[int] = ...
        WIDGET_2: ClassVar[int] = ...
        USER_1: ClassVar[int] = ...
        USER_2: ClassVar[int] = ...
        USER_3: ClassVar[int] = ...
        USER_4: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def center(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def style_get_selector_state(self, /) -> "state_t":
        """
        No Docstrings Yet
        """
        ...

    def style_get_selector_part(self, /) -> "part_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_min_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_max_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_height(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_min_height(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_max_height(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_length(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_x(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_y(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_align(self, part: int, /) -> "align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_height(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_translate_x(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_translate_y(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_scale_x(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_scale_y(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_rotation(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_pivot_x(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_pivot_y(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_skew_x(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_skew_y(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_pad_top(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_pad_bottom(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_pad_left(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_pad_right(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_pad_row(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_pad_column(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_margin_top(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_margin_bottom(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_margin_left(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_margin_right(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_grad_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_grad_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_grad_dir(self, part: int, /) -> "grad_dir_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_main_stop(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_grad_stop(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_main_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_grad_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_grad(self, part: int, /) -> "grad_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_image_src(self, part: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_image_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_image_recolor(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_image_recolor_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_image_recolor_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bg_image_tiled(self, part: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_style_border_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_border_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_border_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_border_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_border_side(self, part: int, /) -> "border_side_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_border_post(self, part: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_style_outline_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_outline_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_outline_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_outline_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_outline_pad(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_shadow_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_shadow_offset_x(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_shadow_offset_y(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_shadow_spread(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_shadow_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_shadow_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_shadow_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_image_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_image_recolor(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_image_recolor_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_image_recolor_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_line_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_line_dash_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_line_dash_gap(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_line_rounded(self, part: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_style_line_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_line_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_line_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_arc_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_arc_rounded(self, part: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_style_arc_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_arc_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_arc_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_arc_image_src(self, part: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_color(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_color_filtered(self, part: int, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_font(self, part: int, /) -> "font_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_letter_space(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_line_space(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_decor(self, part: int, /) -> "text_decor_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_text_align(self, part: int, /) -> "text_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_radius(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_clip_corner(self, part: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_style_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_opa_layered(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_color_filter_dsc(self, part: int, /) -> "color_filter_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_color_filter_opa(self, part: int, /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_anim(self, part: int, /) -> "anim_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_anim_duration(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transition(self, part: int, /) -> "style_transition_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_blend_mode(self, part: int, /) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_layout(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_base_dir(self, part: int, /) -> "base_dir_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_bitmap_mask_src(self, part: int, /) -> "image":
        """
        No Docstrings Yet
        """
        ...

    def get_style_rotary_sensitivity(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_flex_flow(self, part: int, /) -> "flex_flow_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_flex_main_place(self, part: int, /) -> "flex_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_flex_cross_place(self, part: int, /) -> "flex_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_flex_track_place(self, part: int, /) -> "flex_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_flex_grow(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_column_dsc_array(self, part: int, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_column_align(self, part: int, /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_row_dsc_array(self, part: int, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_row_align(self, part: int, /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_cell_column_pos(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_cell_x_align(self, part: int, /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_cell_column_span(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_cell_row_pos(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_cell_y_align(self, part: int, /) -> "grid_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_grid_cell_row_span(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_all(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_hor(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_ver(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_margin_all(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_margin_hor(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_margin_ver(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_gap(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_size(
        self,
        width: int,
        height: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_scale(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_style_space_left(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_space_right(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_space_top(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_space_bottom(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_scale_x_safe(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_style_transform_scale_y_safe(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def set_user_data(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_user_data(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def move_foreground(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def move_background(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_flow(self, flow: "flex_flow_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_align(
        self,
        main_place: "flex_align_t",
        cross_place: "flex_align_t",
        track_cross_place: "flex_align_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_flex_grow(self, grow: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_dsc_array(
        self,
        col_dsc: List[int],
        row_dsc: List[int],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_align(
        self,
        column_align: "grid_align_t",
        row_align: "grid_align_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_grid_cell(
        self,
        column_align: "grid_align_t",
        col_pos: int,
        col_span: int,
        row_align: "grid_align_t",
        row_pos: int,
        row_span: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def clean(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def delete_delayed(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def delete_anim_completed_cb(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def delete_async(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_parent(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def swap(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def move_to_index(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_screen(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_display(self, /) -> "display_t":
        """
        No Docstrings Yet
        """
        ...

    def get_parent(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_child(self, idx: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_child_by_type(self, idx: int, class_p: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_sibling(self, idx: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_sibling_by_type(self, idx: int, class_p: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_child_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_child_count_by_type(self, class_p: "obj", /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_index(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_index_by_type(self, class_p: "obj", /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def tree_walk(self, cb: Callable, start_obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def dump_tree(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pos(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_x(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_y(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_size(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def refr_size(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_width(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_height(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_content_width(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_content_height(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_layout(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def is_layout_positioned(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def mark_layout_as_dirty(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def update_layout(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_align(self, align: "align_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def align(self, align: "align_t", x_ofs: int, y_ofs: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def align_to(
        self,
        base: "obj",
        align: "align_t",
        x_ofs: int,
        y_ofs: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_coords(self, coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_x2(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_y2(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_x_aligned(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_y_aligned(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_content_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_content_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_content_coords(self, coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_self_width(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_self_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def refresh_self_size(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def refr_pos(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def move_to(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def move_children_by(
        self,
        x_diff: int,
        y_diff: int,
        ignore_floating: bool,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def transform_point(self, p: "point_t", flags: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def transform_point_array(
        self,
        points: List["point_t"],
        count: int,
        flags: "obj",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_transformed_area(self, area: "area_t", flags: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def invalidate_area(self, area: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def invalidate(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def area_is_visible(self, area: "area_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def is_visible(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_ext_click_area(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_click_area(self, coords: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def hit_test(self, point: "point_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_scrollbar_mode(self, mode: "scrollbar_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_scroll_dir(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_scroll_snap_x(self, align: "scroll_snap_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_scroll_snap_y(self, align: "scroll_snap_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_scrollbar_mode(self, /) -> "scrollbar_mode_t":
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_snap_x(self, /) -> "scroll_snap_t":
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_snap_y(self, /) -> "scroll_snap_t":
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_top(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_bottom(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_left(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_right(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scroll_end(self, end: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scroll_by(self, x: int, y: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scroll_by_bounded(
        self,
        x: int,
        y: int,
        anim_en: "anim_enable_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scroll_to(self, x: int, y: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scroll_to_x(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scroll_to_y(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scroll_to_view(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scroll_to_view_recursive(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def is_scrolling(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def update_snap(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_scrollbar_area(self, hor: "area_t", ver: "area_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def scrollbar_invalidate(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def readjust_scroll(self, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_style(
        self,
        style: "style_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def replace_style(
        self,
        old_style: "style_t",
        new_style: "style_t",
        selector: "style_selector_t",
        /
    ) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def remove_style(
        self,
        style: "style_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def remove_style_all(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def report_style_change(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def refresh_style(self, part: "part_t", prop: "style_prop_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def enable_style_refresh(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_style_prop(
        self,
        part: "part_t",
        prop: "style_prop_t",
        /
    ) -> "style_value_t":
        """
        No Docstrings Yet
        """
        ...

    def has_style_prop(
        self,
        selector: "style_selector_t",
        prop: "style_prop_t",
        /
    ) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def set_local_style_prop(
        self,
        prop: "style_prop_t",
        value: "style_value_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_local_style_prop(
        self,
        prop: "style_prop_t",
        value: "style_value_t",
        selector: "style_selector_t",
        /
    ) -> "style_res_t":
        """
        No Docstrings Yet
        """
        ...

    def remove_local_style_prop(
        self,
        prop: "style_prop_t",
        selector: "style_selector_t",
        /
    ) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def fade_in(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def fade_out(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_min_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_max_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_height(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_min_height(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_max_height(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_length(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_x(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_y(self, value: int, selector: "style_selector_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_align(
        self,
        value: "align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_height(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_translate_x(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_translate_y(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_scale_x(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_scale_y(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_rotation(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_pivot_x(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_pivot_y(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_skew_x(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transform_skew_y(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_top(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_bottom(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_left(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_right(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_row(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_pad_column(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_margin_top(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_margin_bottom(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_margin_left(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_margin_right(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_grad_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_grad_dir(
        self,
        value: "grad_dir_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_main_stop(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_grad_stop(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_main_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_grad_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_grad(
        self,
        value: "grad_dsc_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_image_src(
        self,
        value: Any,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_image_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_image_recolor(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_image_recolor_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bg_image_tiled(
        self,
        value: bool,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_border_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_border_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_border_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_border_side(
        self,
        value: "border_side_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_border_post(
        self,
        value: bool,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_outline_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_outline_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_outline_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_outline_pad(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_shadow_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_shadow_offset_x(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_shadow_offset_y(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_shadow_spread(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_shadow_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_shadow_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_image_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_image_recolor(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_image_recolor_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_line_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_line_dash_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_line_dash_gap(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_line_rounded(
        self,
        value: bool,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_line_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_line_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_arc_width(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_arc_rounded(
        self,
        value: bool,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_arc_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_arc_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_arc_image_src(
        self,
        value: Any,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_text_color(
        self,
        value: "color_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_text_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_text_font(
        self,
        value: "font_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_text_letter_space(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_text_line_space(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_text_decor(
        self,
        value: "text_decor_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_text_align(
        self,
        value: "text_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_radius(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_clip_corner(
        self,
        value: bool,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_opa_layered(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_color_filter_dsc(
        self,
        value: "color_filter_dsc_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_color_filter_opa(
        self,
        value: "opa_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_anim(
        self,
        value: "anim_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_anim_duration(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_transition(
        self,
        value: "style_transition_dsc_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_blend_mode(
        self,
        value: "blend_mode_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_layout(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_base_dir(
        self,
        value: "base_dir_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_bitmap_mask_src(
        self,
        value: "image",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_rotary_sensitivity(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_flex_flow(
        self,
        value: "flex_flow_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_flex_main_place(
        self,
        value: "flex_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_flex_cross_place(
        self,
        value: "flex_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_flex_track_place(
        self,
        value: "flex_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_flex_grow(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_column_dsc_array(
        self,
        value: List[int],
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_column_align(
        self,
        value: "grid_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_row_dsc_array(
        self,
        value: List[int],
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_row_align(
        self,
        value: "grid_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_cell_column_pos(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_cell_x_align(
        self,
        value: "grid_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_cell_column_span(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_cell_row_pos(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_cell_y_align(
        self,
        value: "grid_align_t",
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_style_grid_cell_row_span(
        self,
        value: int,
        selector: "style_selector_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def calculate_style_text_align(
        self,
        part: "part_t",
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "text_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_style_opa_recursive(self, part: "part_t", /) -> "opa_t":
        """
        No Docstrings Yet
        """
        ...

    def init_draw_rect_dsc(
        self,
        part: int,
        draw_dsc: "draw_rect_dsc_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def init_draw_label_dsc(
        self,
        part: int,
        draw_dsc: "draw_label_dsc_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def init_draw_image_dsc(
        self,
        part: int,
        draw_dsc: "draw_image_dsc_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def init_draw_line_dsc(
        self,
        part: int,
        draw_dsc: "draw_line_dsc_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def init_draw_arc_dsc(
        self,
        part: int,
        draw_dsc: "draw_arc_dsc_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def calculate_ext_draw_size(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def refresh_ext_draw_size(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def class_create_obj(self, parent: "obj", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def class_init_obj(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def is_editable(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def is_group_def(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def send_event(
        self,
        event_code: "event_code_t",
        param: Any,
        /
    ) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def event_base(self, e: "event_t", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def add_event_cb(
        self,
        event_cb: Callable,
        filter: "event_code_t",
        obj: "obj",
        /
    ) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def get_event_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_event_dsc(self, index: int, /) -> "event_dsc_t":
        """
        No Docstrings Yet
        """
        ...

    def remove_event(self, index: int, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def remove_event_cb(self, event_cb: Callable, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def remove_event_dsc(self, dsc: "event_dsc_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def remove_event_cb_with_user_data(
        self,
        event_cb: Callable,
        obj: "obj",
        /
    ) -> int:
        """
        No Docstrings Yet
        """
        ...

    def add_flag(self, f: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def remove_flag(self, f: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def update_flag(self, f: "obj", v: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_state(self, state: "state_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def remove_state(self, state: "state_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_state(self, state: "state_t", v: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def has_flag(self, f: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def has_flag_any(self, f: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_state(self, /) -> "state_t":
        """
        No Docstrings Yet
        """
        ...

    def has_state(self, state: "state_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_group(self, /) -> "group_t":
        """
        No Docstrings Yet
        """
        ...

    def allocate_spec_attr(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def check_type(self, class_p: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def has_class(self, class_p: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_class(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def is_valid(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def redraw(self, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def bind_flag_if_eq(
        self,
        subject: "subject_t",
        flag: "obj",
        ref_value: int,
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    def bind_flag_if_not_eq(
        self,
        subject: "subject_t",
        flag: "obj",
        ref_value: int,
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    def bind_state_if_eq(
        self,
        subject: "subject_t",
        state: "state_t",
        ref_value: int,
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...

    def bind_state_if_not_eq(
        self,
        subject: "subject_t",
        state: "state_t",
        ref_value: int,
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...


class image(obj):
    """
    No Docstrings Yet
    """

    class SRC(object):
        """
        No Docstrings Yet
        """
        VARIABLE: ClassVar[int] = ...
        FILE: ClassVar[int] = ...
        SYMBOL: ClassVar[int] = ...
        UNKNOWN: ClassVar[int] = ...

    class ALIGN(object):
        """
        No Docstrings Yet
        """
        DEFAULT: ClassVar[int] = ...
        TOP_LEFT: ClassVar[int] = ...
        TOP_MID: ClassVar[int] = ...
        TOP_RIGHT: ClassVar[int] = ...
        BOTTOM_LEFT: ClassVar[int] = ...
        BOTTOM_MID: ClassVar[int] = ...
        BOTTOM_RIGHT: ClassVar[int] = ...
        LEFT_MID: ClassVar[int] = ...
        RIGHT_MID: ClassVar[int] = ...
        CENTER: ClassVar[int] = ...
        STRETCH: ClassVar[int] = ...
        TILE: ClassVar[int] = ...

    class FLAGS(object):
        """
        No Docstrings Yet
        """
        PREMULTIPLIED: ClassVar[int] = ...
        COMPRESSED: ClassVar[int] = ...
        ALLOCATED: ClassVar[int] = ...
        MODIFIABLE: ClassVar[int] = ...
        USER1: ClassVar[int] = ...
        USER2: ClassVar[int] = ...
        USER3: ClassVar[int] = ...
        USER4: ClassVar[int] = ...
        USER5: ClassVar[int] = ...
        USER6: ClassVar[int] = ...
        USER7: ClassVar[int] = ...
        USER8: ClassVar[int] = ...

    class COMPRESS(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        RLE: ClassVar[int] = ...
        LZ4: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "image":
        """
        No Docstrings Yet
        """
        ...

    def buf_set_palette(self, id: int, c: "color32_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def buf_free(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def cache_drop(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def cache_resize(self, evict_now: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def header_cache_drop(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def header_cache_resize(self, evict_now: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_get_info(self, header: "image", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def decoder_open(self, src: Any, args: "image", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def decoder_get_area(
        self,
        full_area: "area_t",
        decoded_area: "area_t",
        /
    ) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def decoder_close(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_create(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...

    def decoder_delete(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_get_next(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...

    def decoder_set_info_cb(self, info_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_set_open_cb(self, open_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_set_get_area_cb(self, read_line_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_set_close_cb(self, close_cb: Callable, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_set_cache_free_cb(
        self,
        cache_free_cb: "cache_free_cb_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decoder_post_process(self, decoded: "draw_buf_t", /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    def src_get_type(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...

    def set_src(self, src: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_offset_x(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_offset_y(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_rotation(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_pivot(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_scale(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_scale_x(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_scale_y(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_blend_mode(self, blend_mode: "blend_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_antialias(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_inner_align(self, align: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bitmap_map_src(self, src: "image", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_src(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_offset_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_offset_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_rotation(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_pivot(self, end: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_scale(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scale_x(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_scale_y(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_blend_mode(self, /) -> "blend_mode_t":
        """
        No Docstrings Yet
        """
        ...

    def get_antialias(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_inner_align(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...

    def get_bitmap_map_src(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...


class animimg(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "animimg":
        """
        No Docstrings Yet
        """
        ...

    def set_src(self, dsc: Any, num: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def start(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_duration(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_repeat_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_src_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_duration(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_repeat_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...


class arc(obj):
    """
    No Docstrings Yet
    """

    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        REVERSE: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "arc":
        """
        No Docstrings Yet
        """
        ...

    def set_start_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_end_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_angles(
        self,
        start: "value_precise_t",
        end: "value_precise_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_start_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_end_angle(self, start: "value_precise_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_bg_angles(
        self,
        start: "value_precise_t",
        end: "value_precise_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_rotation(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_mode(self, type: "arc", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_change_rate(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_knob_offset(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_angle_start(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    def get_angle_end(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    def get_bg_angle_start(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    def get_bg_angle_end(self, /) -> "value_precise_t":
        """
        No Docstrings Yet
        """
        ...

    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_mode(self, /) -> "arc":
        """
        No Docstrings Yet
        """
        ...

    def get_rotation(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_knob_offset(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def align_obj_to_angle(self, obj_to_align: "obj", r_offset: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def rotate_obj_to_angle(
        self,
        obj_to_align: "obj",
        r_offset: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...


class label(obj):
    """
    No Docstrings Yet
    """

    class LONG(object):
        """
        No Docstrings Yet
        """
        WRAP: ClassVar[int] = ...
        DOT: ClassVar[int] = ...
        SCROLL: ClassVar[int] = ...
        SCROLL_CIRCULAR: ClassVar[int] = ...
        CLIP: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "label":
        """
        No Docstrings Yet
        """
        ...

    def set_text(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_static(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_long_mode(self, long_mode: "label", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_selection_start(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_selection_end(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_text(self, /) -> Union[str, bytearray, bytes, List[int]]:
        """
        No Docstrings Yet
        """
        ...

    def get_long_mode(self, /) -> "label":
        """
        No Docstrings Yet
        """
        ...

    def get_letter_pos(self, char_id: int, pos: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_letter_on(self, pos_in: "point_t", bidi: bool, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def is_char_under_pos(self, pos: "point_t", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_text_selection_start(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_text_selection_end(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def ins_text(
        self,
        pos: int,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def cut_text(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def bind_text(
        self,
        subject: "subject_t",
        fmt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...


class bar(obj):
    """
    No Docstrings Yet
    """

    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        RANGE: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "bar":
        """
        No Docstrings Yet
        """
        ...

    def set_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_start_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_mode(self, mode: "bar", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_start_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_mode(self, /) -> "bar":
        """
        No Docstrings Yet
        """
        ...

    def is_symmetrical(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...


class button(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "button":
        """
        No Docstrings Yet
        """
        ...

    def bind_checked(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...


class buttonmatrix(obj):
    """
    No Docstrings Yet
    """

    class CTRL(object):
        """
        No Docstrings Yet
        """
        HIDDEN: ClassVar[int] = ...
        NO_REPEAT: ClassVar[int] = ...
        DISABLED: ClassVar[int] = ...
        CHECKABLE: ClassVar[int] = ...
        CHECKED: ClassVar[int] = ...
        CLICK_TRIG: ClassVar[int] = ...
        POPOVER: ClassVar[int] = ...
        CUSTOM_1: ClassVar[int] = ...
        CUSTOM_2: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "buttonmatrix":
        """
        No Docstrings Yet
        """
        ...

    def set_map(
        self,
        map: List[Union[bytearray, bytes, str, List[int]]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_ctrl_map(self, ctrl_map: List["buttonmatrix"], /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_selected_button(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def clear_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_button_ctrl_all(self, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def clear_button_ctrl_all(self, ctrl: "buttonmatrix", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_button_width(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_one_checked(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_map(self, /) -> List[List[int]]:
        """
        No Docstrings Yet
        """
        ...

    def get_selected_button(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_button_text(self, btn_id: int, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def has_button_ctrl(self, btn_id: int, ctrl: "buttonmatrix", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_one_checked(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_popovers(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...


class calendar(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...

    def set_today_date(self, year: int, month: int, day: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_showed_date(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_highlighted_dates(
        self,
        highlighted: List["calendar"],
        date_num: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_day_names(
        self,
        day_names: List[Union[str, bytearray, bytes, List[int]]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_btnmatrix(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_today_date(self, /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...

    def get_showed_date(self, /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...

    def get_highlighted_dates(self, /) -> "calendar":
        """
        No Docstrings Yet
        """
        ...

    def get_highlighted_dates_num(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_pressed_date(self, date: "calendar", /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def header_dropdown_set_year_list(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...


class calendar_header_arrow(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "calendar_header_arrow":
        """
        No Docstrings Yet
        """
        ...


class calendar_header_dropdown(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "calendar_header_dropdown":
        """
        No Docstrings Yet
        """
        ...

    def header_dropdown_set_year_list(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...


class canvas(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "canvas":
        """
        No Docstrings Yet
        """
        ...

    def buf_size(self, h: int, bpp: int, stride: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def set_buffer(
        self,
        buf: Any,
        w: int,
        h: int,
        cf: "color_format_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_draw_buf(self, draw_buf: "draw_buf_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_px(self, x: int, y: int, color: "color_t", opa: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_palette(self, index: int, color: "color32_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_draw_buf(self, /) -> "draw_buf_t":
        """
        No Docstrings Yet
        """
        ...

    def get_px(self, x: int, y: int, /) -> "color32_t":
        """
        No Docstrings Yet
        """
        ...

    def get_image(self, /) -> "image":
        """
        No Docstrings Yet
        """
        ...

    def get_buf(self, /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def copy_buf(
        self,
        canvas_area: "area_t",
        dest_buf: "draw_buf_t",
        dest_area: "area_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def fill_bg(self, color: "color_t", opa: "opa_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def init_layer(self, layer: "layer_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def finish_layer(self, layer: "layer_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...


class chart(obj):
    """
    No Docstrings Yet
    """

    class TYPE(object):
        """
        No Docstrings Yet
        """
        NONE: ClassVar[int] = ...
        LINE: ClassVar[int] = ...
        BAR: ClassVar[int] = ...
        SCATTER: ClassVar[int] = ...

    class UPDATE_MODE(object):
        """
        No Docstrings Yet
        """
        SHIFT: ClassVar[int] = ...
        CIRCULAR: ClassVar[int] = ...

    class AXIS(object):
        """
        No Docstrings Yet
        """
        PRIMARY_Y: ClassVar[int] = ...
        SECONDARY_Y: ClassVar[int] = ...
        PRIMARY_X: ClassVar[int] = ...
        SECONDARY_X: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...

    def set_type(self, type: "chart", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_point_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_range(self, axis: "chart", min: int, max: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_update_mode(self, update_mode: "chart", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_div_line_count(self, hdiv: int, vdiv: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_type(self, /) -> "chart":
        """
        No Docstrings Yet
        """
        ...

    def get_point_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_x_start_point(self, ser: "chart", /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_point_pos_by_id(
        self,
        ser: "chart",
        id: int,
        p_out: "point_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def refresh(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_series(self, color: "color_t", axis: "chart", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...

    def remove_series(self, series: "chart", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def hide_series(self, series: "chart", hide: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_series_color(self, series: "chart", color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_x_start_point(self, ser: "chart", id: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_series_next(self, ser: "chart", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...

    def add_cursor(self, color: "color_t", dir: "dir_t", /) -> "chart":
        """
        No Docstrings Yet
        """
        ...

    def set_cursor_pos(self, cursor: "chart", pos: "point_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_cursor_point(
        self,
        cursor: "chart",
        ser: "chart",
        point_id: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_cursor_point(self, cursor: "chart", /) -> "point_t":
        """
        No Docstrings Yet
        """
        ...

    def set_all_value(self, ser: "chart", value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_next_value(self, ser: "chart", value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_next_value2(
        self,
        ser: "chart",
        x_value: int,
        y_value: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_value_by_id(self, ser: "chart", id: int, value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_value_by_id2(
        self,
        ser: "chart",
        id: int,
        x_value: int,
        y_value: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_ext_y_array(self, ser: "chart", array: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_ext_x_array(self, ser: "chart", array: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_y_array(self, ser: "chart", /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_x_array(self, ser: "chart", /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_pressed_point(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_first_point_center_offset(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...


class checkbox(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "checkbox":
        """
        No Docstrings Yet
        """
        ...

    def set_text(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_static(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_text(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...


class dropdown(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "dropdown":
        """
        No Docstrings Yet
        """
        ...

    def set_text(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_options(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_options_static(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_option(
        self,
        option: Union[str, bytearray, bytes, List[int]],
        pos: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def clear_options(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_selected(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_dir(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_symbol(self, src: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_selected_highlight(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_list(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_text(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_options(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_selected(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_option_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_selected_str(
        self,
        buf: Union[str, bytearray, bytes, List[int]],
        buf_size: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_option_index(
        self,
        option: Union[str, bytearray, bytes, List[int]],
        /
    ) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_symbol(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_selected_highlight(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_dir(self, /) -> "dir_t":
        """
        No Docstrings Yet
        """
        ...

    def open(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def close(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def is_open(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...


class imagebutton(obj):
    """
    No Docstrings Yet
    """

    class STATE(object):
        """
        No Docstrings Yet
        """
        RELEASED: ClassVar[int] = ...
        PRESSED: ClassVar[int] = ...
        DISABLED: ClassVar[int] = ...
        CHECKED_RELEASED: ClassVar[int] = ...
        CHECKED_PRESSED: ClassVar[int] = ...
        CHECKED_DISABLED: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "imagebutton":
        """
        No Docstrings Yet
        """
        ...

    def set_src(
        self,
        state: "imagebutton",
        src_left: Any,
        src_mid: Any,
        src_right: Any,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_src_left(self, state: "imagebutton", /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_src_middle(self, state: "imagebutton", /) -> Any:
        """
        No Docstrings Yet
        """
        ...

    def get_src_right(self, state: "imagebutton", /) -> Any:
        """
        No Docstrings Yet
        """
        ...


class keyboard(obj):
    """
    No Docstrings Yet
    """

    class MODE(object):
        """
        No Docstrings Yet
        """
        TEXT_LOWER: ClassVar[int] = ...
        TEXT_UPPER: ClassVar[int] = ...
        SPECIAL: ClassVar[int] = ...
        NUMBER: ClassVar[int] = ...
        USER_1: ClassVar[int] = ...
        USER_2: ClassVar[int] = ...
        USER_3: ClassVar[int] = ...
        USER_4: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "keyboard":
        """
        No Docstrings Yet
        """
        ...

    def get_map_array(self, /) -> List[List[int]]:
        """
        No Docstrings Yet
        """
        ...

    def get_selected_button(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_button_text(self, btn_id: int, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def set_textarea(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_mode(self, mode: "keyboard", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_popovers(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_map(
        self,
        mode: "keyboard",
        map: List[Union[bytearray, bytes, str, List[int]]],
        ctrl_map: List["buttonmatrix"],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_textarea(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_mode(self, /) -> "keyboard":
        """
        No Docstrings Yet
        """
        ...

    def def_event_cb(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class led(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "led":
        """
        No Docstrings Yet
        """
        ...

    def set_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_brightness(self, grow: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def on(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def off(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def toggle(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_brightness(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...


class line(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "line":
        """
        No Docstrings Yet
        """
        ...

    def set_points(
        self,
        points: List["point_precise_t"],
        point_num: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_y_invert(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_y_invert(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...


class list(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "list":
        """
        No Docstrings Yet
        """
        ...

    def add_text(
        self,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def add_button(
        self,
        icon: Any,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_button_text(self, btn: "obj", /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def set_button_text(
        self,
        btn: "obj",
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...


class menu(obj):
    """
    No Docstrings Yet
    """

    class HEADER(object):
        """
        No Docstrings Yet
        """
        TOP_FIXED: ClassVar[int] = ...
        TOP_UNFIXED: ClassVar[int] = ...
        BOTTOM_FIXED: ClassVar[int] = ...

    class ROOT_BACK_BUTTON(object):
        """
        No Docstrings Yet
        """
        DISABLED: ClassVar[int] = ...
        ENABLED: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "menu":
        """
        No Docstrings Yet
        """
        ...

    def set_page(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_page_title(
        self,
        title: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_page_title_static(
        self,
        title: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_sidebar_page(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_mode_header(self, mode: "menu", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_mode_root_back_button(self, mode: "menu", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_load_page_event(self, obj: "obj", page: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_cur_main_page(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_cur_sidebar_page(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_main_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_main_header_back_button(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_sidebar_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_sidebar_header_back_button(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def back_button_is_root(self, obj: "obj", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def clear_history(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class menu_page(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "menu_page":
        """
        No Docstrings Yet
        """
        ...


class menu_cont(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "menu_cont":
        """
        No Docstrings Yet
        """
        ...


class menu_section(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "menu_section":
        """
        No Docstrings Yet
        """
        ...


class menu_separator(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "menu_separator":
        """
        No Docstrings Yet
        """
        ...


class msgbox(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "msgbox":
        """
        No Docstrings Yet
        """
        ...

    def add_title(
        self,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def add_header_button(self, icon: Any, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def add_text(
        self,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def add_footer_button(
        self,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def add_close_button(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_footer(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_content(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_title(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def close(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def close_async(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class roller(obj):
    """
    No Docstrings Yet
    """

    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        INFINITE: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "roller":
        """
        No Docstrings Yet
        """
        ...

    def set_options(
        self,
        options: Union[str, bytearray, bytes, List[int]],
        mode: "roller",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_selected(self, sel_opt: int, anim: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_visible_row_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_selected(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_selected_str(
        self,
        buf: Union[str, bytearray, bytes, List[int]],
        buf_size: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_options(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_option_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...


class scale(obj):
    """
    No Docstrings Yet
    """

    class MODE(object):
        """
        No Docstrings Yet
        """
        HORIZONTAL_TOP: ClassVar[int] = ...
        HORIZONTAL_BOTTOM: ClassVar[int] = ...
        VERTICAL_LEFT: ClassVar[int] = ...
        VERTICAL_RIGHT: ClassVar[int] = ...
        ROUND_INNER: ClassVar[int] = ...
        ROUND_OUTER: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "scale":
        """
        No Docstrings Yet
        """
        ...

    def set_mode(self, mode: "scale", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_total_tick_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_major_tick_every(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_label_show(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_angle_range(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_rotation(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_line_needle_value(
        self,
        needle_line: "obj",
        needle_length: int,
        value: int,
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_image_needle_value(self, needle_img: "obj", value: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_src(
        self,
        map: List[Union[bytearray, bytes, str, List[int]]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_post_draw(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_section(self, /) -> "scale":
        """
        No Docstrings Yet
        """
        ...

    def section_set_range(self, minor_range: int, major_range: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def section_set_style(
        self,
        part: int,
        section_part_style: "style_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_mode(self, /) -> "scale":
        """
        No Docstrings Yet
        """
        ...

    def get_total_tick_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_major_tick_every(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_label_show(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_angle_range(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_range_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_range_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...


class slider(obj):
    """
    No Docstrings Yet
    """

    class MODE(object):
        """
        No Docstrings Yet
        """
        NORMAL: ClassVar[int] = ...
        SYMMETRICAL: ClassVar[int] = ...
        RANGE: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "slider":
        """
        No Docstrings Yet
        """
        ...

    def set_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_left_value(self, x: int, anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_mode(self, mode: "slider", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_left_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_min_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_max_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_mode(self, /) -> "slider":
        """
        No Docstrings Yet
        """
        ...

    def is_symmetrical(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def is_dragged(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def bind_value(self, subject: "subject_t", /) -> "observer_t":
        """
        No Docstrings Yet
        """
        ...


class spangroup(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "spangroup":
        """
        No Docstrings Yet
        """
        ...

    def new_span(self, /) -> "span_t":
        """
        No Docstrings Yet
        """
        ...

    def delete_span(self, span: "span_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_overflow(self, overflow: "span_overflow_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_indent(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_mode(self, mode: "span_mode_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_max_lines(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_span_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_align(self, /) -> "text_align_t":
        """
        No Docstrings Yet
        """
        ...

    def get_overflow(self, /) -> "span_overflow_t":
        """
        No Docstrings Yet
        """
        ...

    def get_indent(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_mode(self, /) -> "span_mode_t":
        """
        No Docstrings Yet
        """
        ...

    def get_max_lines(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_max_line_height(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_expand_width(self, max_width: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_expand_height(self, width: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def refr_mode(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class textarea(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "textarea":
        """
        No Docstrings Yet
        """
        ...

    def add_char(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_text(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def delete_char(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def delete_char_forward(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_placeholder_text(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_cursor_pos(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_cursor_click_pos(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_password_mode(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_password_bullet(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_one_line(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_accepted_chars(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_max_length(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_insert_replace(
        self,
        text: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_text_selection(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_password_show_time(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_text(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_placeholder_text(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_label(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_cursor_pos(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_cursor_click_pos(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_password_mode(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_password_bullet(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_one_line(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_accepted_chars(self, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_max_length(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def text_is_selected(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_text_selection(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_password_show_time(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_current_char(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def clear_selection(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def cursor_right(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def cursor_left(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def cursor_down(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def cursor_up(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class spinbox(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "spinbox":
        """
        No Docstrings Yet
        """
        ...

    def set_value(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_rollover(self, antialias: bool, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_digit_format(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_step(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_range(self, x: int, y: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_cursor_pos(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_digit_step_direction(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_rollover(self, /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_value(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_step(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def step_next(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def step_prev(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def increment(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def decrement(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class spinner(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "spinner":
        """
        No Docstrings Yet
        """
        ...

    def set_anim_params(self, time: int, delay: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class switch(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "switch":
        """
        No Docstrings Yet
        """
        ...


class table(obj):
    """
    No Docstrings Yet
    """

    class CELL_CTRL(object):
        """
        No Docstrings Yet
        """
        MERGE_RIGHT: ClassVar[int] = ...
        TEXT_CROP: ClassVar[int] = ...
        CUSTOM_1: ClassVar[int] = ...
        CUSTOM_2: ClassVar[int] = ...
        CUSTOM_3: ClassVar[int] = ...
        CUSTOM_4: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "table":
        """
        No Docstrings Yet
        """
        ...

    def set_cell_value(
        self,
        row: int,
        col: int,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_row_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_column_count(self, delay_ms: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_column_width(self, col_id: int, w: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def add_cell_ctrl(self, row: int, col: int, ctrl: "table", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def clear_cell_ctrl(self, row: int, col: int, ctrl: "table", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_cell_user_data(self, row: int, col: int, obj: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_cell_value(self, row: int, col: int, /) -> List[int]:
        """
        No Docstrings Yet
        """
        ...

    def get_row_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_column_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_column_width(self, part: int, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def has_cell_ctrl(self, row: int, col: int, ctrl: "table", /) -> bool:
        """
        No Docstrings Yet
        """
        ...

    def get_selected_cell(self, row: List[int], col: List[int], /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_cell_user_data(self, row: int, col: int, /) -> Any:
        """
        No Docstrings Yet
        """
        ...


class tabview(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "tabview":
        """
        No Docstrings Yet
        """
        ...

    def add_tab(self, txt: Union[str, bytearray, bytes, List[int]], /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def rename_tab(
        self,
        pos: int,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_active(self, sel_opt: int, anim: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_tab_bar_position(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_tab_bar_size(self, index: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_tab_count(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_tab_active(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...

    def get_content(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_tab_bar(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...


class tileview(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "tileview":
        """
        No Docstrings Yet
        """
        ...

    def add_tile(self, col_id: int, row_id: int, dir: "dir_t", /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def set_tile(self, tile_obj: "obj", anim_en: "anim_enable_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_tile_by_index(
        self,
        col_id: int,
        row_id: int,
        anim_en: "anim_enable_t",
        /
    ) -> None:
        """
        No Docstrings Yet
        """
        ...

    def get_tile_active(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...


class win(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "win":
        """
        No Docstrings Yet
        """
        ...

    def add_title(
        self,
        txt: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def add_button(self, icon: Any, btn_w: int, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_header(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def get_content(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...


class ime_pinyin(obj):
    """
    No Docstrings Yet
    """

    class PINYIN_MODE(object):
        """
        No Docstrings Yet
        """
        K26: ClassVar[int] = ...
        K9: ClassVar[int] = ...
        K9_NUMBER: ClassVar[int] = ...

    def __init__(self, parent: "obj", /) -> "ime_pinyin":
        """
        No Docstrings Yet
        """
        ...

    def pinyin_set_keyboard(self, parent: "obj", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def pinyin_set_dict(self, dict: "pinyin_dict_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def pinyin_set_mode(self, mode: "ime_pinyin", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def pinyin_get_kb(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def pinyin_get_cand_panel(self, /) -> "obj":
        """
        No Docstrings Yet
        """
        ...

    def pinyin_get_dict(self, /) -> "pinyin_dict_t":
        """
        No Docstrings Yet
        """
        ...


class barcode(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "barcode":
        """
        No Docstrings Yet
        """
        ...

    def set_dark_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_light_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_scale(self, scale: int, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_direction(self, dir: "dir_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def update(
        self,
        data: Union[str, bytearray, bytes, List[int]],
        /
    ) -> "result_t":
        """
        No Docstrings Yet
        """
        ...

    def get_dark_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_light_color(self, /) -> "color_t":
        """
        No Docstrings Yet
        """
        ...

    def get_scale(self, /) -> int:
        """
        No Docstrings Yet
        """
        ...


class gif(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "gif":
        """
        No Docstrings Yet
        """
        ...

    def set_src(self, src: Any, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def restart(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def pause(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def resume(self, /) -> None:
        """
        No Docstrings Yet
        """
        ...


class qrcode(obj):
    """
    No Docstrings Yet
    """

    def __init__(self, parent: "obj", /) -> "qrcode":
        """
        No Docstrings Yet
        """
        ...

    def set_dark_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def set_light_color(self, color: "color_t", /) -> None:
        """
        No Docstrings Yet
        """
        ...

    def update(self, data: Any, data_len: int, /) -> "result_t":
        """
        No Docstrings Yet
        """
        ...


class obj_class(object):
    """
    No Docstrings Yet
    """
    ...


class image_class(object):
    """
    No Docstrings Yet
    """
    ...


class animimg_class(object):
    """
    No Docstrings Yet
    """
    ...


class arc_class(object):
    """
    No Docstrings Yet
    """
    ...


class label_class(object):
    """
    No Docstrings Yet
    """
    ...


class bar_class(object):
    """
    No Docstrings Yet
    """
    ...


class button_class(object):
    """
    No Docstrings Yet
    """
    ...


class buttonmatrix_class(object):
    """
    No Docstrings Yet
    """
    ...


class calendar_class(object):
    """
    No Docstrings Yet
    """
    ...


class calendar_header_arrow_class(object):
    """
    No Docstrings Yet
    """
    ...


class calendar_header_dropdown_class(object):
    """
    No Docstrings Yet
    """
    ...


class canvas_class(object):
    """
    No Docstrings Yet
    """
    ...


class chart_class(object):
    """
    No Docstrings Yet
    """
    ...


class checkbox_class(object):
    """
    No Docstrings Yet
    """
    ...


class dropdown_class(object):
    """
    No Docstrings Yet
    """
    ...


class imagebutton_class(object):
    """
    No Docstrings Yet
    """
    ...


class keyboard_class(object):
    """
    No Docstrings Yet
    """
    ...


class led_class(object):
    """
    No Docstrings Yet
    """
    ...


class line_class(object):
    """
    No Docstrings Yet
    """
    ...


class list_class(object):
    """
    No Docstrings Yet
    """
    ...


class menu_class(object):
    """
    No Docstrings Yet
    """
    ...


class menu_page_class(object):
    """
    No Docstrings Yet
    """
    ...


class menu_cont_class(object):
    """
    No Docstrings Yet
    """
    ...


class menu_section_class(object):
    """
    No Docstrings Yet
    """
    ...


class menu_separator_class(object):
    """
    No Docstrings Yet
    """
    ...


class msgbox_class(object):
    """
    No Docstrings Yet
    """
    ...


class roller_class(object):
    """
    No Docstrings Yet
    """
    ...


class scale_class(object):
    """
    No Docstrings Yet
    """
    ...


class slider_class(object):
    """
    No Docstrings Yet
    """
    ...


class spangroup_class(object):
    """
    No Docstrings Yet
    """
    ...


class textarea_class(object):
    """
    No Docstrings Yet
    """
    ...


class spinbox_class(object):
    """
    No Docstrings Yet
    """
    ...


class spinner_class(object):
    """
    No Docstrings Yet
    """
    ...


class switch_class(object):
    """
    No Docstrings Yet
    """
    ...


class table_class(object):
    """
    No Docstrings Yet
    """
    ...


class tabview_class(object):
    """
    No Docstrings Yet
    """
    ...


class tileview_class(object):
    """
    No Docstrings Yet
    """
    ...


class win_class(object):
    """
    No Docstrings Yet
    """
    ...


class ime_pinyin_class(object):
    """
    No Docstrings Yet
    """
    ...


class barcode_class(object):
    """
    No Docstrings Yet
    """
    ...


class gif_class(object):
    """
    No Docstrings Yet
    """
    ...


class qrcode_class(object):
    """
    No Docstrings Yet
    """
    ...


color_filter_shade: "color_filter_dsc_t" = ...
cache_class_lru_rb_count: "cache_class_t" = ...
cache_class_lru_rb_size: "cache_class_t" = ...
font_montserrat_12: "font_t" = ...
font_montserrat_14: "font_t" = ...
font_montserrat_16: "font_t" = ...
style_const_prop_id_inv: "_mp_int_wrapper" = ...
_nesting: "_mp_int_wrapper" = ...


def memzero(dst: Any, len: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_handler_run_in_period(period: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def trigo_cos(angle: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def bezier3(t: int, u0: int, u1: int, u2: int, u3: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def pct(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def pct_to_px(v: int, base: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_format_get_size(cf: "color_format_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_hex(c: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_make(r: int, g: int, b: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color32_make(r: int, g: int, b: int, a: int, /) -> "color32_t":
    """
    No Docstrings Yet
    """
    ...


def color_hex3(c: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_16_16_mix(c1: int, c2: int, mix: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_white() -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_black() -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def font_default() -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def bidi_calculate_align(
    align: "text_align_t",
    base_dir: "base_dir_t",
    txt: Union[str, bytearray, bytes, List[int]],
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def grid_fr(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def style_prop_has_flag(prop: "style_prop_t", flag: int, /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def screen_active() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def layer_top() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def layer_sys() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def layer_bottom() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def dpx(x: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def snapshot_free(dsc: "image", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def snapshot_take_to_buf(
    obj: "obj",
    cf: "color_format_t",
    dsc: "image",
    buf: Any,
    buf_size: int,
    /
) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def task_handler() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_major() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_minor() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_patch() -> int:
    """
    No Docstrings Yet
    """
    ...


def version_info() -> List[int]:
    """
    No Docstrings Yet
    """
    ...


def mp_lv_init_gc() -> None:
    """
    No Docstrings Yet
    """
    ...


def init() -> None:
    """
    No Docstrings Yet
    """
    ...


def deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def is_initialized() -> bool:
    """
    No Docstrings Yet
    """
    ...


def strlen(str: Union[str, bytearray, bytes, List[int]], /) -> int:
    """
    No Docstrings Yet
    """
    ...


def strncpy(
    strDest: Union[str, bytearray, bytes, List[int]],
    strSource: Union[str, bytearray, bytes, List[int]],
    count: int,
    /
) -> Union[str, bytearray, bytes, List[int]]:
    """
    No Docstrings Yet
    """
    ...


def strcpy(
    strDestination: Union[str, bytearray, bytes, List[int]],
    strSource: Union[str, bytearray, bytes, List[int]],
    /
) -> Union[str, bytearray, bytes, List[int]]:
    """
    No Docstrings Yet
    """
    ...


def mem_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def mem_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def mem_add_pool(mem: Any, bytes: int, /) -> "mem_pool_t":
    """
    No Docstrings Yet
    """
    ...


def mem_remove_pool(pool: "mem_pool_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def malloc(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def malloc_zeroed(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def free(data: Any, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def realloc(data_p: Any, new_size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def malloc_core(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def free_core(data: Any, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def realloc_core(data_p: Any, new_size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def mem_test_core() -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def mem_test() -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def memcpy(dst: Any, src: Any, len: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def memset(dst: Any, v: int, len: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def memmove(dst: Any, src: Any, len: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def strcmp(
    s1: Union[str, bytearray, bytes, List[int]],
    s2: Union[str, bytearray, bytes, List[int]],
    /
) -> int:
    """
    No Docstrings Yet
    """
    ...


def strdup(src: Union[str, bytearray, bytes, List[int]], /) -> Union[
    str, bytearray, bytes, List[int]]:
    """
    No Docstrings Yet
    """
    ...


def tick_inc(ms: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def tick_get() -> int:
    """
    No Docstrings Yet
    """
    ...


def tick_elaps(period: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def delay_ms(ms: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def tick_set_cb(cb: "tick_get_cb_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def delay_set_cb(cb: "delay_cb_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_handler() -> int:
    """
    No Docstrings Yet
    """
    ...


def timer_periodic_handler() -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_handler_set_resume_cb(
    cb: "timer_handler_resume_cb_t",
    data: Any,
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_create_basic() -> "timer_t":
    """
    No Docstrings Yet
    """
    ...


def timer_create(
    user_data: Any,
    period: int,
    timer_xcb: Callable,
    /
) -> "timer_t":
    """
    No Docstrings Yet
    """
    ...


def timer_enable(en: bool, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def timer_get_idle() -> int:
    """
    No Docstrings Yet
    """
    ...


def timer_get_time_until_next() -> int:
    """
    No Docstrings Yet
    """
    ...


def trigo_sin(angle: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def cubic_bezier(x: int, x1: int, y1: int, x2: int, y2: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def atan2(x: int, y: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def sqrt(x: int, q: "sqrt_res_t", mask: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def pow(base: int, exp: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def map(x: int, x1: int, y1: int, x2: int, y2: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def rand_set_seed(ms: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def rand(min: int, max: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def async_call(user_data: Any, async_xcb: Callable, /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def async_call_cancel(user_data: Any, async_xcb: Callable, /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def anim_delete(var: Any, exec_cb: "anim_exec_xcb_t", /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def anim_delete_all() -> None:
    """
    No Docstrings Yet
    """
    ...


def anim_get(var: Any, exec_cb: "anim_exec_xcb_t", /) -> "anim_t":
    """
    No Docstrings Yet
    """
    ...


def anim_get_timer() -> "timer_t":
    """
    No Docstrings Yet
    """
    ...


def anim_count_running() -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_speed(period: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_speed_clamped(speed: int, min_time: int, max_time: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def anim_refr_now() -> None:
    """
    No Docstrings Yet
    """
    ...


def anim_timeline_create() -> "anim_timeline_t":
    """
    No Docstrings Yet
    """
    ...


def color_format_get_bpp(cf: "color_format_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def color_format_has_alpha(src_cf: "color_format_t", /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def color_hsv_to_rgb(h: int, s: int, v: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def color_rgb_to_hsv(r8: int, g8: int, b8: int, /) -> "color_hsv_t":
    """
    No Docstrings Yet
    """
    ...


def palette_main(p: "palette_t", /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def palette_lighten(p: "palette_t", lvl: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def palette_darken(p: "palette_t", lvl: int, /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def draw_buf_get_handlers() -> "draw_buf_handlers_t":
    """
    No Docstrings Yet
    """
    ...


def draw_buf_align(buf: Any, color_format: "color_format_t", /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_buf_width_to_stride(w: int, color_format: "color_format_t", /) -> int:
    """
    No Docstrings Yet
    """
    ...


def draw_buf_create(
    w: int,
    h: int,
    cf: "color_format_t",
    stride: int,
    /
) -> "draw_buf_t":
    """
    No Docstrings Yet
    """
    ...


def thread_init(
    user_data: Any,
    prio: "thread_prio_t",
    callback: Callable,
    stack_size: int,
    thread: "thread_t",
    /
) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def thread_delete(thread: "thread_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def mutex_init(mutex: "mutex_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def mutex_lock(mutex: "mutex_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def mutex_lock_isr(mutex: "mutex_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def mutex_unlock(mutex: "mutex_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def mutex_delete(mutex: "mutex_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def thread_sync_init(sync: "thread_sync_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def thread_sync_wait(sync: "thread_sync_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def thread_sync_signal(sync: "thread_sync_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def thread_sync_delete(sync: "thread_sync_t", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def cache_entry_get_size(node_size: int, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def cache_entry_get_entry(data: Any, node_size: int, /) -> "cache_entry_t":
    """
    No Docstrings Yet
    """
    ...


def cache_entry_alloc(node_size: int, cache: "cache_t", /) -> "cache_entry_t":
    """
    No Docstrings Yet
    """
    ...


def text_get_size(
    size_res: "point_t",
    text: Union[str, bytearray, bytes, List[int]],
    font: "font_t",
    letter_space: int,
    line_space: int,
    max_width: int,
    flag: "text_flag_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def text_get_width(
    txt: Union[str, bytearray, bytes, List[int]],
    length: int,
    font: "font_t",
    letter_space: int,
    /
) -> int:
    """
    No Docstrings Yet
    """
    ...


def layout_register(user_data: Any, cb: Callable, /) -> int:
    """
    No Docstrings Yet
    """
    ...


def flex_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def grid_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def style_register_prop(flag: int, /) -> "style_prop_t":
    """
    No Docstrings Yet
    """
    ...


def style_get_num_custom_props() -> "style_prop_t":
    """
    No Docstrings Yet
    """
    ...


def style_prop_get_default(prop: "style_prop_t", /) -> "style_value_t":
    """
    No Docstrings Yet
    """
    ...


def event_register_id() -> int:
    """
    No Docstrings Yet
    """
    ...


def fs_get_drv(letter: Union[int, str, bytes, bytearray], /) -> "fs_drv_t":
    """
    No Docstrings Yet
    """
    ...


def fs_is_ready(letter: Union[int, str, bytes, bytearray], /) -> bool:
    """
    No Docstrings Yet
    """
    ...


def fs_get_letters(buf: Union[str, bytearray, bytes, List[int]], /) -> Union[
    str, bytearray, bytes, List[int]]:
    """
    No Docstrings Yet
    """
    ...


def fs_get_ext(fn: Union[str, bytearray, bytes, List[int]], /) -> List[int]:
    """
    No Docstrings Yet
    """
    ...


def fs_up(buf: Union[str, bytearray, bytes, List[int]], /) -> Union[
    str, bytearray, bytes, List[int]]:
    """
    No Docstrings Yet
    """
    ...


def fs_get_last(fn: Union[str, bytearray, bytes, List[int]], /) -> List[int]:
    """
    No Docstrings Yet
    """
    ...


def draw_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_create_unit(size: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_add_task(layer: "layer_t", coords: "area_t", /) -> "draw_task_t":
    """
    No Docstrings Yet
    """
    ...


def draw_finalize_task_creation(layer: "layer_t", t: "draw_task_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_dispatch() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_dispatch_wait_for_request() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_dispatch_request() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_get_next_available_task(
    layer: "layer_t",
    t_prev: "draw_task_t",
    draw_unit_id: int,
    /
) -> "draw_task_t":
    """
    No Docstrings Yet
    """
    ...


def draw_layer_create(
    parent_layer: "layer_t",
    color_format: "color_format_t",
    area: "area_t",
    /
) -> "layer_t":
    """
    No Docstrings Yet
    """
    ...


def draw_layer_alloc_buf(layer: "layer_t", /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_layer_go_to_xy(layer: "layer_t", x: int, y: int, /) -> Any:
    """
    No Docstrings Yet
    """
    ...


def draw_rect(
    layer: "layer_t",
    dsc: "draw_rect_dsc_t",
    coords: "area_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_label(
    layer: "layer_t",
    dsc: "draw_label_dsc_t",
    coords: "area_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_character(
    layer: "layer_t",
    dsc: "draw_label_dsc_t",
    point: "point_t",
    unicode_letter: int,
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_image(
    layer: "layer_t",
    dsc: "draw_image_dsc_t",
    coords: "area_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_layer(
    layer: "layer_t",
    dsc: "draw_image_dsc_t",
    coords: "area_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_arc(layer: "layer_t", dsc: "draw_arc_dsc_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_arc_get_area(
    x: int,
    y: int,
    radius: int,
    start_angle: "value_precise_t",
    end_angle: "value_precise_t",
    w: int,
    rounded: bool,
    area: "area_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_line(layer: "layer_t", dsc: "draw_line_dsc_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_triangle(layer: "layer_t", draw_dsc: "draw_triangle_dsc_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_mask_rect(layer: "layer_t", dsc: "draw_mask_rect_dsc_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def display_create(hor_res: int, ver_res: int, /) -> "display_t":
    """
    No Docstrings Yet
    """
    ...


def display_get_default() -> "display_t":
    """
    No Docstrings Yet
    """
    ...


def screen_load(scr: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def screen_load_anim(
    scr: "obj",
    anim_type: "screen_load_anim_t",
    time: int,
    delay: int,
    auto_del: bool,
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def clamp_width(
    width: int,
    min_width: int,
    max_width: int,
    ref_width: int,
    /
) -> int:
    """
    No Docstrings Yet
    """
    ...


def clamp_height(
    width: int,
    min_width: int,
    max_width: int,
    ref_width: int,
    /
) -> int:
    """
    No Docstrings Yet
    """
    ...


def group_create() -> "group_t":
    """
    No Docstrings Yet
    """
    ...


def group_get_default() -> "group_t":
    """
    No Docstrings Yet
    """
    ...


def group_swap_obj(obj: "obj", parent: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def group_remove_obj(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def group_focus_obj(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def group_get_count() -> int:
    """
    No Docstrings Yet
    """
    ...


def group_by_index(index: int, /) -> "group_t":
    """
    No Docstrings Yet
    """
    ...


def indev_create() -> "indev_t":
    """
    No Docstrings Yet
    """
    ...


def indev_read_timer_cb(arg0: "timer_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def indev_active() -> "indev_t":
    """
    No Docstrings Yet
    """
    ...


def indev_get_active_obj() -> "obj":
    """
    No Docstrings Yet
    """
    ...


def indev_search_obj(obj: "obj", point: "point_t", /) -> "obj":
    """
    No Docstrings Yet
    """
    ...


def refr_now(disp: "display_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def binfont_create(
    font_name: Union[str, bytearray, bytes, List[int]],
    /
) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def binfont_destroy(font: "font_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def span_stack_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def span_stack_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def snapshot_take(obj: "obj", cf: "color_format_t", /) -> "draw_buf_t":
    """
    No Docstrings Yet
    """
    ...


def snapshot_create_draw_buf(
    obj: "obj",
    cf: "color_format_t",
    /
) -> "draw_buf_t":
    """
    No Docstrings Yet
    """
    ...


def snapshot_reshape_draw_buf(
    obj: "obj",
    draw_buf: "draw_buf_t",
    /
) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def snapshot_take_to_draw_buf(
    obj: "obj",
    cf: "color_format_t",
    draw_buf: "draw_buf_t",
    /
) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def gridnav_add(obj: "obj", ctrl: "gridnav_ctrl_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def gridnav_remove(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def gridnav_set_focused(
    tv: "obj",
    tile_obj: "obj",
    anim_en: "anim_enable_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def imgfont_create(
    user_data: Any,
    path_cb: Callable,
    height: int,
    /
) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def imgfont_destroy(font: "font_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_info(
    decoder: "image",
    src: Any,
    header: "image",
    /
) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_get_area(
    decoder: "image",
    dsc: "image",
    full_area: "area_t",
    decoded_area: "area_t",
    /
) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_open(decoder: "image", dsc: "image", /) -> "result_t":
    """
    No Docstrings Yet
    """
    ...


def bin_decoder_close(decoder: "image", dsc: "image", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def bmp_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def bmp_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def lodepng_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def lodepng_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def gd_open_gif_file(
    fname: Union[str, bytearray, bytes, List[int]],
    /
) -> "gd_GIF":
    """
    No Docstrings Yet
    """
    ...


def gd_open_gif_data(data: Any, /) -> "gd_GIF":
    """
    No Docstrings Yet
    """
    ...


def tjpgd_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def tjpgd_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_create_file(
    path: Union[str, bytearray, bytes, List[int]],
    font_size: int,
    /
) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_create_file_ex(
    path: Union[str, bytearray, bytes, List[int]],
    font_size: int,
    cache_size: int,
    /
) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_create_data(
    data: Any,
    data_size: int,
    font_size: int,
    /
) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_create_data_ex(
    data: Any,
    data_size: int,
    font_size: int,
    cache_size: int,
    /
) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_set_size(font: "font_t", font_size: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def tiny_ttf_destroy(font: "font_t", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def theme_get_from_obj(obj: "obj", /) -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_apply(obj: "obj", /) -> None:
    """
    No Docstrings Yet
    """
    ...


def theme_get_font_small(obj: "obj", /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_font_normal(obj: "obj", /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_font_large(obj: "obj", /) -> "font_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_color_primary(obj: "obj", /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def theme_get_color_secondary(obj: "obj", /) -> "color_t":
    """
    No Docstrings Yet
    """
    ...


def theme_default_init(
    disp: "display_t",
    color_primary: "color_t",
    color_secondary: "color_t",
    dark: bool,
    font: "font_t",
    /
) -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_default_get() -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_default_is_inited() -> bool:
    """
    No Docstrings Yet
    """
    ...


def theme_default_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def theme_simple_init(disp: "display_t", /) -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_simple_is_inited() -> bool:
    """
    No Docstrings Yet
    """
    ...


def theme_simple_get() -> "theme_t":
    """
    No Docstrings Yet
    """
    ...


def theme_simple_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_rgb565_swap(buf: Any, buf_size_px: int, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_rotate(
    src: Any,
    dest: Any,
    src_width: int,
    src_height: int,
    src_sride: int,
    dest_stride: int,
    rotation: "display_rotation_t",
    color_format: "color_format_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_mask_init() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_mask_deinit() -> None:
    """
    No Docstrings Yet
    """
    ...


def draw_sw_mask_apply(
    masks: Any,
    mask_buf: "opa_t",
    abs_x: int,
    abs_y: int,
    len: int,
    /
) -> "draw_sw_mask_res_t":
    """
    No Docstrings Yet
    """
    ...


def draw_sw_mask_free_param(data: Any, /) -> None:
    """
    No Docstrings Yet
    """
    ...


def conical_gradient(
    buf: Union[bytearray, bytes, List[int]],
    radius: int,
    grad: "grad_dsc_t",
    angle: int,
    twist: int,
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def radial_gradient(
    buf: Union[bytearray, bytes, List[int]],
    radius: int,
    grad: "grad_dsc_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...


def rgb565_dither(
    buf: Union[bytearray, bytes, List[int]],
    width: int,
    height: int,
    format: "color_format_t",
    /
) -> None:
    """
    No Docstrings Yet
    """
    ...
