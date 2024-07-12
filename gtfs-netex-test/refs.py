import datetime
from typing import Optional, List, T

from netex import *

def getRef(obj: object, klass=None):
    if obj is None:
        return None

    if klass == None:
        asobj = type(obj).__name__ + 'Ref' # Was: RefStructure
        klass = globals()[asobj]

    if hasattr(obj, 'id'):
        instance = klass(ref = obj.id)
    elif hasattr(obj, 'ref'):
        instance = klass(ref = obj.ref)

    if hasattr(instance, 'order'):
        instance.order = obj.order

    name = type(obj).__name__
    if hasattr(obj, 'Meta') and hasattr(obj.Meta, 'name'):
        name = obj.Meta.name
    elif name.endswith('RefStructure'):
        name = name.replace('RefStructure', 'Ref')

    if hasattr(obj, 'version'):
        instance.version = obj.version

    kname = klass.__name__
    meta_kname = klass.__name__
    if hasattr(klass, 'Meta') and hasattr(klass.Meta, 'name'):
        meta_kname = klass.Meta.name

    if not (kname.startswith(name) or meta_kname.startswith(name)):
        instance.name_of_ref_class = name
    return instance

def getFakeRef(id: str, klass: T, version: str) -> T:
    if id is None:
        return None

    instance = klass(ref=id, version=version)
    return instance

def getIdByRef(obj: object, codespace: Codespace, ref: str):
    name = type(obj).__name__
    if hasattr(obj.Meta, 'name'):
        name = obj.Meta.name
    return "{}:{}:{}".format(codespace.xmlns, name, str(ref).replace(':', '-'))

from operator import attrgetter

def getIndex(l: List[T], attr=None) -> dict[object, T]:
    if not attr:
        return {x.id:x for x in l }

    f = attrgetter(attr)
    return  {f(x):x for x in l }

def setIdVersion(obj: object, codespace: Codespace, id: str, version: Optional[Version]):
    name = type(obj).__name__
    if hasattr(obj.Meta, 'name'):
        name = obj.Meta.name
    obj.id = "{}:{}:{}".format(codespace.xmlns, name, str(id).replace(':', '-'))
    if version:
        obj.version = version.version
    else:
        obj.version = "any"

def getId(clazz, codespace: Codespace, id: str):
    name = getattr(clazz.Meta, 'name', clazz.__name__)
    return "{}:{}:{}".format(codespace.xmlns, name, str(id).replace(':', '-'))

def getVersionOfObjectRef(obj: object):
    return VersionOfObjectRefStructure(name_of_ref_class=type(obj).__name__, ref=obj.id)

def getBitString2(available: list, f_orig = None, t_orig = None):
    l = sorted(available)
    if f_orig is None:
        f_orig = l[0]
    if t_orig is None:
        t_orig = l[-1]

    f = f_orig

    out = ''
    while f <= t_orig:
        out += str(int(f in l))
        f += datetime.timedelta(days=1)

    return out

def getOptionalString(name: str):
    if name:
        return MultilingualString(value=name)
