from dataclasses import dataclass, field

from .sanitary_facility_enumeration import SanitaryFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SanitaryFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: SanitaryFacilityEnumeration = field(
        default=SanitaryFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
