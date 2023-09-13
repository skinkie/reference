# Integration between pyside6 and ypy

This folder gives a practical implementation how to use asynchronous ypy code in concert with the Qt6 in python.
The foundation that should be run first is `ypy-server.py` which creates a websockets server at localhost:1234.
In order to have a client that continously produces data `ypy-client-sync.py` was created.
The actual integration with `pyside6` and `qtinter` can be found in `pyside6-ypy.py`.

It is possible to dynamically observer multiple elements within a room, having a single YDoc.
It is not possible to create dynamic signals, which for example subscribe parts, since we cannot emit this.
We can emit messages with a certain topic and have the filtering done on the receiver side.
Here everyone signal-slot would receive every message.

### TODO
1. Investigate if a publish-subscribe pattern can be used

