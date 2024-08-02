from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .aimed_flexible_area import AimedFlexibleArea
from .aimed_flexible_area_ref import AimedFlexibleAreaRef
from .aimed_location_name import AimedLocationName
from .boarding_position_ref_structure_2 import BoardingPositionRefStructure2
from .flexible_area_ref_structure import FlexibleAreaRefStructure
from .flexible_area_structure import FlexibleAreaStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .quay_ref_structure_2 import QuayRefStructure2
from .quay_type import QuayType

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopAssignmentStructure:
    choice: List[
        Union[
            "StopAssignmentStructure.AimedQuayRef",
            "StopAssignmentStructure.AimedQuayName",
            "StopAssignmentStructure.ExpectedQuayRef",
            "StopAssignmentStructure.ExpectedQuayName",
            "StopAssignmentStructure.ActualQuayRef",
            "StopAssignmentStructure.ActualQuayName",
            QuayType,
            "StopAssignmentStructure.AimedBoardingPositionRef",
            "StopAssignmentStructure.AimedBoardingPositionName",
            "StopAssignmentStructure.ExpectedBoardingPositionRef",
            "StopAssignmentStructure.ExpectedBoardingPositionName",
            "StopAssignmentStructure.ActualBoardingPositionRef",
            "StopAssignmentStructure.ActualBoardingPositionName",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AimedQuayRef",
                    "type": ForwardRef("StopAssignmentStructure.AimedQuayRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedQuayName",
                    "type": ForwardRef("StopAssignmentStructure.AimedQuayName"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ExpectedQuayRef",
                    "type": ForwardRef("StopAssignmentStructure.ExpectedQuayRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ExpectedQuayName",
                    "type": ForwardRef("StopAssignmentStructure.ExpectedQuayName"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ActualQuayRef",
                    "type": ForwardRef("StopAssignmentStructure.ActualQuayRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ActualQuayName",
                    "type": ForwardRef("StopAssignmentStructure.ActualQuayName"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "QuayType",
                    "type": QuayType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedBoardingPositionRef",
                    "type": ForwardRef("StopAssignmentStructure.AimedBoardingPositionRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedBoardingPositionName",
                    "type": ForwardRef("StopAssignmentStructure.AimedBoardingPositionName"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ExpectedBoardingPositionRef",
                    "type": ForwardRef("StopAssignmentStructure.ExpectedBoardingPositionRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ExpectedBoardingPositionName",
                    "type": ForwardRef("StopAssignmentStructure.ExpectedBoardingPositionName"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ActualBoardingPositionRef",
                    "type": ForwardRef("StopAssignmentStructure.ActualBoardingPositionRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ActualBoardingPositionName",
                    "type": ForwardRef("StopAssignmentStructure.ActualBoardingPositionName"),
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
    expected_flexible_area: Optional[FlexibleAreaStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedFlexibleArea",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_flexible_area_ref: Optional[FlexibleAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ExpectedFlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_location_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ExpectedLocationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_flexible_area: Optional[FlexibleAreaStructure] = field(
        default=None,
        metadata={
            "name": "ActualFlexibleArea",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_flexible_area_ref: Optional[FlexibleAreaRefStructure] = field(
        default=None,
        metadata={
            "name": "ActualFlexibleAreaRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    actual_location_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ActualLocationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class AimedQuayRef(QuayRefStructure2):
        pass

    @dataclass(kw_only=True)
    class AimedQuayName(NaturalLanguageStringStructure):
        pass

    @dataclass(kw_only=True)
    class ExpectedQuayRef(QuayRefStructure2):
        pass

    @dataclass(kw_only=True)
    class ExpectedQuayName(NaturalLanguageStringStructure):
        pass

    @dataclass(kw_only=True)
    class ActualQuayRef(QuayRefStructure2):
        pass

    @dataclass(kw_only=True)
    class ActualQuayName(NaturalLanguageStringStructure):
        pass

    @dataclass(kw_only=True)
    class AimedBoardingPositionRef(BoardingPositionRefStructure2):
        pass

    @dataclass(kw_only=True)
    class AimedBoardingPositionName(NaturalLanguageStringStructure):
        pass

    @dataclass(kw_only=True)
    class ExpectedBoardingPositionRef(BoardingPositionRefStructure2):
        pass

    @dataclass(kw_only=True)
    class ExpectedBoardingPositionName(NaturalLanguageStringStructure):
        pass

    @dataclass(kw_only=True)
    class ActualBoardingPositionRef(BoardingPositionRefStructure2):
        pass

    @dataclass(kw_only=True)
    class ActualBoardingPositionName(NaturalLanguageStringStructure):
        pass
