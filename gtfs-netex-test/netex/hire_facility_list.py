from dataclasses import dataclass, field
from typing import List
from .hire_facility_enumeration import HireFacilityEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HireFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[HireFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
