from dataclasses import dataclass, field
from typing import List
from netex.accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccommodationAccessList:
    """
    List of ACCOMMODATION ACCESS.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: List[AccommodationAccessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        }
    )
