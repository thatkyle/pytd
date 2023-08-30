from constants import *

STYLES = {
    "base_font": None, # Used as font argument for pygame.font.SysFont(font, font_size) to initialize default pygame font
    "shop_button": {
        "height": 30,
        "width": 40,
        "right_margin": 10,
        "bottom_margin": 10,
        "font_size": 14,
        "font_color": WHITE
    },
    "gold_counter": {
        "abs_pos": (SCREEN_WIDTH - 150, 10),
        "font_size": 36,
        "font_color": GOLD
    }
}
