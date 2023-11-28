from dataclasses import dataclass, field
from netex.direction_type_enumeration import DirectionTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DirectionType:
    """A Direction of a ROUTE.

    One of a restricted set of values. Default is "Outbound"
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: DirectionTypeEnumeration = field(
        default=DirectionTypeEnumeration.OUTBOUND,
        metadata={
            "required": True,
        }
    )
