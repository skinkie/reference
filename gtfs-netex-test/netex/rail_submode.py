from dataclasses import dataclass, field
from netex.rail_submode_enumeration import RailSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RailSubmode:
    """TPEG pti02 Rail submodes loc13.

    See also See ERA B.4.7009 - Name: Item description code.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RailSubmodeEnumeration = field(
        default=RailSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
