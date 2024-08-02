from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .journey_relation_type_enumeration import JourneyRelationTypeEnumeration
from .related_call_structure import RelatedCallStructure
from .related_journey import RelatedJourney
from .related_journey_part_structure import RelatedJourneyPartStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class JourneyRelationStructure:
    journey_relation_type: JourneyRelationTypeEnumeration = field(
        metadata={
            "name": "JourneyRelationType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    call_info_or_journey_parts: Optional[Union[RelatedCallStructure, "JourneyRelationStructure.JourneyParts"]] = field(
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
                    "type": ForwardRef("JourneyRelationStructure.JourneyParts"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    related_journey: List[RelatedJourney] = field(
        default_factory=list,
        metadata={
            "name": "RelatedJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "min_occurs": 1,
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
