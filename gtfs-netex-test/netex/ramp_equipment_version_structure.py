from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.access_equipment_version_structure import AccessEquipmentVersionStructure
from netex.gradient_enumeration import GradientEnumeration
from netex.handrail_enumeration import HandrailEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RampEquipmentVersionStructure(AccessEquipmentVersionStructure):
    """
    Type for a RAMP EQUIPMENT.

    :ivar length: Length of ramp in metres.
    :ivar gradient: Gradient of ramp in degrees.
    :ivar gradient_type: Gradient of ramp fixed values.+v1.1
    :ivar pedestal: Whether ramp is on a pedestal.
    :ivar handrail_height: Height of handrail.
    :ivar handrail_type: Type of handrail.
    :ivar tactile_guidance_strips: Whether ramp has tactile guidance
        strips.
    :ivar visual_guidance_bands: Whether ramp has visual guidance bands
        or guidance strips.
    :ivar temporary: Whether ramp is temporary or permanent.
    :ivar suitable_for_cycles: Whether equipment is suitable for cycles.
    """
    class Meta:
        name = "RampEquipment_VersionStructure"

    length: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Length",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gradient: Optional[int] = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gradient_type: Optional[GradientEnumeration] = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    pedestal: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Pedestal",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    handrail_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "HandrailHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    handrail_type: Optional[HandrailEnumeration] = field(
        default=None,
        metadata={
            "name": "HandrailType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_guidance_strips: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGuidanceStrips",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    visual_guidance_bands: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VisualGuidanceBands",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    temporary: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Temporary",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    suitable_for_cycles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "SuitableForCycles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
