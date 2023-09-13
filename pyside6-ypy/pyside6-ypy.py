#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import signal
from functools import partial

import qtinter
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import (QWidget, QDataWidgetMapper,
                               QLineEdit, QApplication, QGridLayout, QListView)
from y_py import YDoc, YMapEvent
from ypy_websocket import WebsocketProvider
from websockets import connect

class YDocWorker(QObject):
    ydoc_signal = Signal(str, YMapEvent)
    ydoc: YDoc()
    
    def __init__(self, *args, **kwargs):
        QObject.__init__(self)
        self.ydoc = YDoc()
        self._task = asyncio.create_task(self._connect())

    @Slot(str)
    def observe(self, name: str):
        print(name)
        self.ydoc.get_map(name).observe_deep(partial(self.ydoc_signal.emit, name))

    async def _connect(self):
        print("server link")
        async with (
            connect("ws://localhost:1234/my-roomname") as websocket,
            WebsocketProvider(self.ydoc, websocket),
        ):
            print("joined")
            await asyncio.Future()  # run forever

def update(name: str, msg: YMapEvent):
    print(name, msg)

if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)

    signal.signal(signal.SIGINT, lambda a, b: QApplication.quit())

    with qtinter.using_asyncio_from_qt():
        worker = YDocWorker()
        worker.ydoc_signal.connect(update)
        worker.observe("document1")
        worker.observe("document2")

        sys.exit(app.exec())
