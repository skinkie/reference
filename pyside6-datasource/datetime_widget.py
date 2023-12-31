import signal
from dataclasses import Field
from enum import EnumType, Enum
from functools import lru_cache

import typing

import qtinter
from PySide6 import QtWidgets, QtCore
from PySide6.QtCore import Slot, Signal, Property, QDateTime, QDate
from PySide6.QtWidgets import QApplication, QWidget, QGridLayout, QLineEdit

# Might want to implement, this does not work yet
# https://github.com/Qt-Widgets/QDateEditEx

class DateTimeEdit(QtWidgets.QDateTimeEdit):
    abstract_changed = Signal()
    optional: bool

    def __init__(self, str_type: str, optional: bool=False, parent=None):
        super(DateTimeEdit, self).__init__(parent)
        self.optional = optional
        self.setCalendarPopup(True)

        # HACK to get empty
        self.setSpecialValueText( " " )
        self.setMinimumDate(QDate.fromString("13/10/2023", "dd/MM/yyyy"))
        self.setDateTime(QDateTime.fromString("01/01/0001", "dd/MM/yyyy"))
        self.setDisplayFormat("yyyy-MM-ddThh:mm:ss")

        print(self.metaObject().userProperty().name())

        # self.textEdited.connect(self.abstract_changed)

    def clear(self) -> None:
        self.setDateTime(self.minimumDateTime())
    def readDateTimeNull(self):
        if self.dateTime() == self.minimumDateTime():
            return QDateTime()
        return self.dateTime()

    def setDateTimeNull(self, dateTime: QDateTime) -> None:
        if dateTime.isNull():
            self.setDateTime(self.minimumDateTime())
        else:
            self.setDateTime(dateTime)

    # This property allows us to restore the cursor position,
    # when it updates from an external source.
    dateTimeNull = Property(QDateTime, readDateTimeNull, setDateTimeNull, user=True)

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

class DataclassDateTimeEdit(DateTimeEdit):
    def __init__(self, field: Field, parent=None):
        str_type, optional = get_type(field.type)
        super(DataclassDateTimeEdit, self).__init__(str_type, optional, parent)

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

    dccombobox = DataclassDateTimeEdit(Version.__dataclass_fields__['id'])

    layout.addWidget(dccombobox)

    mywindow = QWidget()
    mywindow.setLayout(layout)
    mywindow.show()

    sys.exit(app.exec())
