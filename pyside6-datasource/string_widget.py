import signal
from dataclasses import Field
from enum import EnumType, Enum
from functools import lru_cache

import typing

import qtinter
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, Signal, Property
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit


class StringLineEdit(QtWidgets.QLineEdit):
    abstract_changed = Signal()
    optional: bool

    def __init__(self, str_type: str, optional: bool=False, parent=None):
        super(StringLineEdit, self).__init__(parent)
        self.optional = optional

        self.textEdited.connect(self.abstract_changed)

    def readText2(self):
        return self.text()

    def setText2(self, text: str) -> None:
        cursorposition = self.cursorPosition()
        self.setText(text)
        self.setCursorPosition(cursorposition)

    # This property allows us to restore the cursor position,
    # when it updates from an external source.
    text2 = Property(str, readText2, setText2, user=True)

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

class DataclassStringLineEdit(StringLineEdit):
    def __init__(self, field: Field, parent=None):
        str_type, optional = get_type(field.type)
        super(DataclassStringLineEdit, self).__init__(str_type, optional, parent)

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

    layout = QGridLayout()

    dccombobox = DataclassStringLineEdit(Version.__dataclass_fields__['id'])

    layout.addWidget(dccombobox)

    mywindow = QWidget()
    mywindow.setLayout(layout)
    mywindow.show()

    sys.exit(app.exec())
