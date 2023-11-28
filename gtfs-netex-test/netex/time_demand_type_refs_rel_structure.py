from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.time_demand_type_ref import TimeDemandTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimeDemandTypeRefsRelStructure(OneToManyRelationshipStructure):
    """
    Data type for a collection of one or more references to a TIME DEMAND TYPE.
    """
    class Meta:
        name = "timeDemandTypeRefs_RelStructure"

    time_demand_type_ref: List[TimeDemandTypeRef] = field(
        default_factory=list,
        metadata={
            "name": "TimeDemandTypeRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
