from dataclasses import dataclass, field

from .hire_facility_enumeration import HireFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class HireFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: HireFacilityEnumeration = field(
        default=HireFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
