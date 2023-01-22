RADIUS = "6px"


TEXT_COLOR = "hsl(0, 0%, 80%)"

VIBRANT_COLOR = "#113300"
DARK_COLOR = "hsl(0, 0%, 10%)"
LIGHT_COLOR = "hsl(0, 0%, 20%)"
DISABLED_COLOR = "hsl(0, 0%, 19%);"

QPUSHBUTTON = f"QPushButton {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\
              f"QPushButton:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"

QLINEEDIT = f"QLineEdit {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\
            f"QLineEdit:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"

QTOOLBUTTON = f"QToolButton {{color: {TEXT_COLOR}; background-color: {DARK_COLOR}; border-radius: {RADIUS}}}"\
              f"QToolButton:disabled {{color: {TEXT_COLOR}; background-color: {DISABLED_COLOR}}}"

QGROUPBOX = f"QGroupBox {{background-color: {LIGHT_COLOR}; border-bottom-right-radius: {RADIUS}; border-bottom-left-radius: {RADIUS}}}"

QTITLE = f"QToolButton {{background-color: {VIBRANT_COLOR}}}"\
         f"QLabel {{background-color: {DARK_COLOR}; border-top-right-radius: {RADIUS}}}"

QSTATS = f"QPushButton {{background-color: {DARK_COLOR};border-top-right-radius: {RADIUS}}}"\
         f"QLineEdit {{background-color: {DARK_COLOR}; border-bottom-right-radius: {RADIUS}; border-bottom-left-radius: {RADIUS}}}"

DARK_STYLE = """
QWidget  {
    border-style: outset;
    border: 1px solid #3b3b3b;
    background-color: hsl(0, 0%, 10%);
    color: hsl(0, 0%, 80%);
    font: 12px;
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
