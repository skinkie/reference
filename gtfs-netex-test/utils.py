from typing import T

def project(obj, clazz: T) -> T:
    # if issubclass(obj.__class__, clazz_intermediate):
    attributes = {x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())}
    if 'id' in attributes:
        attributes['id'] = attributes['id'].replace(f":{obj.__class__.__name__}:", f":{clazz.__name__}:")
    # return clazz({x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys())})
    return clazz(**attributes)
