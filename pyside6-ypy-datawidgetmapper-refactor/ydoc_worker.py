#!/usr/bin/env python
# -*- coding: utf-8 -*-
import asyncio
import signal
from functools import partial
import y_py as Y


import qtinter
from PySide6.QtCore import QObject, Signal, Slot
from PySide6.QtWidgets import (QWidget, QDataWidgetMapper,
                               QLineEdit, QApplication, QGridLayout, QListView)
from y_py import YDoc, YMapEvent
from ypy_websocket import WebsocketProvider
from websockets import connect
from diff_match_patch import diff_match_patch


def create_diff(txn, ytext, current_text, widget_text):
    dmp = diff_match_patch()
    d = dmp.diff_main(current_text, widget_text)
    dmp.diff_cleanupSemanticLossless(d)
    print(d)
    index = 0
    last = len(d) - 1
    for r in range(0, len(d)):
        s, chunk = d[r]
        l = len(chunk)
        if s == -1:
            if l == 1:
                ytext.delete(txn, index)
            else:
                ytext.delete_range(txn, index, l)
        elif s == 1:
            if r != last:
                ytext.insert(txn, index, chunk)
            else:
                ytext.extend(txn, chunk)

        index += l
class YDocWorker(QObject):
    ydoc_signal = Signal(str, YMapEvent)
    ydoc_observations = {}
    ydoc_subscription_ids = {}
    ydoc: YDoc()
    
    def __init__(self, *args, **kwargs):
        QObject.__init__(self)
        self.ydoc = YDoc()
        self._task = asyncio.create_task(self._connect())

    @Slot(str)
    def observe_map(self, name: str, observed_ydoc_slot):
        print(name)
        counter = self.ydoc_observations.get(name, 0)
        if counter == 0:
            print("SUBSCRIBE: " + name)
            self.ydoc_subscription_ids[name] = self.ydoc.get_map(name).observe_deep(partial(self.sender_map, name))

        self.ydoc_signal.connect(observed_ydoc_slot)
        self.ydoc_observations[name] = counter + 1

    def sender_map(self, name: str, ymap_event: YMapEvent):
        mytype = type(ymap_event[0])
        if mytype ==  YMapEvent:
            self.ydoc_signal.emit(name, dict(ymap_event[0].target))
        elif mytype == Y.YTextEvent:
            self.ydoc_signal.emit(name, {str(ymap_event[0].path()[0]): str(ymap_event[0].target)})

    @Slot(str, str, str)
    def update_map(self, name: str, value: str, type: str=None):
        name, key = name.split('/')
        print("update_map", name, key)
        with self.ydoc.begin_transaction() as txn:
            if type == 'text':
                ytext: Y.YText
                ytext = self.ydoc.get_map(name).get(key)
                if not isinstance(ytext, Y.YText):
                    ytext = Y.YText(value)
                    self.ydoc.get_map(name).set(txn, key, ytext)
                else:
                    create_diff(txn, ytext, str(ytext), value)
            else:
                self.ydoc.get_map(name).set(txn, key, value)

    @Slot(str, str)
    def update_text(self, name: str, value: str):
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
