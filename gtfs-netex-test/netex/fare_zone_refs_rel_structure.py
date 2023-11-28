from dataclasses import dataclass, field
from typing import List
from netex.fare_zone_ref import FareZoneRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareZoneRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of FARE ZONEs.
    """
    class Meta:
        name = "fareZoneRefs_RelStructure"

    fare_zone_ref: List[FareZoneRef] = field(
        default_factory=list,
        metadata={
            "name": "FareZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
