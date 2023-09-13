import asyncio
import time
import y_py as Y
from websockets import connect
from ypy_websocket import WebsocketProvider
from diff_match_patch import diff_match_patch

class Timer:
    def __init__(self, timeout, callback, recurring=False):
        self._timeout = timeout
        self._callback = callback
        self.recurring = recurring
        self._task = asyncio.ensure_future(self._job())

    async def _job(self):
        await asyncio.sleep(self._timeout)
        await self._callback()
        if self.recurring:
            self._task = asyncio.ensure_future(self._job())

    def cancel(self):
        self._task.cancel()

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

def doc_updated(ymap):
    print(ymap.target.to_json())

async def force_update():
    global ydoc
    with ydoc.begin_transaction() as txn:
        # ydoc.get_map("document1").set(txn, "hello", str(int(time.time())))
        ytext: Y.YText
        ytext = ydoc.get_map("document1").get("hello")
        if not isinstance(ytext, Y.YText):
            ytext = Y.YText()
            ydoc.get_map("document1").set(txn, "hello", ytext)
        else:
            create_diff(txn, ytext, str(ytext), str(int(time.time())))
            # ytext.delete_range(txn, 0, len(str(ytext)))
            # ytext.extend(txn, "Hello world")

ydoc = Y.YDoc()

async def client():
    async with (connect("ws://localhost:1234/my-roomname") as websocket, WebsocketProvider(ydoc, websocket)):
        # ydoc.get_map("document1").observe(doc_updated)

        timer = Timer(2, force_update, True)

        await asyncio.Future()

asyncio.run(client())