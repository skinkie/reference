from dataclasses import dataclass, field
from typing import List
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareScheduledStopPointRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a list of FARE SCHEDULED STOP POINTs.
    """
    class Meta:
        name = "fareScheduledStopPointRefs_RelStructure"

    fare_scheduled_stop_point_ref: List[FareScheduledStopPointRef] = field(
        default_factory=list,
        metadata={
            "name": "FareScheduledStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
