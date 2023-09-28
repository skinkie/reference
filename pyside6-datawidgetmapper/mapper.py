#!/usr/bin/env python
# -*- coding: utf-8 -*-

from  PySide6.QtWidgets import (QWidget, QDataWidgetMapper,
                              QLineEdit, QApplication, QGridLayout, QListView)
from PySide6.QtCore import Qt, QAbstractTableModel, QModelIndex

from utils import create_diff

class MyQLineEdit(QLineEdit):
    def __init__(self, parent=None):
        super(MyQLineEdit, self).__init__(parent)

class Window(QWidget):
    def __init__(self, parent=None):
        super(Window, self).__init__(parent)

        # Set up the widgets.
        self.nameEdit = MyQLineEdit()
        self.nameEdit2 = MyQLineEdit()

        # set up the layout
        layout = QGridLayout()
        layout.addWidget(self.nameEdit, 0, 1, 1, 1)
        layout.addWidget(self.nameEdit2, 0, 2, 1, 1)
        self.setLayout(layout)

        self.mapper = None

    def setModel(self, model):
        # Set up the mapper.
        self.mapper = QDataWidgetMapper(self)
        self.mapper.setModel(model)
        self.mapper.addMapping(self.nameEdit, 0)
        self.mapper.addMapping(self.nameEdit2, 1)
        self.mapper.toFirst()
        
        self.nameEdit.textEdited.connect(self.mapper.submit)
        self.nameEdit2.textEdited.connect(self.mapper.submit)


class MyModel(QAbstractTableModel):
    def __init__(self, data, parent=None):
        QAbstractTableModel.__init__(self, parent)
        self.lst = data

    def columnCount(self, parent=QModelIndex()):
        return len(self.lst[0])

    def rowCount(self, parent=QModelIndex()):
        return len(self.lst)

    def data(self, index, role=Qt.DisplayRole):
        row = index.row()
        col = index.column()

        if role == Qt.EditRole:
            return self.lst[row][col]
        elif role == Qt.DisplayRole:
            return self.lst[row][col]

    def flags(self, index):
        flags = super(MyModel, self).flags(index)

        if index.isValid():
            flags |= Qt.ItemIsEditable
            flags |= Qt.ItemIsDragEnabled
        else:
            flags = Qt.ItemIsDropEnabled

        return flags

    def setData(self, index, value, role=Qt.EditRole):

        if not index.isValid() or role != Qt.EditRole:
            return False

        create_diff(None, None, self.lst[index.row()][index.column()], value)

        self.lst[index.row()][index.column()] = value
        self.dataChanged.emit(index, index)
        return True


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    myModel = MyModel([['row 1 col1', 'row 1 col2'],
                       ['row 2 col1', 'row 2 col2'],
                       ['row 3 col1', 'row 3 col2'],
                       ['row 4 col1', 'row 4 col2']])

    # myModel = MyModel()
    mywindow = Window()
    mywindow.setModel(myModel)

    qlistview2 = QListView()
    qlistview2.setModel(myModel)

    mywindow.show()
    qlistview2.show()

    sys.exit(app.exec())
