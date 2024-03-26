from dataclasses import dataclass, field

from .climate_control_enumeration import ClimateControlEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ClimateControl:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: ClimateControlEnumeration = field(
        metadata={
            "required": True,
        }
    )
