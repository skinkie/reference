import inspect
import netex
import warnings
from typing import T, Generator
from xsdata.models.datatype import XmlDateTime, XmlDuration

def get_object_name(clazz: T) -> str:
    return getattr(clazz.Meta, 'name', clazz.__name__)

def get_element_name_with_ns(clazz):
    name = get_object_name(clazz)
    return "{" + clazz.Meta.namespace + "}" + name

def project(obj, clazz: T) -> T:
    # if issubclass(obj.__class__, clazz_intermediate):
    attributes = {x: y for x, y in obj.__dict__.items() if x in list(clazz.__dataclass_fields__.keys()) if (hasattr(clazz.__dataclass_fields__[x], 'init') and clazz.__dataclass_fields__[x].init != False)}
    if 'id' in attributes:
        attributes['id'] = attributes['id'].replace(f":{get_object_name(obj.__class__)}:", f":{get_object_name(clazz)}:")

    return clazz(**attributes)

def to_seconds(xml_duration: XmlDuration):
    if xml_duration.months is not None and xml_duration.months > 0:
        warnings.warn("Duration is bigger than a month!")
    return (((xml_duration.days or 0) * 24 + (xml_duration.hours or 0)) * 3600) + ((xml_duration.minutes or 0) * 60) + (xml_duration.seconds or 0)

def dontsetifnone(clazz, attr, value):
    if value is None:
        return None

    try:
        first = value.__next__()
    except StopIteration:
        return None
    else:
        return clazz(**{attr: chain([first],value)})

def chain(*iterables) -> Generator:
    for it in iterables:
        for element in it:
            yield element

class GeneratorTester:
    def __init__(self, value):
        self._has_value = None
        self.value = value

    def has_value(self) -> bool:
        if self._has_value is not None:
            return self._has_value

        try:
            self.first = self.value.__next__()
            self._has_value = True
        except StopIteration:
            self._has_value = False
            pass

        return self._has_value

    def generator(self) -> Generator | None:
        if self._has_value is None:
            return self.value

        elif self._has_value:
            return chain([self.first], self.value)

        return None

def get_boring_classes():
    # Get all classes from the generated NeTEx Python Dataclasses
    clsmembers = inspect.getmembers(netex, inspect.isclass)

    # The interesting class members certainly will have a "Meta class" with a namespace
    interesting_members = [x[1] for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1].Meta, 'namespace')]

    return interesting_members

def get_interesting_classes(filter=None):
    # Get all classes from the generated NeTEx Python Dataclasses
    clsmembers = inspect.getmembers(netex, inspect.isclass)

    # The interesting class members certainly will have a "Meta class" with a namespace
    interesting_members = [x for x in clsmembers if hasattr(x[1], 'Meta') and hasattr(x[1].Meta, 'namespace')]

    # Specifically we are interested in classes that are derived from "EntityInVersion", to find them, we exclude embedded child objects called "VersionedChild"
    entitiesinversion = [x for x in interesting_members if netex.VersionedChildStructure not in x[1].__mro__ and netex.EntityInVersionStructure in x[1].__mro__]

    # Obviously we want to have the VersionedChild too
    versionedchild = [x for x in interesting_members if netex.VersionedChildStructure in x[1].__mro__]

    # There is one particular container in NeTEx that should reflect almost the same our collection EntityInVersion namely the "GeneralFrame"
    general_frame_members = netex.GeneralFrameMembersRelStructure.__dataclass_fields__['choice'].metadata['choices']

    # The interesting part here is where the difference between the two lie.
    # geme = [x['type'].Meta.getattr('name', x['type'].__name__) for x in general_frame_members]
    # envi = [x[0] for x in entitiesinversion]
    # set(geme) - set(envi)

    if filter is not None:
        clean_element_names = [x[0] for x in entitiesinversion if x[0] in filter]
        interesting_element_names =  [get_element_name_with_ns(x[1]) for x in entitiesinversion if x[0] in filter]
        interesting_clazzes = [x[1] for x in entitiesinversion if x[0] in filter]
    else:
        clean_element_names = [x[0] for x in entitiesinversion if not x[0].endswith('Frame')]
        interesting_element_names =  [get_element_name_with_ns(x[1]) for x in entitiesinversion if not x[0].endswith('Frame')]
        interesting_clazzes = [x[1] for x in entitiesinversion if not x[0].endswith('Frame')]

    return clean_element_names, interesting_element_names, interesting_clazzes