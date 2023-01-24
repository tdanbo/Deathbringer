from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
import constants as cons

import json
import functions as func

from pyside import Section, Widget

class FeatsGUI(QWidget):
    def __init__(self, feature_slot = ""):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        self.feature_slot = feature_slot

        self.features = json.load(open(cons.FEATURES, "r"))

        self.feat_main_layout = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            spacing = 10,   
        )

        self.feats_scroll = Section(
            outer_layout = QVBoxLayout(),
            inner_layout = ("VBox", 1),
            parent_layout = self.feat_main_layout.inner_layout(1),
            scroll=(True,"top"),
        )

        for feat in self.features:
            self.single_feat_layout = Section (
            outer_layout = QVBoxLayout(),
            inner_layout = ("HBox", 3),
            group = (True,None,None), 
            title=feat["Name"],
            icon = (feat["Icon"],cons.WSIZE*1.5,cons.ICON_COLOR),	  
            parent_layout = self.feats_scroll.inner_layout(1),
            )

            self.feat_label = Widget(
                widget_type=QPlainTextEdit(),
                stylesheet=style.QPUSHBUTTON,
                parent_layout=self.single_feat_layout.inner_layout(2),
                text = feat["Description"],
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                )
            
            self.select_feat = Widget(
                widget_type=QPushButton(),
                stylesheet=style.QPUSHBUTTON,
                parent_layout=self.single_feat_layout.inner_layout(3),
                text = "Select",
                size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                height = cons.WSIZE*1.5,
                objectname=feat["Name"],
                )

            self.select_feat.get_widget().clicked.connect(self.confirm_feat)
            self.single_feat_layout.inner_layout(2).addWidget(self.feat_label.get_widget())
            self.single_feat_layout.inner_layout(3).addWidget(self.select_feat.get_widget())
            self.feats_scroll.inner_layout(1).addLayout(self.single_feat_layout.outer_layout())

        self.feat_main_layout.outer_layout().addLayout(self.feats_scroll.outer_layout())
        self.setWindowTitle("Select Feat")
        self.setLayout(self.feat_main_layout.outer_layout())

        self.setStyleSheet(style.DARK_STYLE)

    def confirm_feat(self):
        print("Selected Feat")
        print(self.feature_slot)
        selected_feat = [feat for feat in self.features if feat["Name"] == self.sender().objectName()][0]
        func.set_icon(self.feature_slot, selected_feat["Icon"],cons.ICON_COLOR)
        self.feature_slot.setToolTip(selected_feat["Description"])
        self.hide()