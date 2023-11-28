from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.journey_part import JourneyPart
from netex.journey_part_ref import JourneyPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of JOURNEY PARTs.
    """
    class Meta:
        name = "journeyParts_RelStructure"

    journey_part_ref_or_journey_part: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "JourneyPartRef",
                    "type": JourneyPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "JourneyPart",
                    "type": JourneyPart,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
