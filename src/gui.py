from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *
import os
import sys
import constants as cons

import functions as func
import stylesheet as style
from combat_log import CombatLog

import json


class MainWindow(QWidget):
    def __init__(self):
        super().__init__(None, Qt.WindowStaysOnTopHint)

        # Layouts
        self.main_layout = QHBoxLayout()
        self.setLayout(self.main_layout)

        # Widget height
        self.widget_height = 30

        # Setting up layouts/sections
        self.log_section = Section(
            QVBoxLayout(),
            self.main_layout,
            sub_layouts=2,
            group=True,
        )

        self.character_sheet = Section(
            QVBoxLayout(),
            self.main_layout,
            group=True,
        )
        self.log_scroll = Section(
            QVBoxLayout(),
            self.log_section.get_layout(1),
            scroll=True,
        )
        self.log_latest = Section(
            QVBoxLayout(),
            self.log_section.get_layout(1),
            group=True,
        )
        self.log_dice = Section(
            QHBoxLayout(),
            self.log_section.get_layout(1),
        )

        combat_log = CombatLog().get_log()
        print(combat_log)
        '''
        for entry in combat_log:
            print(entry)

            self.log_latest_name = Section( 
                QHBoxLayout(),
                self.log_latest.get_layout(1),
            )

            self.log_latest_data = Section( 
                QHBoxLayout(),
                self.log_latest.get_layout(1),
            )
            self.log_latest_date = Section( 
                QHBoxLayout(),
                self.log_latest.get_layout(1),
            )
            '''


        # BUTTONS
        dice = ["%","D4", "D6", "D8", "D10", "D12", "D20"]
        for die in dice:
            Widget(
                widget=QPushButton(),
                layout=self.log_dice.get_layout(1),
                text=die,
                tooltip=f"Roll {die}",
                width=self.widget_height,
                height=self.widget_height,
            )
                
        self.test_button = Widget(
            widget=QPushButton(),
            layout=self.character_sheet.get_layout(1),
            text="Test",
            objectname="test_button",
            setting = "checked",
            height=self.widget_height,
        )



        '''''
        self.boolean_button = Widget(
            widget=QPushButton(),
            layout=self.dynamesh_section.get_layout(1),
            text="Boolean",
            tooltip="Enable Boolean",
            objectname="boolean_button",
            checkable=True,
            setting = "checked",
            height=self.widget_height,
        )'''

        # general settings and styling for UI
        self.main_layout.setSpacing(2)
        self.main_layout.setContentsMargins(0, 0, 0, 0)

        # setting stylesheet
        self.setStyleSheet(style.DARK_STYLE)

    def show_hide_settings(self):
        if self.sender().isChecked():
            self.settings_section.get_group().setHidden(False)
        else:
            self.settings_section.get_group().setHidden(True)

class Section:
    def __init__(
        self,
        layout_type,
        parent_layout,
        sub_layouts=1,
        group=False,
        scroll=False,
        hidden=False,
    ):
        self.layout = layout_type
        if group == True:
            self.group = QGroupBox()
            self.group.setLayout(self.layout)
            self.group.setHidden(hidden)
            parent_layout.addWidget(self.group)
        else:
            parent_layout.addLayout(self.layout)

        self.widget_layouts = []
        for count in range(sub_layouts):
            widget_layout = self.layout
            self.widget_layouts.append(widget_layout)
            self.layout.addLayout(widget_layout)

        if scroll == True:
            if sub_layouts > 1:
                raise ValueError("Only 1 widget layout allowed for scroll setup")
            else:
                self.scroll_layout = QVBoxLayout()
                self.scroll_widget = QWidget()
                self.scroll_widget.setObjectName("scroll_widget")
                self.scroll_area_widget = QScrollArea()
                self.scroll_area_widget.setWidget(self.scroll_widget)
                self.scroll_widget.setLayout(self.scroll_layout)

                self.scroll_layout.setAlignment(Qt.AlignTop)
                self.scroll_layout.setSpacing(0)

                self.scroll_area_widget.setWidgetResizable(True)
                self.scroll_area_widget.setHorizontalScrollBarPolicy(
                    Qt.ScrollBarAlwaysOff
                )

                self.widget_layouts[0].addWidget(self.scroll_area_widget)
                self.widget_layouts.insert(0, self.scroll_layout)

    def get_layout(self, index):
        return self.widget_layouts[index - 1]

    def get_group(self):
        return self.group


class Widget:
    _registry = []
    _task_registry = []

    def __init__(
        self,
        widget="",
        layout="",
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
    ):
        self.text = text
        self.widget = widget
        self.object = objectname
        self.setting = setting
        self.widget.setToolTip(tooltip)
        self.widget.setObjectName(self.object)
        self.widget_key = f"{self.object}_{self.setting}"
        self.set_enabled(enabled)
        self.set_checkable(checkable)
        self.set_text(widget, self.text)
        self.set_signal(widget, signal, setting)
        self.set_alignment(widget, align)
        self.set_size(self.widget, width, height)
        self.set_validator(widget, validator)
        self.set_placeholder(widget, placeholder)
        self.load_setting(objectname, setting)
        if icon != "":
            self.set_icon(self.widget, icon, 30 / 2)
        layout.addWidget(self.widget)

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


def run_gui(name, version):
    app = QApplication(sys.argv)
    w = MainWindow()
    w.setWindowTitle("%s v%s" % (name, str(version)))
    w.show()
    app.exec_()
