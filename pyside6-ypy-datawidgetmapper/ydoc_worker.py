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
    ydoc_observations = {}
    ydoc_subscription_ids = {}
    ydoc_signals = {}
    ydoc: YDoc()
    
    def __init__(self, *args, **kwargs):
        QObject.__init__(self)
        self.ydoc = YDoc()
        self._task = asyncio.create_task(self._connect())

    @Slot(str)
    def observe_map(self, name: str):
        name, key = name.split('/')
        print(name)
        counter = self.ydoc_observations.get(name, 0)
        if counter == 0:
            print("SUBSCRIBE: " + name)
            self.ydoc_subscription_ids[name] = self.ydoc.get_map(name).observe_deep(partial(self.sender_map, name))
        self.ydoc_observations[name] = counter + 1

    def sender_map(self, name: str, ymap_event: YMapEvent):
        self.ydoc_signal.emit(name, dict(ymap_event[0].target))

    @Slot(str, str)
    def update_map(self, name: str, value: str):
        name, key = name.split('/')
        print("update_map", name, key)
        with self.ydoc.begin_transaction() as txn:
            self.ydoc.get_map(name).set(txn, key, value)

    @Slot(str)
    def observe(self, name: str):
        print(name)
        counter = self.ydoc_observations.get(name, 0)
        if counter == 0:
            self.ydoc_subscription_ids[name] = self.ydoc.get_map(name).observe_deep(partial(self.ydoc_signal.emit, name))
        self.ydoc_observations[name] = counter + 1

    @Slot(str)
    def unobserve(self, name: str):
        counter = self.ydoc_observations.get(name, 0)
        if counter > 0:
            counter = counter - 1
            if counter == 0:
                self.ydoc.get_map(name).unobserve(self.ydoc_subscription_ids[name])
                del self.ydoc_subscription_ids[name]
                del self.ydoc_observations[name]
                print('released')
 
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
        # worker.observe("document2")
        # worker.unobserve("document1")
        # worker.unobserve("document2")

        sys.exit(app.exec())
