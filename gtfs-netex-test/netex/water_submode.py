from dataclasses import dataclass, field
from .water_submode_enumeration import WaterSubmodeEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class WaterSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: WaterSubmodeEnumeration = field(
        default=WaterSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
