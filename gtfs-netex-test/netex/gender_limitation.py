from dataclasses import dataclass, field
from .gender_limitation_enumeration import GenderLimitationEnumeration


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenderLimitation:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: GenderLimitationEnumeration = field(
        metadata={
            "required": True,
        }
    )
