from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.type_of_zone_ref import TypeOfZoneRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfZoneRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TYPE OF ZONEs.
    """
    class Meta:
        name = "typeOfZoneRefs_RelStructure"

    type_of_zone_ref: List[TypeOfZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "TypeOfZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
