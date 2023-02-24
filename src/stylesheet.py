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
DIM_WHITE_LIGHT2 = "hsl(0, 0%, 50%)"
WHITE_LIGHT = f"hsl(0, {SATURATION}, 75%)"


PLAYER_COLOR = "hsl(214, 30%, 15%)"
CREATURE_COLOR = "hsl(0, 30%, 15%)"

FONT_COLOR = f"hsl(0, {SATURATION}, 80%)"


#WIDGET COLOR SATURATION

#COLOR
GUI_COLOR = "#3d1f1f"

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
DISABLED_COLOR2 = f"hsl(0, {SATURATION}, 30%);"
DISABLED_COLOR3 = f"hsl(0, {SATURATION}, 20%);"

QTITLE = f"QToolButton {{background-color: {GROUP_HEADER}}}"\
         f"QLabel {{background-color: {GROUP_HEADER}; border-top-right-radius: {RADIUS}}}"\
         f"QPushButton {{background-color: {GUI_COLOR}; border-top-right-radius: {RADIUS}; border-top-left-radius: {RADIUS}; border-right: 2px solid {BORDER_COLOR};border-left: 2px solid {BORDER_COLOR};border-top: 2px solid {BORDER_COLOR};}}"

QSTATS = f"QPushButton {{background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-top-right-radius: {RADIUS};border-top-left-radius: {RADIUS};}}"\

BIG_BUTTONS = f"QPushButton {{font: 18px; color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
              f"QPushButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\

BUTTONS_INJURY = f"QPushButton {{font: 15px; color: {INJURY_RED_BRIGHT}; border: 1px solid {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border-radius: {RADIUS}}}"\

BUTTONS = f"QPushButton {{color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
          f"QPushButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
          f"QToolButton {{color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
          f"QToolButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
          f"QToolButton:checked {{color: {FONT_COLOR}; background-color: {WHITE_LIGHT}}}"\
          f"QPushButton:checked {{color: {FONT_COLOR}; background-color: {WHITE_LIGHT}}}"\

LABELS = f"QLabel {{color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\

PARTY_BUTTONS = f"QPushButton {{color: {DISABLED_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
          f"QPushButton:checked {{color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}}}"\

CREATURE_BUTTONS = f"QPushButton {{color: {DISABLED_COLOR}; background-color: {BUTTONS_BACKGROUND}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"\
          f"QPushButton:checked {{color: {FONT_COLOR}; background-color: {BUTTONS_BACKGROUND}}}"\

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
            
DICE_TRAY1 = f"QPushButton {{color: {FONT_COLOR};background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-top-right-radius: {RADIUS}; border-bottom-right-radius: {RADIUS};}}"
DICE_TRAY2 = f"QPushButton {{color: {FONT_COLOR};background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-top-left-radius: {RADIUS}; border-bottom-left-radius: {RADIUS};}}"
DICE_TRAY = f"QPushButton {{color: {MID_COLOR}; background-color: {DISABLED_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"

TEST_COMBO = '''
QComboBox {
    font-size: 18x;
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


#PORTRAIT = f"QLabel {{background-image: url(.icons/beasttoe.png); background-position: center; background-repeat: no-repeat; background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"	
PORTRAIT = f"QLabel {{background-position: center; background-repeat: no-repeat; background-color: {DARK_COLOR}; border: 1px solid {BORDER_COLOR_LIGHT}; border-radius: {RADIUS}}}"	


INVENTORY = f"QToolButton {{background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QLineEdit {{background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton {{color: {FONT_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton#icon_label_bottom_left {{font: 10px; background-color: {DARK_COLOR}; border-bottom-left-radius: {RADIUS}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton#roll_label {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border-bottom-right-radius: {RADIUS}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
             f"QToolButton:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
             f"QLineEdit:disabled {{color: {FONT_COLOR}; background-color: {DISABLED_COLOR}}}"\
             f"QLabel {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QLabel:disabled {{color: {DISABLED_COLOR}; background-color: {DISABLED_COLOR}}}"\
             
INVENTORY_INJURY = f"QToolButton {{background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\
                   f"QLineEdit {{color: {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\
                   f"QPushButton {{color: {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\

INVENTORY_INJURY_LABELS = f"QToolButton {{background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QLineEdit {{color: {FONT_COLOR}; background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QPushButton {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QLabel {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {INJURY_RED_DARK}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\

COMBAT_LOG = f"QLabel[objectName^='character'] {{font-size: 12px; color: {FONT_COLOR}; font-weight: bold; background-color: {GROUP_BACKGROUND};}}"\
             f"QLabel[objectName^='time'] {{font-size: 10px; color: {TEXT_MID_COLOR}; background-color: {GROUP_BACKGROUND}; padding-right: 5px;}}"\
             f"QLabel[objectName^='breakdown'] {{font-size: 10px; color: {TEXT_MID_COLOR}; background-color: {GROUP_BACKGROUND};}}"\
             f"QPushButton[objectName^='desc hit'] {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-bottom: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel[objectName^='action name'] {{font-size: 14px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; padding-left:10px; padding-top:10px;}}"\
             f"QLabel[objectName^='icon'] {{border: 2px solid {WHITE_LIGHT}; background-color: {WHITE_LIGHT};}}"\
             f"QLabel[objectName^='action dice'] {{font-size: 10px; font-weight: bold; color: {DIM_WHITE_LIGHT2}; background-color: {WHITE_LIGHT}; padding-left:11px;}}"

COMBAT_BUTTON_1 = f"QLabel {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top-right-radius: {RADIUS}; border-bottom: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_BUTTON_2 = f"QLabel {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-bottom-right-radius: {RADIUS}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"

COMBAT_BUTTON_1_REROLL = f"QLabel {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-bottom: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_BUTTON_2_REROLL = f"QLabel {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"

COMBAT_LABEL = f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_DAMAGE = f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: #870000; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_HEALING= f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: #00872d; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_EVOKE= f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: #004887; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_CUSTOM= f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: #874d00; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_CHECK= f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: #008768; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"
COMBAT_LABEL_HIT= f"QPushButton[objectName^='desc roll'] {{font-size: 10px; font-weight: bold; color: #000bab; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"

BASE_STYLE = f"QWidget {{border-style: outset; background-color: {GUI_BACKGROUND}; color: {FONT_COLOR};}}"\
