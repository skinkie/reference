from dataclasses import dataclass, field

from .accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccommodationAccess:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: AccommodationAccessEnumeration = field(
        metadata={
            "required": True,
        }
    )
