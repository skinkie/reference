import signal
from dataclasses import Field

from PySide6.QtWidgets import QGroupBox, QFormLayout, QApplication, QWidget

from mro_attributes import list_attributes
from netex.data_source import DataSource
from string_widget import DataclassStringLineEdit
from multiligualstring_widget import DataclassMultiLingualStringLineEdit
from enumeration_widget import DataclassEnumerationComboBox
from datetime_widget import DataclassDateTimeEdit
from netex.key_value_structure import KeyValueStructure

def create_label(name, mytype, optional, default, field: Field):
    label = field.name
    if hasattr(field, 'metadata') and 'name' in field.metadata:
        label = field.metadata['name']

    if not optional:
        label += ' (*)'

    return label


def create_widget(name, mytype, optional, default, field: Field):
    widget_mapping = {
        'str': DataclassStringLineEdit,
        'MultilingualString': DataclassMultiLingualStringLineEdit,
        'XmlDateTime': DataclassDateTimeEdit,
        'EnumType': DataclassEnumerationComboBox,
    }

    if mytype.__name__ in widget_mapping:
        return widget_mapping[mytype.__name__](field, None)

    else:
        print(name, mytype)

def create_multiwidget(name, mytype, optional, default, field: Field, layout):
    print("\n" + name + "\n-----")
    for name, type_optional, default, field in mytype:
        if type_optional is not None:
            mytype, optional = type_optional

            label = create_label(name, mytype, optional, default, field)

            # Hier zou nog een onderscheid moeten worden gemaakt tussen het "resolved" type,
            # en waar we daadwerkelijk implementaties voor hebben.
            if type(mytype) == list:
                formlayout = QFormLayout()
                create_multiwidget(name, mytype, optional, default, field, formlayout)

                # TODO: https://github.com/eyalk11/qt-collapsible-section-pyside6
                groupbox = QGroupBox() # (name)
                groupbox.setLayout(formlayout)
                layout.addRow(label, groupbox)

            else:
                widget = create_widget(name, mytype, optional, default, field)
                layout.addRow(label, widget)
        else:
            print(name, 'failed')
    print("\n")

def print_attributes(dataclazz):
    mytype = list_attributes(dataclazz)
    formlayout = QFormLayout()
    create_multiwidget(dataclazz.__name__, mytype, None, None, None, formlayout)

    """
    for name, type_optional, default, field in list_attributes(dataclazz):
        if type_optional is not None:
            mytype, optional = type_optional
            create_multiwidget()
            if type(mytype) == list:
                create_multiwidget(name, mytype, optional, default, field)
            else:
                create_widget(name, mytype, optional, default, field)
        else:
            print(name)
    """

# print_attributes(DataSource)

if __name__ == '__main__':
    import sys
    app = QApplication(sys.argv)
    signal.signal(signal.SIGINT, lambda a, b: QApplication.quit())

    mywindow = QWidget()
    formlayout = QFormLayout()

    mytype = list_attributes(DataSource)
    create_multiwidget(DataSource.__name__, mytype, None, None, None, formlayout)

    mywindow.setLayout(formlayout)
    mywindow.show()

    sys.exit(app.exec())
