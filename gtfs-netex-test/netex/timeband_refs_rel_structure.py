from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.timeband_ref import TimebandRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimebandRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of TIMEBAND.
    """
    class Meta:
        name = "timebandRefs_RelStructure"

    timeband_ref: List[TimebandRef] = field(
        default_factory=list,
        metadata={
            "name": "TimebandRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
