import stylesheet as style

MAIN_LINE_EDIT = f"QLineEdit {{font: 15px; color: {style.FONT_COLOR}; background-color: {style.DARK_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}}}"

BIG_BUTTONS = f"QWidget {{font: 18px; color: {style.FONT_COLOR}; background-color: {style.DARK_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}}}"

ICON_LABEL = f"QWidget {{background-color: {style.DARK_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}}}"

SMALL_BUTTONS = f"QPushButton {{font: 12px; color: {style.FONT_COLOR}; background-color: {style.DARK_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}}}"

SMALL_FADED_BUTTONS = f"QPushButton {{font: 12px; color: {style.DISABLED_COLOR2}; background-color: {style.DARK_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}}}"


SUB_LABEL = f"QLabel {{font: 10px; color: {style.DISABLED_COLOR2}; background-color: {style.DARK_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}}}"

STAT_LABEL = f"QWidget {{font: 10px; color: {style.DISABLED_COLOR3}; background-color: {style.DARK_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}}}"


PLAYER_TOP_LABEL = f"QLabel {{background-color: {style.PLAYER_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}; border-top-right-radius: {style.RADIUS}px; border-top-left-radius: {style.RADIUS}}}"
PLAYER_BOTTOM_LABEL = f"QLabel {{background-color: {style.PLAYER_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}; border-bottom-right-radius: {style.RADIUS}; border-bottom-left-radius: {style.RADIUS}}}"

CREATURE_TOP_LABEL = f"QLabel {{background-color: {style.CREATURE_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}; border-top-right-radius: 3px; border-top-left-radius: 3px}}"
CREATURE_BOTTOM_LABEL = f"QLabel {{background-color: {style.CREATURE_COLOR}; border: 0px solid {style.BORDER_COLOR_LIGHT}; border-bottom-right-radius: 3px; border-bottom-left-radius: 3px}}"