import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        # create a QVBoxLayout layout
        layout = QVBoxLayout()

        section_layout = QVBoxLayout()
        section_widget = QWidget()
        outer_layout = QVBoxLayout()
        inner_layout = QHBoxLayout()

        # TEST 1
        section_layout.addWidget(section_widget)
        section_widget.setLayout(outer_layout)
        outer_layout.addLayout(inner_layout)

        layout2 = QVBoxLayout()

        # add a label to the layout
        button1 = QPushButton("TEST BUTTON1")
        button2 = QPushButton("TEST BUTTON2")

        button1.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        button2.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)

        inner_layout.addWidget(button1)
        layout2.addWidget(button2)

        

        layout.addLayout(section_layout)
        layout.addLayout(layout2)

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())