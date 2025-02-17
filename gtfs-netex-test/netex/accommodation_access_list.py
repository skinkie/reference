from dataclasses import dataclass, field

from .accommodation_access_enumeration import AccommodationAccessEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccommodationAccessList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[AccommodationAccessEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
