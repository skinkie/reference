from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional

from .entity_in_version_structure import VersionedChildStructure
from .handrail_enumeration import HandrailEnumeration
from .stair_end_structure import StairEndStructure
from .stair_ramp_enumeration import StairRampEnumeration
from .step_condition_enumeration import StepConditionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class StairFlightVersionedChildStructure(VersionedChildStructure):
    class Meta:
        name = "StairFlight_VersionedChildStructure"

    depth: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Depth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StepHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "StepLength",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_colour_contrast: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StepColourContrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    step_condition: Optional[StepConditionEnumeration] = field(
        default=None,
        metadata={
            "name": "StepCondition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_type: Optional[HandrailEnumeration] = field(
        default=None,
        metadata={
            "name": "HandrailType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lower_handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "LowerHandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_writing: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileWriting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    stair_ramp: Optional[StairRampEnumeration] = field(
        default=None,
        metadata={
            "name": "StairRamp",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    top_end: Optional[StairEndStructure] = field(
        default=None,
        metadata={
            "name": "TopEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    bottom_end: Optional[StairEndStructure] = field(
        default=None,
        metadata={
            "name": "BottomEnd",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    continuous_handrail: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ContinuousHandrail",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
