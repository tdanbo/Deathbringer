from PySide2.QtWidgets import *
from PySide2.QtGui import *
from PySide2.QtCore import *

import os
import json

import constants as cons

import stylesheet as style
import functions as func

class SimpleSection(QWidget):
    def __init__(self,
        section_layout = QVBoxLayout(),
        inner_layout=(QHBoxLayout(), 1),
        parent_layout=None,
        class_group=None,
        margins=(0,0,0,0),
        spacing=0,
        width=None,
        height=None,
    ):
        super().__init__()



        self.section_layout = section_layout
        self.parent_layout = parent_layout
        self.section_inner_layout = self.inner_layout_list(inner_layout)
        self.inner_layouts = self.inner_layout_list(inner_layout)

        for layout in self.inner_layouts:
            section_layout.addLayout(layout)

        # styling
        self.section_layout.setContentsMargins(*margins)
        self.section_layout.setSpacing(spacing)

        self.setLayout(self.section_layout)

        if width != None:
            self.setFixedWidth(width)
        
        if height != None:
            self.setFixedHeight(height)

        if class_group != None:
            class_group.append(self)

    def inner_layout_list(self, inner_layout):
        self.all_inner_layouts = []
        for layout in range(inner_layout[1]):
            self.all_inner_layouts.append(inner_layout[0])
        return self.all_inner_layouts
    
    def inner_layout(self, count):
        return self.all_inner_layouts[count - 1]
    
    def connect_to_parent(self):
        if self.parent_layout != None:
            self.parent_layout.addWidget(self)
    
class Section(QWidget):
    all_sections = []

    def __init__(
        self,
        outer_layout=QVBoxLayout(),
        inner_layout=(QHBoxLayout(), 1),
        parent_layout=None,
        spacing=0,
        group=False,
        scroll=(False, "bottom"),
        title="",
        icon="",
        content_margin="",
        class_group=[],
        width = "",
        height = ""
    ):
        super().__init__()

        self.outer_layout_type = outer_layout
        self.inner_layout_type = inner_layout[0]
        self.inner_layout_count = inner_layout[1]
        self.parent_layout = parent_layout
        self.group = group
        self.scroll = scroll
        self.spacing = spacing
        self.class_group = class_group
        self.width = width
        self.height = height

        if self.width != "":
            self.setFixedWidth(self.width)
        if self.height != "":
            self.setFixedHeight(self.height)


        self.section_layout = QVBoxLayout()
        self.section_layout.setContentsMargins(0, 0, 0, 0)

        self.inner_layouts = self.inner_layout_list()
        self.outer_layout_type.setSpacing(spacing)

        if content_margin != "":
            self.outer_layout_type.setContentsMargins(*content_margin)

        self.section_layout.setSpacing(0)
        if self.group == True:
            if title != "":
                self.title_layout = QHBoxLayout()
                self.title_label = QLabel(title)
                self.title_label.setStyleSheet(style.QTITLE)
                self.title_label.setObjectName("title")
                self.outer_layout_type.addWidget(self.title_label)
                self.title_label.setFixedHeight(cons.WSIZE)
                self.title_label.setSizePolicy(
                    QSizePolicy.Expanding, QSizePolicy.Expanding
                )
                if icon != "":
                    self.title_icon = QToolButton()
                    self.title_icon.setStyleSheet(style.QTITLE)
                    self.title_icon.setFixedSize(cons.WSIZE, cons.WSIZE)
                    func.set_icon(self.title_icon, icon[0], icon[2])
                    self.title_layout.addWidget(self.title_icon)
                self.title_layout.addWidget(self.title_label)

                self.section_layout.addLayout(self.title_layout)

            self.groupbox = QGroupBox()
            self.groupbox.setStyleSheet(style.QGROUPBOX)

            self.groupbox.setLayout(self.outer_layout_type)
            self.section_layout.addWidget(self.groupbox)
        else:
            self.section_layout.addLayout(self.outer_layout_type)

        if self.scroll[0] == True:
            if len(self.inner_layouts) > 1:
                raise ValueError("Scroll layouts can't have more than 1 widget layout")
            else:
                self.scroll_area_widget = QScrollArea()
                self.scroll_area_widget.setObjectName("scroll_widget")
                i_layout = self.inner_layouts[0]
                self.scroll_widget = QWidget()
                self.scroll_widget.setObjectName("scroll_widget")
                self.scroll_widget.setLayout(i_layout)
                self.scroll_area_widget.setWidget(self.scroll_widget)

                if self.scroll[1] == "top":
                    i_layout.setAlignment(Qt.AlignTop)
                else:
                    i_layout.setAlignment(Qt.AlignBottom)

                i_layout.setSpacing(spacing)
                i_layout.setContentsMargins(0, 0, 0, 0)

                self.scroll_area_widget.setWidgetResizable(True)
                self.scroll_area_widget.setHorizontalScrollBarPolicy(
                    Qt.ScrollBarAlwaysOff
                )

                self.scroll_widget.setStyleSheet(style.QGROUPBOX)
                self.scroll_area_widget.setStyleSheet(style.QGROUPBOX)

                self.outer_layout_type.addWidget(self.scroll_area_widget)
        else:
            for layout in self.inner_layouts:
                self.outer_layout_type.addLayout(layout)

        self.all_sections.append(self)
        self.class_group.append(self)

        self.setLayout(self.section_layout)

    def inner_layout_list(self):
        self.all_inner_layouts = []
        for number in range(self.inner_layout_count):
            if self.inner_layout_type == "VBox":
                i_layout = QVBoxLayout()
            else:
                i_layout = QHBoxLayout()
            self.all_inner_layouts.append(i_layout)

        return self.all_inner_layouts

    def inner_layout(self, count):
        return self.all_inner_layouts[count - 1]

    def outer_layout(self):
        return self.section_layout

    def connect_to_parent(self):
        if self.parent_layout != None:
            self.parent_layout.addWidget(self)

    def get_group(self):
        return self.groupbox

    def get_title(self):
        return (self.title_icon,self.title_label,self.title_layout)

class Widget:
    all_widgets = []

    def __init__(
        self,
        widget_type,
        parent_layout=None,
        text="",
        tooltip="",
        objectname="",
        signal="",
        icon=("", 30, 0, 0),
        width="",
        height="",
        align="",
        enabled=True,
        checkable=False,
        validator="",
        placeholder="",
        setting="",
        stylesheet="",
        size_policy=None,
        checked=False,
        property=("",""),
        class_group=[]
    ):
        self.class_group = class_group
        self.text = text
        self.widget = widget_type
        if isinstance(self.widget, QComboBox):
            self.setup_combobox(self.widget, text)
        if isinstance(self.widget, QPushButton):
            self.widget.setFocusPolicy(Qt.NoFocus)
        self.parent_layout = parent_layout
        self.object = objectname
        self.setting = setting
        self.widget.setToolTip(tooltip)
        self.widget.setObjectName(self.object)
        self.widget.setStyleSheet(stylesheet)
        self.widget.setProperty(property[0],property[1])
        self.widget_key = f"{self.object}_{self.setting}"
        self.signal = signal
        self.set_enabled(enabled)
        self.set_checkable(checkable, checked)
        self.set_text(self.widget, self.text)
        self.set_alignment(self.widget, align)
        self.set_size(self.widget, width, height)
        self.set_validator(self.widget, validator)
        self.set_placeholder(self.widget, placeholder)
        self.load_setting(self.setting)
        if icon[0] != "":
            if len(icon) == 4:
                pix_width = icon[3]
            else:
                pix_width = 0
            func.set_icon(self.widget, icon[0], icon[2], width=pix_width)
        if size_policy != None:
            self.widget.setSizePolicy(size_policy[0], size_policy[1])

        self.all_widgets.append(self)
        self.class_group.append(self)

    def setup_combobox(self, widget, text):
        widget.setSizeAdjustPolicy(QComboBox.AdjustToMinimumContentsLength)
        widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        model = QStandardItemModel(widget)

        widget.setEditable(True)
        widget.lineEdit().setReadOnly(True)
        widget.lineEdit().setAlignment(Qt.AlignCenter)

        # Add items to the model and center their text
        for i, item in enumerate(text):
            si = QStandardItem(item)
            si.setData(Qt.AlignCenter, Qt.TextAlignmentRole)
            model.appendRow(si)
        # Set the model for the combo box
        widget.setModel(model)

    def load_setting(self, setting):
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
                if self.setting == "button":
                    self.widget.setText(open_json[self.widget_key])
        else:
            pass
        # self.save_setting()

    def save_setting(self):
        if os.path.exists(cons.SETTINGS):
            open_json = json.load(open(cons.SETTINGS, "r"))
        else:
            json.dump({}, open(cons.SETTINGS, "w"), indent=4)
            open_json = json.load(open(cons.SETTINGS, "r"))

        if self.setting == "button":
            open_json[self.widget_key] = self.widget.text()
        if self.setting == "text":
            open_json[self.widget_key] = self.widget.text()
        elif self.setting == "value":
            open_json[self.widget_key] = self.widget.value()
        elif self.setting == "checked":
            open_json[self.widget_key] = self.widget.isChecked()
        elif self.setting == "items":
            open_json[self.widget_key] = self.widget.currentText()
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
            regex = QRegExp("^(0\.[1-9]|[1-9]?[0-9])(\.[0-9]{1,2})?$")
            validator = QRegExpValidator(regex)
            widget.setValidator(validator)
        else:
            pass

    def set_checkable(self, checkable, checked):
        try:
            self.widget.setCheckable(checkable)
            self.widget.setChecked(checked)
        except:
            pass

    def get_inner_layout(self, layout):
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
            widget.setPlainText(text)
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

    def set_signal(self):
        if self.setting == "checked":
            self.widget.clicked.connect(self.save_setting)
        elif self.setting == "text":
            self.widget.textEdited.connect(self.save_setting)

        if self.signal != "":
            try:
                self.widget.currentIndexChanged.connect(self.signal)
            except:
                pass
            try:
                self.widget.editingFinished.connect(self.signal)
            except:
                pass
            try:
                self.widget.clicked.connect(self.signal)
                return
            except:
                pass

    def connect_to_parent(self):
        self.parent_layout.addWidget(self.widget)




