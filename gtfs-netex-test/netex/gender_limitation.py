from dataclasses import dataclass, field
from netex.gender_limitation_enumeration import GenderLimitationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GenderLimitation:
    """
    Classification GENDER LIMITATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: GenderLimitationEnumeration = field(
        metadata={
            "required": True,
        }
    )
