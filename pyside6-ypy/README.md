# Integration between pyside6 and ypy

This folder gives a practical implementation how to use asynchronous ypy code in concert with the Qt6 in python.
The foundation that should be run first is `ypy-server.py` which creates a websockets server at localhost:1234.
In order to have a client that continously produces data `ypy-client-sync.py` was created.
The actual integration with `pyside6` and `qtinter` can be found in `pyside6-ypy.py`.

It is possible to dynamically observer multiple elements within a room, having a single YDoc.

### TODO
1. Deduplicate the observe calls.
2. Investigate if a publish-subscribe pattern can be used
3. Investigate if unobserve could and should be implemented by a form of garbage collection

