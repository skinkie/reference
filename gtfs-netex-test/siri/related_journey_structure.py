from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .connecting_journey_ref_structure import ConnectingJourneyRefStructure
from .related_call_structure import RelatedCallStructure
from .related_journey_part_structure import RelatedJourneyPartStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RelatedJourneyStructure(ConnectingJourneyRefStructure):
    call_info_or_journey_parts: Optional[Union[RelatedCallStructure, "RelatedJourneyStructure.JourneyParts"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CallInfo",
                    "type": RelatedCallStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "JourneyParts",
                    "type": ForwardRef("RelatedJourneyStructure.JourneyParts"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )

    @dataclass(kw_only=True)
    class JourneyParts:
        journey_part_info: List[RelatedJourneyPartStructure] = field(
            default_factory=list,
            metadata={
                "name": "JourneyPartInfo",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
