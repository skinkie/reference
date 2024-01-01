from dataclasses import dataclass, field
from typing import List
from .safety_facility_enumeration import SafetyFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SafetyFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[SafetyFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
