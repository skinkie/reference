import signal
from dataclasses import Field
from enum import EnumType, Enum
from functools import lru_cache

import typing

import qtinter
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, Signal
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit
from y_py import YMapEvent

from ydoc_worker import YDocWorker

# The QAbstractListModel is used here as container to get access to individual items within the Enumeration
# it is not used to represent a column of a datastore. Therefore this model has nothing to do with Ydoc.
class EnumerationModel(QtCore.QAbstractListModel):
    ydoc_path: str
    enum_type: EnumType
    optional: bool
    def __init__(self, enum_type: EnumType, optional: bool=False, parent=None):
        QtCore.QAbstractListModel.__init__(self, parent)
        self.enum_type = enum_type
        self.optional = optional

    @lru_cache(maxsize=None)
    def rowCount(self, parent=QtCore.QModelIndex()):
        return len(self.enum_type) + int(self.optional)

    def index(self, row, column, parent):
        if row < 0 or row >= self.rowCount():
            return QtCore.QModelIndex()
        return self.createIndex(row, column)

    def data(self, index, role):
        if not index.isValid():
            return

        if role == QtCore.Qt.DisplayRole:
            if index.row() == 0 and self.optional:
                return ''

            row = index.row() - int(self.optional)
            return list(self.enum_type)[row].value

class EnumerationComboBox(QtWidgets.QComboBox):
    ydoc_signal = Signal(str, str)
    optional: bool
    ydoc_worker: YDocWorker
    ydoc_path: str
    propagate: bool = True

    def __init__(self, enum_type: EnumType, optional: bool=False, ydoc_worker: YDocWorker=None, ydoc_path: str=None, parent=None):
        super(EnumerationComboBox, self).__init__(parent)
        self.optional = optional
        self.ydoc_worker = ydoc_worker
        self.ydoc_path = ydoc_path

        model = EnumerationModel(enum_type, optional)
        self.setModel(model)

        if self.ydoc_worker:
            self.ydoc_worker.ydoc_signal.connect(self.ydocSlot)
            self.ydoc_worker.observe_map(self.ydoc_path)
            self.ydoc_signal.connect(self.ydoc_worker.update_map)

            self.currentIndexChanged.connect(self.ydocSignal)


    def ydocSignal(self):
        if not self.propagate:
            return

        value = self.currentText()
        if value == '' and self.optional:
            value = None

        print("ydocSignal", self.ydoc_path, value)
        self.ydoc_signal.emit(self.ydoc_path, value)

    @Slot(str, str)
    def ydocSlot(self, name: str, value: dict):
        sname, skey = self.ydoc_path.split('/')
        print('ydocSlot', name, value)

        if name == sname and skey in value:
            text = value[skey]
            if self.currentText() != text:
                self.propagate = False
                self.setCurrentText(text)
                self.propagate = True


def get_type(clazz):
    optional = False
    clazz_resolved = clazz

    if clazz == typing.List[object]:
        # We don't handle these yet
        return None

    if hasattr(clazz, '_name'):
        if clazz._name == 'Optional':
            optional = True
            clazz_resolved = [x for x in clazz.__args__ if x is not None.__class__][0]
        elif clazz._name == 'List':
            return None # TODO: handle list elements
        else:
            clazz_resolved = [x for x in clazz.__args__ if x is not None.__class__][0]

    return (clazz_resolved, optional)

class DataclassEnumerationComboBox(EnumerationComboBox):
    def __init__(self, field: Field, ydoc_worker: YDocWorker=None, ydoc_path: str=None, parent=None):
        enum_type, optional = get_type(field.type)
        super(DataclassEnumerationComboBox, self).__init__(enum_type, optional, ydoc_worker, ydoc_path, parent)

def update(name: str, msg: YMapEvent):
    print(name, msg)

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

        layout = QGridLayout()

        dccombobox = DataclassEnumerationComboBox(VersionVersionStructure.__dataclass_fields__['version_type'], ydoc_worker, "document1/testenum")
        ydoc_worker.ydoc_signal.connect(update)

        layout.addWidget(dccombobox)

        mywindow = QWidget()
        mywindow.setLayout(layout)
        mywindow.show()

        sys.exit(app.exec())
