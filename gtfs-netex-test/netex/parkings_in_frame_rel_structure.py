from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.parking import Parking

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingsInFrameRelStructure(ContainmentAggregationStructure):
    """
    Type for containment in frame of PARKING.

    :ivar parking: A designated path between two PLACEs. May include an
        Ordered sequence of references to PATH LINKS.
    """
    class Meta:
        name = "parkingsInFrame_RelStructure"

    parking: List[Parking] = field(
        default_factory=list,
        metadata={
            "name": "Parking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "min_occurs": 1,
        }
    )
