RADIUS = "6px"


TEXT_COLOR = "hsl(0, 0%, 80%)"
TEXT_MID_COLOR = "hsl(0, 0%, 40%)"	
TEXT_DARK_COLOR = "hsl(0, 0%, 25%)"	
TEXT_BLACK_COLOR = "hsl(0, 0%, 5%)"	

INJURY_RED = "#330000"
INJURY_RED_BRIGHT = "#800000"
INJURY_RED_DARK = "#2b0000"

VIBRANT_COLOR = "hsl(0, 0%, 10%)"
DARK_COLOR = "hsl(0, 0%, 10%)"
MID_COLOR = "hsl(0, 0%, 25%)"
LIGHT_COLOR = "hsl(0, 0%, 20%)"
DISABLED_COLOR = "hsl(0, 0%, 19%);"
DIM_WHITE_LIGHT = "hsl(0, 0%, 75%)"
WHITE_LIGHT = "hsl(0, 0%, 80%)"

QPUSHBUTTON = f"QPushButton {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\
              f"QPushButton:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"

QPUSHBUTTON_INJURY = f"QPushButton {{color: {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border-radius: {RADIUS}}}"\

QLINEEDIT = f"QLineEdit {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\
            f"QLineEdit:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"

QTOOLBUTTON = f"QToolButton {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\
              f"QToolButton:checked {{color: {TEXT_COLOR}; background-color: {TEXT_COLOR}; border-radius: {RADIUS}}}"\
              f"QToolButton:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"\
              f"QToolTip {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\

QTOOLBUTTON_PORTRAIT = f"QToolButton {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS};}}"\

QGROUPBOX = f"QGroupBox {{background-color: {LIGHT_COLOR}; border-bottom-right-radius: {RADIUS}; border-bottom-left-radius: {RADIUS}}}"

QTITLE = f"QToolButton {{background-color: {VIBRANT_COLOR}}}"\
         f"QLabel {{background-color: {DARK_COLOR}; border-top-right-radius: {RADIUS}}}"

QSTATS = f"QPushButton {{background-color: {DARK_COLOR};border-top-right-radius: {RADIUS}}}"\
         f"QLineEdit {{background-color: {DARK_COLOR}; border-bottom-right-radius: {RADIUS}; border-bottom-left-radius: {RADIUS}}}"

INVENTORY = f"QToolButton {{background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QLineEdit {{background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton#icon_label_bottom_left {{font: 10px; background-color: {DARK_COLOR}; border-bottom-left-radius: {RADIUS}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton#roll_label {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border-bottom-right-radius: {RADIUS}; border: 0px solid {MID_COLOR};}}"\
             f"QPushButton:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"\
             f"QToolButton:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"\
             f"QLineEdit:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"\

INVENTORY_LABEL = f"QPushButton {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
                  f"QLabel {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {DARK_COLOR}; border: 0px solid {MID_COLOR};}}"\
                  f"QPushButton:disabled {{color: {DISABLED_COLOR}; background-color: {DISABLED_COLOR}}}"\
                  f"QLabel:disabled {{color: {DISABLED_COLOR}; background-color: {DISABLED_COLOR}}}"\

INVENTORY_INJURY = f"QToolButton {{background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\
                   f"QLineEdit {{color: {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\
                   f"QPushButton {{color: {INJURY_RED_BRIGHT}; background-color: {INJURY_RED}; border: 0px solid {MID_COLOR};}}"\

INVENTORY_INJURY_LABELS = f"QToolButton {{background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QLineEdit {{color: {TEXT_COLOR}; background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QPushButton {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {INJURY_RED}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\
                   f"QLabel {{font: 10px; color: {TEXT_MID_COLOR}; background-color: {INJURY_RED_DARK}; border: 0px; border-bottom: 1px solid {INJURY_RED_DARK};}}"\

COMBAT_LOG = f"QLabel#character {{font-size: 12px; color: {TEXT_MID_COLOR}; font-weight: bold; background-color: {LIGHT_COLOR};}}"\
             f"QLabel#date {{font-size: 10px; color: {TEXT_MID_COLOR}; background-color: {LIGHT_COLOR};}}"\
             f"QLabel#breakdown {{font-size: 10px; color: {TEXT_MID_COLOR}; background-color: {LIGHT_COLOR};}}"\
             f"QLabel#hit {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top-right-radius: {RADIUS}; border-bottom: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#roll {{font-size: 16px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-bottom-right-radius: {RADIUS}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#hit_desc {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-bottom: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#roll_desc {{font-size: 10px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; border-top: 1px solid {DIM_WHITE_LIGHT};}}"\
             f"QLabel#label {{font-size: 15px; font-weight: bold; color: {TEXT_BLACK_COLOR}; background-color: {WHITE_LIGHT}; padding-left:10px; padding-top:10px;}}"\
             f"QLabel#label_sub {{font-size: 11px; font-weight: bold; color: #af0000; background-color: {WHITE_LIGHT}; padding-left:11px; padding-bottom:10px;}}"\
             f"QLabel#icon {{border: 2px solid {WHITE_LIGHT};}}"\

# roll_type = {"Custom":"#bd4f00", "Attack":"#bd0000", "Defend":"#0062bd"}

# name_stylesheet = "font-size: 12px; font-weight: bold; color: hsl(0%, 0%, 50%); background-color: hsl(0%, 0%, 20%)"
# icon_stylesheet = "background-color: hsl(0%, 0%, 80%);"
# type_stylesheet = f"font-size: 11px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 20%); border: 0px;"
# breakdown_stylesheet = "font-size: 10px; color: hsl(0%, 0%, 30%); background-color: hsl(0%, 0%, 20%)"
# roll_stylesheet = "font-size: 18px; font-weight: bold; background-color: hsl(0%, 0%, 80%); color: hsl(0%, 0%, 10%); border: 0px; border-top-right-radius: 8px; border-bottom-right-radius: 8px;"
# date_stylesheet = "font-size: 10px; color: hsl(0%, 0%, 30%); background-color: hsl(0%, 0%, 20%)"


DARK_STYLE = """
QWidget  {
    border-style: outset;
    border: 1px solid #3b3b3b;
    background-color: hsl(0, 0%, 10%);
    color: hsl(0, 0%, 80%);
    font: 12px;
    font-family: Trebuchet MS;  
}

QWidget::placeholder{
    color: hsl(0, 0%, 50%);
}

QWidget#scroll_widget  {
    border: 0px;
    background-color: #333333
}

QWidget::pressed {
    background-color: #851209;
}

QPushButton {
    color: hsl(0, 0%, 60%);
}

QToolButton::checked {
    background-color: hsl(0%, 0%, 80%);
    color: #CCCCCC
}

QToolButton#progress_button {
    border: 1px solid #3b3b3b;
}

QPushButton::checked {
    background-color: #4f6b8c;
    color: #CCCCCC
}

QLineEdit {
    color: hsl(0, 0%, 60%);
}

QLineEdit::disabled {
    color: hsl(0, 0%, 30%);
    background-color: hsl(0, 0%, 19%);    
    border: 1px solid hsl(0, 0%, 20%);
}

QComboBox::disabled {
    color: hsl(0, 0%, 30%);
    background-color: hsl(0, 0%, 19%);
    border: 1px solid hsl(0, 0%, 20%);
}

QPushButton::disabled {
    color: hsl(0, 0%, 30%);
    background-color: hsl(0, 0%, 19%);
    border: 1px solid hsl(0, 0%, 20%);
}

QToolButton::disabled {
    color: hsl(0, 0%, 30%);
    background-color: hsl(0, 0%, 19%);
    border: 1px solid hsl(0, 0%, 20%);
}

QLineEdit#upres_percent  {
    padding-left: 1px;
}

QLabel {
    border: 0px;
    color: hsl(0%, 0%, 60%);
}

QLabel#title {
    border: 1px;
    font-weight: bold;
    border-style: outset;
    border: 1px solid #3b3b3b;
    color: hsl(0%, 0%, 60%);
}

QGroupBox  {
    background-color: #333333
}

QFrame#divider  {
    background-color: #3b3b3b
}

QScrollBar {
    width: 10px;
}

QScrollBar::handle {
    background-color: #404040;
}
"""
