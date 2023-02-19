import sys
from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *


class MyWidget(QWidget):

    def __init__(self):
        super().__init__()

        # create a QVBoxLayout layout
        layout = QVBoxLayout()

        for i in range(1, 4):
            section_widget = QWidget()
            section_layout = QVBoxLayout()
            section_widget.setLayout(section_layout)
            outer_layout = QVBoxLayout()
            section_layout.addLayout(outer_layout)
            inner_layout = QHBoxLayout()
            outer_layout.addLayout(inner_layout)



            button = QPushButton(f"TEST BUTTON{i}")
            inner_layout.addWidget(button)
            #inner_layout.setAlignment(Qt.AlignTop)  # align the button to the top
            layout.addWidget(section_widget)
            outer_layout.setContentsMargins(0,0,0,0)
            section_widget.setStyleSheet("background-color: red;")
            inner_layout.setAlignment(Qt.AlignTop)    

        #section_layout.setAlignment(Qt.AlignTop)  # remove this line
        layout.setAlignment(Qt.AlignTop)    

        # add a label to the layout

        self.setLayout(layout)
        self.show()


if __name__ == '__main__':

    app = QApplication(sys.argv)
    ex = MyWidget()
    sys.exit(app.exec_())
