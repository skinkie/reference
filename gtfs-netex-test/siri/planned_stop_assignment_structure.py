from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .aimed_flexible_area import AimedFlexibleArea
from .aimed_flexible_area_ref import AimedFlexibleAreaRef
from .aimed_location_name import AimedLocationName
from .boarding_position_ref_structure_2 import BoardingPositionRefStructure2
from .natural_language_string_structure import NaturalLanguageStringStructure
from .quay_ref_structure_2 import QuayRefStructure2
from .quay_type import QuayType

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PlannedStopAssignmentStructure:
    aimed_quay_ref_or_aimed_quay_name_or_quay_type_or_aimed_boarding_position_ref_or_aimed_boarding_position_name: List[Union[QuayRefStructure2, "PlannedStopAssignmentStructure.AimedQuayName", QuayType, BoardingPositionRefStructure2, "PlannedStopAssignmentStructure.AimedBoardingPositionName"]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AimedQuayRef",
                    "type": QuayRefStructure2,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedQuayName",
                    "type": ForwardRef("PlannedStopAssignmentStructure.AimedQuayName"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "QuayType",
                    "type": QuayType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedBoardingPositionRef",
                    "type": BoardingPositionRefStructure2,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedBoardingPositionName",
                    "type": ForwardRef("PlannedStopAssignmentStructure.AimedBoardingPositionName"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    aimed_flexible_area: Optional[AimedFlexibleArea] = field(
        default=None,
        metadata={
            "name": "AimedFlexibleArea",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_flexible_area_ref: Optional[AimedFlexibleAreaRef] = field(
        default=None,
        metadata={
            "name": "AimedFlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_location_name: List[AimedLocationName] = field(
        default_factory=list,
        metadata={
            "name": "AimedLocationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class AimedQuayName(NaturalLanguageStringStructure):
        pass

    @dataclass(kw_only=True)
    class AimedBoardingPositionName(NaturalLanguageStringStructure):
        pass
