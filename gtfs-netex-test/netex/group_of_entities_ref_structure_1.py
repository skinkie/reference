from dataclasses import dataclass
from netex.group_of_entities_ref_structure_2 import GroupOfEntitiesRefStructure2

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfEntitiesRefStructure1(GroupOfEntitiesRefStructure2):
    """
    Extending Type for a reference to a GROUP OF ENTITies.
    """
    class Meta:
        name = "GroupOfEntitiesRefStructure"
