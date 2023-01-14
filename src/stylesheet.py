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

QWidget::disabled  {
    color: hsl(0, 0%, 30%);
}

QWidget#scroll_widget  {
    border: 0px;
}

QWidget::pressed {
    background-color: #851209;
}

QPushButton {
    color: hsl(0, 0%, 30%);
}

QToolButton {
    border: 1px solid #3b3b3b;
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
    color: hsl(0, 0%, 60%);
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
