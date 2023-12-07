from mro_attributes import unembed, list_attributes
from netex.alternative_texts_rel_structure import AlternativeTextsRelStructure, AlternativeText

import netex
import inspect
members = inspect.getmembers(netex)
class_list = {x[0]:x[1] for x in members}

# output = list_attributes(AlternativeTextsRelStructure, class_list, set([]))

# output = list_attributes(netex.DataSource, class_list)
# output = list_attributes(netex.ScheduledStopPoint, class_list, set([]))
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

for x in versionedchild:
    list_attributes(x[1], class_list, set([]))

# print(output)