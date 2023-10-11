from dataclasses import Field
from enum import EnumType, Enum
from functools import lru_cache

import typing
from PySide6 import QtWidgets, QtCore
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit


class EnumerationModel(QtCore.QAbstractListModel):
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
    def __init__(self, enum_type: EnumType, optional: bool=False, parent=None):
        super(EnumerationComboBox, self).__init__(parent)
        model = EnumerationModel(enum_type, optional)
        self.setModel(model)

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
    def __init__(self, field: Field, parent=None):
        enum_type, optional = get_type(field.type)
        super(DataclassEnumerationComboBox, self).__init__(enum_type, optional, parent)

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

    layout = QGridLayout()
    combobox = EnumerationComboBox(VersionTypeEnumeration)
    layout.addWidget(combobox)

    dccombobox = DataclassEnumerationComboBox(VersionVersionStructure.__dataclass_fields__['version_type'])
    layout.addWidget(dccombobox)

    mywindow = QWidget()
    mywindow.setLayout(layout)
    mywindow.show()

    sys.exit(app.exec())
