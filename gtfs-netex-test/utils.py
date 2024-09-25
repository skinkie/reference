import warnings
from typing import T
from xsdata.models.datatype import XmlDateTime, XmlDuration

def project(obj, clazz: T) -> T:
    # if issubclass(obj.__class__, clazz_intermediate):
    attributes = {x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())}
    if 'id' in attributes:
        attributes['id'] = attributes['id'].replace(f":{obj.__class__.__name__}:", f":{clazz.__name__}:")
    # return clazz({x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())})
    return clazz(**attributes)

def to_seconds(xml_duration: XmlDuration):
    if xml_duration.months is not None and xml_duration.months > 0:
        warnings.warn("Duration is bigger than a month!")
    return ((xml_duration.days * 24 + xml_duration.hours) * 3600) + (xml_duration.minutes * 60) + (xml_duration.seconds)