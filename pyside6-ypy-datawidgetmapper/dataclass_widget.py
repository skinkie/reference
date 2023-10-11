#!/usr/bin/env python
# -*- coding: utf-8 -*-
import qtinter
from PySide6.QtWidgets import (QWidget, QDataWidgetMapper,
                               QLineEdit, QApplication, QFormLayout)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

import signal
from dataclasses import Field
from enum import EnumType, Enum

from mro_attributes import list_attributes, likely_type
from enumeration_widget import EnumerationComboBox, DataclassEnumerationComboBox
from ydoc_worker import YDocWorker

class MyQLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MyQLineEdit, self).__init__(parent)


class MultilingualStringEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MultilingualStringEdit, self).__init__(parent)


"""
The GenericForm is used when no specific dataclazz has been defined
it should display all data attributes in vertical form
"""


class GenericModel(QAbstractTableModel):
    all_attributes: list

    def __init__(self, dataclazz, parent=None):
        super(GenericModel, self).__init__(parent)
        self.all_attributes = list_attributes(dataclazz)

    # TODO: Better place in the model?
    def get_attributes(self):
        return self.all_attributes

    def columnCount(self, parent=QModelIndex()):
        return 1  # TODO dependend on per row attributes?

    def rowCount(self, parent=QModelIndex()):
        return len(self.all_attributes)


# TODO: Make QFormLayout more generic QLayout
class GenericForm(QFormLayout):
    ydoc_worker: YDocWorker
    ydoc_path: str
    mapper: QDataWidgetMapper
    model: QAbstractTableModel
    widget_mapping: dict

    def __init__(self, dataclazz, ydoc_worker: YDocWorker=None, ydoc_path: str=None, parent=None):
        self.ydoc_worker = ydoc_worker
        self.yoc_path = ydoc_path

        super(GenericForm, self).__init__(parent)
        # TODO: Cache?
        self.model = GenericModel(dataclazz, parent=self)
        self.mapper = QDataWidgetMapper(parent=self)
        self.mapper.setModel(self.model)

        widget_mapping = {
            'str': MyQLineEdit,
            'MultilingualString': MultilingualStringEdit,
            'EnumType': DataclassEnumerationComboBox,
        }

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
            if str(lt) in widget_mapping:
                label = all_attributes[i][0]
                if hasattr(all_attributes[i][3], 'metadata') and 'name' in all_attributes[i][3].metadata:
                    label = all_attributes[i][3].metadata['name']

                if not optional:
                    label += ' (*)'

                w = widget_mapping[str(lt)](all_attributes[i][3], ydoc_worker, ydoc_path, None)
                # w.textEdited.connect(self.mapper.submit)
                self.addRow(label, w)
                self.mapper.addMapping(w, i)


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

    app = QApplication(sys.argv)
    signal.signal(signal.SIGINT, lambda a, b: QApplication.quit())

    with qtinter.using_asyncio_from_qt():
        ydoc_worker = YDocWorker()

        layout = GenericForm(VersionVersionStructure, ydoc_worker, "document1")

        # dccombobox = DataclassEnumerationComboBox(VersionVersionStructure.__dataclass_fields__['version_type'], ydoc_worker, "document1/testenum")

        # layout.addWidget(dccombobox)

        mywindow = QWidget()
        mywindow.setLayout(layout)
        mywindow.show()

        sys.exit(app.exec())
