from dataclasses import dataclass, field
from typing import List

from .climate_control_enumeration import ClimateControlEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClimateControlList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[ClimateControlEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
