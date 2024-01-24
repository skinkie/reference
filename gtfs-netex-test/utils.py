from typing import T
from netex import ScheduledStopPoint

def project(obj, clazz: T) -> T:
    # if issubclass(obj.__class__, clazz_intermediate):
    attributes = {x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())}
    attributes['id'] = attributes['id'].replace(obj.__class__.__name__, clazz.__name__)
    return clazz({x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())})
