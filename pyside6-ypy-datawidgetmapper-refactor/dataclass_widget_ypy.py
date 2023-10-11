#!/usr/bin/env python
# -*- coding: utf-8 -*-
import qtinter
from PySide6.QtWidgets import (QWidget, QDataWidgetMapper,
                               QLineEdit, QApplication, QFormLayout)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex, Signal, Slot

import signal
from dataclasses import Field
from enum import EnumType, Enum

from mro_attributes import list_attributes, likely_type
from enumeration_widget import DataclassEnumerationComboBox
from string_widget import DataclassStringLineEdit
from multiligualstring_widget import DataclassMultiLingualStringLineEdit
from ydoc_worker import YDocWorker

from netex import DataSource, ScheduledStopPoint

class MyQLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MyQLineEdit, self).__init__(parent)


"""
The GenericForm is used when no specific dataclazz has been defined
it should display all data attributes in vertical form
"""
from collections import OrderedDict

class GenericModel(QAbstractTableModel):
    ydoc_signal = Signal(str, str, str)
    ydoc_worker: YDocWorker
    ydoc_path: str
    all_attributes: list
    index_attributes: dict
    ytype_attributes: list

    test: list

    widget_list: dict

    # TODO: If this is an abstract table, we might actually want to have a list (preferably of the same type)
    # TODO: as input, and use this as an interface to crawl through the data, that is possible if we would
    # TODO: take the dataclazz as some sort of filter in a database
    def __init__(self, dataclazz, ydoc_worker: YDocWorker=None, ydoc_path: str=None, parent=None):
        self.ydoc_worker = ydoc_worker
        self.ydoc_path = ydoc_path


        super(GenericModel, self).__init__(parent)
        self.all_attributes = list_attributes(dataclazz)
        self.index_attributes = {self.all_attributes[i][0]: i for i in range(0, len(self.all_attributes))}
        self.ytype_attributes = [likely_type(x[3]) for x in self.all_attributes]

        self.test = [['' for x in self.all_attributes]]

        if self.ydoc_worker:
            self.ydoc_worker.observe_map(self.ydoc_path, self.ydocSlot)
            self.ydoc_signal.connect(self.ydoc_worker.update_map)

    # Receives a messages from the YDocWorker thread
    @Slot(str, str)
    def ydocSlot(self, name: str, value: dict):
        print('ydocSlot', name, value)

        if name == self.ydoc_path:
            for key in value.keys():
                # TODO: it might be we can save on individual elements, if we would expect entire fragments
                # TODO: to arrive, in that case we would like to update the min to max index, and have the widget
                # TODO: read the range
                col = self.index_attributes.get(key, None)
                print("Emit datachange for index " + str(col))
                if col is not None:
                    row = 0 # TODO: fetch row
                    if self.ytype_attributes[col] == 'str':
                        self.test[row][col] = str(value[key])
                    else:
                        self.test[row][col] = value[key]

                    # HACK: Is there any other way so we can retain the current cursor position before the model updates?
                    cursorPositions = []
                    if col in self.widget_list:
                        cursorPositions = [(x, x.cursorPosition()) for x in self.widget_list[col]]

                    self.dataChanged.emit(self.index(0, col), self.index(0, col))

                    [w.setCursorPosition(c) for w, c in cursorPositions]


    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        col = index.column()

        if role == Qt.EditRole:
            return self.test[row][col]
            # return self.lst[row][col]
        elif role == Qt.DisplayRole:
            return self.test[row][col]
            # return self.lst[row][col]

    def setData(self, index: QModelIndex, value, role=Qt.EditRole) -> bool:
        row = index.row()
        col = index.column()

        print(row, col)

        if self.test[row][col] == value:
            return True

        print("Setting: " + self.test[row][col] + " -> " + value)

        self.test[row][col] = value

        # This is disabled, because we likely receive the edit via the ydocSlot
        # there we handle the moving cursor, prior to updating
        # self.dataChanged.emit(index, index)

        path = self.ydoc_path + "/" + self.all_attributes[col][0]

        print("ydocSignal", path, value)
        if self.ytype_attributes[col] == 'str':
            self.ydoc_signal.emit(path, value, 'text')
        else:
            self.ydoc_signal.emit(path, value, 'map')

        return True

    def set_widget_list(self, widget_list: list):
        self.widget_list = widget_list

    # TODO: Better place in the model?
    def get_attributes(self):
        return self.all_attributes

    def columnCount(self, parent=QModelIndex()):
        return len(self.all_attributes)  # TODO dependend on per row attributes?

    def rowCount(self, parent=QModelIndex()):
        return 1


# TODO: Make QFormLayout more generic QLayout
class GenericForm(QFormLayout):
    mapper: QDataWidgetMapper
    model: QAbstractTableModel
    widget_mapping: dict

    def __init__(self, dataclazz, ydoc_worker: YDocWorker=None, ydoc_path: str=None, parent=None):
        super(GenericForm, self).__init__(parent)
        # TODO: Cache?
        self.model = GenericModel(dataclazz, ydoc_worker, ydoc_path, parent=self)
        self.mapper = QDataWidgetMapper(parent=self)
        self.mapper.setModel(self.model)

        widget_mapping = {
            'str': DataclassStringLineEdit,
            'MultilingualString': DataclassMultiLingualStringLineEdit,
            'EnumType': DataclassEnumerationComboBox,
        }

        widget_list = {}
        all_attributes = self.model.get_attributes()

        for i in range(0, len(all_attributes)):
            lt = likely_type(all_attributes[i][3])

            if all_attributes[i][1] is None:
                # TODO: handle 'rel' objects
                continue

            mytype, optional = all_attributes[i][1]
            if not isinstance(mytype, type):
                # TODO: handle list objects
                continue

            print(all_attributes[i], mytype, lt, optional)

            lt = mytype.__name__
            print(lt)
            if str(lt) in widget_mapping:
                label = all_attributes[i][0]
                if hasattr(all_attributes[i][3], 'metadata') and 'name' in all_attributes[i][3].metadata:
                    label = all_attributes[i][3].metadata['name']

                if not optional:
                    label += ' (*)'

                w = widget_mapping[str(lt)](all_attributes[i][3])
                w.abstract_changed.connect(self.mapper.submit)
                self.addRow(label, w)
                self.mapper.addMapping(w, i)

                # HACK: Is there any other way so we can retain the current cursor position before the model updates?
                # https://stackoverflow.com/questions/15801259/qlineedit-cursor-moves-to-end-after-textchanged-or-commitdata
                # https://stackoverflow.com/questions/14145110/qtextedit-change-carriage-position-after-settext

                if str(lt) == 'str':
                    wl = widget_list.setdefault(i, [])
                    wl.append(w)

                print(label, i)

        self.model.set_widget_list(widget_list)
        self.mapper.toFirst()

if __name__ == '__main__':
    import sys

    from dataclasses import dataclass, field
    from typing import Optional

    __NAMESPACE__ = "http://www.netex.org.uk/netex"



    class VersionTypeEnumeration(Enum):
        """
        Allowed values for Types of VERSION.
        """
        POINT = "point"
        BASELINE = "baseline"

    @dataclass(unsafe_hash=True, kw_only=True)
    class VersionVersionStructure():
        """
        Type for a VERSION.

        :ivar start_date: Date of start of VERSION currency.
        :ivar end_date: Date of end of VERSION currency. Date is INCLUSIVE.
        :ivar status: Status of VERSION.
        :ivar description:
        :ivar version_type: Version type: Point or Baseline.
        :ivar type_of_version_ref:
        :ivar derived_from_version_ref: Reference to VERSION from which this
            VERSION was derived.
        """

        class Meta:
            name = "Version_VersionStructure"

        version_type: Optional[VersionTypeEnumeration] = field(
            default=None,
            metadata={
                "name": "VersionType",
                "type": "Element",
                "namespace": "http://www.netex.org.uk/netex",
            }
        )

    @dataclass(unsafe_hash=True, kw_only=True)
    class Version(VersionVersionStructure):
        """A group of operational data instances which share the same VALIDITY
        CONDITIONs.

        A VERSION belongs to a unique VERSION FRAME and is characterized by
        a unique TYPE OF VERSION. E.g.  NETWORK VERSION for Line 12 starting
        from 2000-01-01.
        """

        class Meta:
            namespace = "http://www.netex.org.uk/netex"

        id: str = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )



    app = QApplication(sys.argv)
    signal.signal(signal.SIGINT, lambda a, b: QApplication.quit())

    with qtinter.using_asyncio_from_qt():
        ydoc_worker = YDocWorker()

        layout = GenericForm(ScheduledStopPoint, ydoc_worker, "document1")

        # dccombobox = DataclassEnumerationComboBox(VersionVersionStructure.__dataclass_fields__['version_type'], ydoc_worker, "document1/testenum")

        # layout.addWidget(dccombobox)

        mywindow = QWidget()
        mywindow.setLayout(layout)
        mywindow.show()

        sys.exit(app.exec())
