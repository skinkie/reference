from dataclasses import dataclass, field
from netex.taxi_submode_enumeration import TaxiSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiSubmode:
    """
    TPEG pti11 Taxi submodes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: TaxiSubmodeEnumeration = field(
        default=TaxiSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
