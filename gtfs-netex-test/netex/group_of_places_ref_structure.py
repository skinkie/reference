from dataclasses import dataclass

from .group_of_entities_ref_structure_1 import GroupOfEntitiesRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfPlacesRefStructure(GroupOfEntitiesRefStructure1):
    pass
