from dataclasses import dataclass, field
from typing import List
from netex.fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareClasses:
    """
    List of FARE CLASSes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
