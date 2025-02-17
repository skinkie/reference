from dataclasses import dataclass, field

from .climate_control_enumeration import ClimateControlEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ClimateControlList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[ClimateControlEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
