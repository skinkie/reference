from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from .extensions_1 import Extensions1
from .link_projection_structure import LinkProjectionStructure
from .offset_structure import OffsetStructure
from .quay_ref_structure_2 import QuayRefStructure2
from .section_ref_structure import SectionRefStructure
from .stop_place_ref_structure import StopPlaceRefStructure
from .stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedSectionStructure:
    section_ref_or_indirect_section_ref: Optional[Union[SectionRefStructure, "AffectedSectionStructure.IndirectSectionRef"]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SectionRef",
                    "type": SectionRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "IndirectSectionRef",
                    "type": ForwardRef("AffectedSectionStructure.IndirectSectionRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class IndirectSectionRef:
        first_stop_point_ref_or_first_stop_place_ref_or_first_quay_ref: Optional[Union[StopPointRefStructure, StopPlaceRefStructure, QuayRefStructure2]] = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "FirstStopPointRef",
                        "type": StopPointRefStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "FirstStopPlaceRef",
                        "type": StopPlaceRefStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "FirstQuayRef",
                        "type": QuayRefStructure2,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
        intermediate_stop_point_ref_or_intermediate_stop_place_ref_or_intermediate_quay_ref: List[Union[StopPointRefStructure, StopPlaceRefStructure, QuayRefStructure2]] = field(
            default_factory=list,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "IntermediateStopPointRef",
                        "type": StopPointRefStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "IntermediateStopPlaceRef",
                        "type": StopPlaceRefStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "IntermediateQuayRef",
                        "type": QuayRefStructure2,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
        last_stop_point_ref_or_last_stop_place_ref_or_last_quay_ref: Optional[Union[StopPointRefStructure, StopPlaceRefStructure, QuayRefStructure2]] = field(
            default=None,
            metadata={
                "type": "Elements",
                "choices": (
                    {
                        "name": "LastStopPointRef",
                        "type": StopPointRefStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "LastStopPlaceRef",
                        "type": StopPlaceRefStructure,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                    {
                        "name": "LastQuayRef",
                        "type": QuayRefStructure2,
                        "namespace": "http://www.siri.org.uk/siri",
                    },
                ),
            },
        )
