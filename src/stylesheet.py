RADIUS = "6px"

SATURATION = "1%"

TEXT_MID_COLOR = "hsl(0, 0%, 40%)"	
TEXT_DARK_COLOR = "hsl(0, 0%, 25%)"	
TEXT_BLACK_COLOR = "hsl(0, 0%, 5%)"	

INJURY_RED = "#330000"
INJURY_RED_BRIGHT = "#800000"
INJURY_RED_DARK = "#2b0000"

DARK_COLOR = f"hsl(0, {SATURATION}, 10%)"
MID_COLOR = "hsl(0, 0%, 25%)"


DIM_WHITE_LIGHT = "hsl(0, 0%, 70%)"
WHITE_LIGHT = f"hsl(0, {SATURATION}, 75%)"


FONT_COLOR = f"hsl(0, {SATURATION}, 80%)"

#WIDGET COLOR SATURATION


#BORDER COLOR
BORDER_SIZE = "1px"
BORDER_COLOR = f"hsl(0, {SATURATION}, 10%)"
BORDER_COLOR_LIGHT = f"hsl(0, {SATURATION}, 18%)"

#SECTIONS
GROUP_HEADER = f"hsl(0, {SATURATION}, 10%)"
GROUP_BACKGROUND = f"hsl(0, {SATURATION}, 16%)"
GUI_BACKGROUND = f"hsl(0, {SATURATION}, 12%)"

#WIDGETS
BUTTONS_BACKGROUND = f"hsl(0, {SATURATION}, 10%)"
DISABLED_COLOR = f"hsl(0, {SATURATION}, 14%);"

QTITLE = f"QToolButton {{background-color: {GROUP_HEADER}}}"\
         f"QLabel {{background-color: {GROUP_HEADER}; border-top-right-radius: {RADIUS}}}"

QSTATS = f"QLabel {{background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-top-right-radius: {RADIUS};border-top-left-radius: {RADIUS}; padding-top:4px}}"\

BIG_BUTTONS = f"QPushButton {{font: 18px; color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
              f"QPushButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\

BUTTONS_INJURY = f"QPushButton {{font: 15px; color: {INJURY_RED_BRIGHT}; border: 1px solid {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border-radius: {RADIUS}}}"\

BUTTONS = f"QPushButton {{color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
          f"QPushButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
          f"QToolButton {{color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
          f"QToolButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\

QCOMBOBOX = f"QComboBox {{color: {FONT_COLOR}; background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS};}}"\
            f"QComboBox:disabled {{color: {FONT_COLOR}; background-color: border: 1px solid {BORDER_COLOR_LIGHT}; {DISABLED_COLOR}}}"\
            f"QListView {{color: {FONT_COLOR}; background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS};}}"\
            
QLINEEDIT = f"QLineEdit {{color: {MID_COLOR}; background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
            f"QLineEdit:disabled {{color: {MID_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; background-color: {DISABLED_COLOR}}}"

QADDSUB = f"QLineEdit {{font: 14px; color: {FONT_COLOR}; background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
          f"QLineEdit:disabled {{font: 14px; color: {FONT_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; background-color: {DISABLED_COLOR}}}"

QTOOLBUTTON = f"QToolButton {{color: {FONT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\
              f"QToolButton:checked {{color: {FONT_COLOR}; background-color: {FONT_COLOR}; border-radius: {RADIUS}}}"\
              f"QToolButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
              f"QToolTip {{color: {FONT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\

QTOOLBUTTON_PORTRAIT = f"QToolButton {{color: {FONT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS};}}"\

QGROUPBOX = f"QGroupBox {{background-color: {GROUP_BACKGROUND}; border: 2px solid {BORDER_COLOR}; border-bottom-right-radius: {RADIUS}; border-bottom-left-radius: {RADIUS}}}"\
            f"QWidget {{background-color: {GROUP_BACKGROUND}; }}"\
            f"QScrollArea {{background-color: {GROUP_BACKGROUND}; }}"\
            f"QScrollBar {{background-color: {WHITE_LIGHT}; width: 6px;}}"\
            f"QScrollBar::handle:vertical {{background-color: {DARK_COLOR}; width: 6px; min-height: 20px; border: none; outline: none;}}"\

TEST_COMBO = '''
QComboBox {
    border: 1px solid hsl(0, 3%, 18%);
    border-radius: 6px;
    background-color: hsl(0, 0%, 10%);
    padding-left: 18px;
}

QComboBox::drop-down {
    background-color: hsl(0, 0%, 8%);
    border-radius: 6px;
}
'''


PORTRAIT = f"QLabel {{background-image: url(.icons/beasttoe.png); background-position: center; background-repeat: no-repeat; background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"	

INVENTORY = f"QToolButton {{background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QLineEdit {{background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton {{color: {FONT_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton#icon_label_bottom_left {{font: 10px; background-color: {DARK_COLOR}; border-bottom-left-radius: {RADIUS}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton#roll_label {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border-bottom-right-radius: {RADIUS}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
             f"QToolButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
             f"QLineEdit:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\

INVENTORY_LABEL = f"QPushButton {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
                  f"QLabel {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
                  f"QPushButton:disabled {{color: {DISABLED_COLOR}; background-color: {DISABLED_COLOR}}}"\
                  f"QLabel:disabled {{color: {DISABLED_COLOR}; background-color: {DISABLED_COLOR}}}"\

INVENTORY_INJURY = f"QToolButton {{background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\
                   f"QLineEdit {{color: {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\
                   f"QPushButton {{color: {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\

INVENTORY_INJURY_LABELS = f"QToolButton {{background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QLineEdit {{color: {FONT_COLOR}; background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QPushButton {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QLabel {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {INJURY_RED_DARK}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\

COMBAT_LOG = f"QLabel#character {{font-size: 12px; color: {FONT_COLOR}; font-weight: bold; background-color: {GROUP_BACKGROUND};}}"\
             f"QLabel#date {{font-size: 10px; color: {TEXT_MID_COLOR}; background-color: {GROUP_BACKGROUND}; padding-right: 5px;}}"\
             f"QLabel#breakdown {{font-size: 10px; color: {TEXT_MID_COLOR}; background-color: {GROUP_BACKGROUND};}}"\
             f"QLabel#hit {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top-right-radius: {RADIUS}; border-bottom: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#roll {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-bottom-right-radius: {RADIUS}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#hit_desc {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-bottom: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#roll_desc {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#label {{font-size: 15px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; padding-left:10px; padding-top:10px;}}"\
             f"QLabel#icon {{border: 2px solid {WHITE_LIGHT};}}"\
             f"QLabel#label_sub {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; padding-left:11px; padding-bottom:10px;}}"

COMBAT_LABEL = f"QLabel#roll_desc {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_DAMAGE = f"QLabel#roll_desc {{font-size: 10px; font-weight: bold; color: #870000; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_HEALING= f"QLabel#roll_desc {{font-size: 10px; font-weight: bold; color: #00872d; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_EVOKE= f"QLabel#roll_desc {{font-size: 10px; font-weight: bold; color: #004887; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"

BASE_STYLE = f"QWidget {{border-style: outset; background-color: {GUI_BACKGROUND}; color: {FONT_COLOR};}}"\
