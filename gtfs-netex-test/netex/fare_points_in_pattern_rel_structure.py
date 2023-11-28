from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.fare_point_in_pattern import FarePointInPattern
from netex.fare_point_in_pattern_ref import FarePointInPatternRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FarePointsInPatternRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of FARE POINT IN JOURNEY PATTERNs.
    """
    class Meta:
        name = "farePointsInPattern_RelStructure"

    fare_point_in_pattern_ref_or_fare_point_in_pattern: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FarePointInPatternRef",
                    "type": FarePointInPatternRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FarePointInPattern",
                    "type": FarePointInPattern,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
