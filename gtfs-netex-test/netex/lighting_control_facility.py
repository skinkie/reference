from dataclasses import dataclass, field

from .lighting_control_facility_enumeration import LightingControlFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class LightingControlFacility:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LightingControlFacilityEnumeration = field(
        default=LightingControlFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
