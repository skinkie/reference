from dataclasses import dataclass, field
from typing import Union

from .containment_aggregation_structure import ContainmentAggregationStructure
from .journey_part import JourneyPart
from .journey_part_ref import JourneyPartRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class JourneyPartsRelStructure(ContainmentAggregationStructure):
    class Meta:
        name = "journeyParts_RelStructure"

    journey_part_ref_or_journey_part: list[Union[JourneyPartRef, JourneyPart]] = field(
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
        },
    )
