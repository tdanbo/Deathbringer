from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import os
import json

import constants as cons

class Section:
    def __init__(
        self,
        layout_type = QVBoxLayout(),
        parent_layout = "No Parent Layout",
        group=False,
        scroll=False,
        hidden=False,
    ):
        self.main_layout = layout_type
        self.parent_layout = parent_layout
        self.group = group
        self.scroll = scroll

        print(self.main_layout)
        print(self.parent_layout)
        print(self.group)
        print(self.scroll)
        print("----------------")

        if group == True:
            self.groupbox = QGroupBox()
            self.group_layout = layout_type
            self.groupbox.setLayout(self.group_layout)
            self.groupbox.setHidden(hidden)

        if self.scroll == True:
            # Create a vertical layout for the main window
            self.scroll_layout = QVBoxLayout()

            # Create a scroll area
            self.scroll_area_widget = QScrollArea()

            # Create a widget to hold the contents of the scroll area
            # and set the layout as its layout
            self.scroll_widget = QWidget()
            self.scroll_widget.setLayout(self.scroll_layout)

            # Set the widget as the scroll area's widget
            self.scroll_area_widget.setWidget(self.scroll_widget)

            self.scroll_layout.setAlignment(Qt.AlignBottom)
            self.scroll_layout.setSpacing(0)

            self.scroll_area_widget.setWidgetResizable(True)
            self.scroll_area_widget.setHorizontalScrollBarPolicy(
                Qt.ScrollBarAlwaysOff
            )

            self.main_layout.addWidget(self.scroll_area_widget)

        if self.parent_layout == "No Parent Layout":
            pass
        else:
            self.parent_layout.addLayout(self.main_layout)  

    def get_layout(self):
        return self.main_layout

    def get_scroll_layout(self):
        return self.scroll_layout

    def get_group_layout(self):
        return self.group_layout

class Widget:
    _registry = []
    _task_registry = []

    def __init__(
        self,
        widget_type="",
        parent_layout="",
        text="",
        tooltip="",
        objectname="",
        signal="",
        icon="",
        width="",
        height="",
        align="",
        enabled=True,
        checkable=False,
        task=False,
        validator="",
        placeholder="",
        setting ="",
        stylesheet=""
    ):
        self.text = text
        self.widget = widget_type
        self.object = objectname
        self.setting = setting
        self.widget.setToolTip(tooltip)
        self.widget.setObjectName(self.object)
        self.widget.setStyleSheet(stylesheet)
        self.widget_key = f"{self.object}_{self.setting}"
        self.set_enabled(enabled)
        self.set_checkable(checkable)
        self.set_text(self.widget, self.text)
        self.set_signal(self.widget, signal, setting)
        self.set_alignment(self.widget, align)
        self.set_size(self.widget, width, height)
        self.set_validator(self.widget, validator)
        self.set_placeholder(self.widget, placeholder)
        self.load_setting(objectname, setting)
        if icon != "":
            self.set_icon(self.widget, icon, 30)
        parent_layout.addWidget(self.widget)

        if task == True:
            self._task_registry.append(self)
        else:
            self._registry.append(self)

    def load_setting(self, objectname, setting):
        if os.path.exists(cons.SETTINGS):   
            open_file = open(cons.SETTINGS, "r")
            open_json = json.load(open_file)
            if self.widget_key in open_json:
                if setting == "checked":
                    self.widget.setChecked(open_json[self.widget_key])
                elif setting == "text":
                    self.widget.setText(open_json[self.widget_key])
                elif setting == "value":
                    self.widget.setValue(open_json[self.widget_key])
        else:
            json.dump({}, open(cons.SETTINGS, "w"), indent=4)
        self.save_setting()

    def save_setting(self):
        open_json = json.load(open(cons.SETTINGS, "r"))
        if self.setting == "text":
            open_json[self.widget_key] = self.widget.text()
        elif self.setting == "value":
            open_json[self.widget_key] = self.widget.value()
        elif self.setting == "checked":
            open_json[self.widget_key] = self.widget.isChecked()
        json.dump(open_json, open(cons.SETTINGS, "w"), indent=4)

    def set_enabled(self, enabled):
        try:
            self.widget.setEnabled(enabled)
        except:
            pass

    def set_placeholder(self, widget, placeholder):
        if placeholder != "":
            widget.setPlaceholderText(placeholder)

    def set_validator(self, widget, validator):
        if validator == "":
            pass
        elif validator == "numbers":
            widget.setValidator(QIntValidator())
        elif validator == "percent":
            widget.setValidator(QIntValidator())
            widget.setMaxLength(3)
        else:
            pass

    def set_checkable(self, checkable):
        try:
            self.widget.setCheckable(checkable)
            self.widget.setChecked(checkable)
        except:
            pass

    def get_parent_layout(self, layout):
        return layout

    def get_widget(self):
        return self.widget

    def set_alignment(self, widget, align):
        if align == "":
            pass
        elif align == "left":
            widget.setAlignment(Qt.AlignLeft)
        elif align == "right":
            widget.setAlignment(Qt.AlignRight)
        elif align == "vcenter":
            widget.setAlignment(Qt.AlignVCenter)
        else:
            widget.setAlignment(Qt.AlignHCenter)

    def set_text(self, widget, text):
        try:
            widget.setText(text)
        except:
            pass
        try:
            widget.setValue(int(text))
        except:
            pass

    def set_size(self, widget, width, height):
        try:
            widget.setFixedWidth(width)
        except:
            pass
        try:
            widget.setFixedHeight(height)
        except:
            pass

    def set_signal(self, widget, signal, setting):
        if signal != "":
            try:
                self.widget.clicked.connect(signal)
            except:
                pass
            try:
                self.widget.textEdited.connect(signal)

            except:
                pass
            try:
                self.widget.textChanged.connect(signal)
            except:
                pass

        if setting == "checked":
            self.widget.clicked.connect(self.save_setting)
        elif setting == "text":
            self.widget.textEdited.connect(self.save_setting)

    def set_icon(self, widget, icon, size):
        self.icon = QIcon()
        self.icon.addPixmap(QPixmap(os.path.join(cons.ICONS, icon)))
        widget.setIcon(self.icon)
        widget.setIconSize(QSize(size, size))