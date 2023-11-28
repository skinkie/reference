from dataclasses import dataclass, field
from netex.accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccommodationAccess:
    """
    Classification of ACCOMMODATION ACCESS type -
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccommodationAccessEnumeration = field(
        metadata={
            "required": True,
        }
    )
