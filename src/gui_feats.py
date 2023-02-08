from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import stylesheet as style
import constants as cons

import json
import functions as func
import os

from pyside import Section, Widget
from character_sheet import CharacterSheet

class FeatsGUI(QWidget):
    def __init__(self, csheet, feature_slot = ""):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        self.csheet = csheet
        self.feature_slot = feature_slot

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
            spacing = 10, 
        )

        for feat_dict in os.listdir(cons.FEATURES):
            for feat in json.load(open(os.path.join(cons.FEATURES,feat_dict), "r")):
                self.single_feat_layout = Section (
                outer_layout = QVBoxLayout(),
                inner_layout = ("HBox", 3),
                group = (True,None,125), 
                title=feat["name"],
                icon = (feat["icon"],cons.WSIZE*1.5,cons.ICON_COLOR),	  
                parent_layout = self.feats_scroll.inner_layout(1),
                )

                self.feat_label = Widget(
                    widget_type=QPlainTextEdit(),
                    stylesheet=style.BUTTONS,
                    parent_layout=self.single_feat_layout.inner_layout(2),
                    text = feat["description"],
                    size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                    )
                
                self.select_feat = Widget(
                    widget_type=QPushButton(),
                    stylesheet=style.BUTTONS,
                    parent_layout=self.single_feat_layout.inner_layout(3),
                    text = "Select",
                    size_policy = (QSizePolicy.Expanding , QSizePolicy.Expanding),
                    height = cons.WSIZE*1.5,
                    objectname=feat["name"],
                    )

                self.select_feat.get_widget().clicked.connect(self.confirm_feat)
                self.single_feat_layout.inner_layout(2).addWidget(self.feat_label.get_widget())
                self.single_feat_layout.inner_layout(3).addWidget(self.select_feat.get_widget())
                self.feats_scroll.inner_layout(1).addLayout(self.single_feat_layout.outer_layout())

        self.feat_main_layout.outer_layout().addLayout(self.feats_scroll.outer_layout())
        self.setWindowTitle("Select Feat")
        self.setLayout(self.feat_main_layout.outer_layout())

        self.setStyleSheet(style.BASE_STYLE)

    def confirm_feat(self):
        for feat_dict in os.listdir(cons.FEATURES):
            for feat in json.load(open(os.path.join(cons.FEATURES,feat_dict), "r")):
                if feat["name"] == self.sender().objectName():
                    selected_feat = feat
                    func.set_icon(self.feature_slot, selected_feat["icon"],cons.ICON_COLOR)
                    self.feature_slot.setToolTip(selected_feat["description"])
                    self.feature_slot.setProperty("feat", selected_feat["name"])
                    self.hide()
                    CharacterSheet(self.csheet).update_sheet()
                    return