from dataclasses import dataclass, field
from netex.bus_submode_enumeration import BusSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BusSubmode:
    """
    TPEG pti05 Bus submodes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: BusSubmodeEnumeration = field(
        default=BusSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
