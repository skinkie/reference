from dataclasses import dataclass, field

from .assistance_facility_enumeration import AssistanceFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AssistanceFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: AssistanceFacilityEnumeration = field(
        default=AssistanceFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
