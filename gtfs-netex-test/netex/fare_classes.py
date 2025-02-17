from dataclasses import dataclass, field

from .fare_class_enumeration import FareClassEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareClasses:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[FareClassEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
