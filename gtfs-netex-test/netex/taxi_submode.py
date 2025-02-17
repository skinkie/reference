from dataclasses import dataclass, field

from .taxi_submode_enumeration import TaxiSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TaxiSubmode:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TaxiSubmodeEnumeration = field(
        default=TaxiSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
