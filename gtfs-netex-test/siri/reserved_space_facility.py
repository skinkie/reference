from dataclasses import dataclass, field

from .reserved_space_facility_enumeration import ReservedSpaceFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ReservedSpaceFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ReservedSpaceFacilityEnumeration = field(
        default=ReservedSpaceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
