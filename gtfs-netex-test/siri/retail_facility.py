from dataclasses import dataclass, field

from .retail_facility_enumeration import RetailFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RetailFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: RetailFacilityEnumeration = field(
        default=RetailFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
