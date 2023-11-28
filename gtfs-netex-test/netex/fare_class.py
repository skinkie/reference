from dataclasses import dataclass, field
from netex.fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareClass:
    """
    Classification of FARE CLASSes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FareClassEnumeration = field(
        default=FareClassEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
