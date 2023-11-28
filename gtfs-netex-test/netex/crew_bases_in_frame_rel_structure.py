from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.crew_base import CrewBase

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CrewBasesInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of CREW BASEs.
    """
    class Meta:
        name = "crewBasesInFrame_RelStructure"

    crew_base: List[CrewBase] = field(
        default_factory=list,
        metadata={
            "name": "CrewBase",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
