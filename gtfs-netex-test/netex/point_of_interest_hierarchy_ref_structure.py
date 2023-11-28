from dataclasses import dataclass
from netex.group_of_entities_ref_structure_1 import GroupOfEntitiesRefStructure1

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestHierarchyRefStructure(GroupOfEntitiesRefStructure1):
    """
    Type for a POINT OF INTEREST CLASSIFICATION HIERARCHY.
    """
