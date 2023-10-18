import netex
import inspect
members = inspect.getmembers(netex)
class_list = [x[1] for x in members]