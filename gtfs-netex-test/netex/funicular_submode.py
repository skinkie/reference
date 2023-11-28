from dataclasses import dataclass, field
from netex.funicular_submode_enumeration import FunicularSubmodeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FunicularSubmode:
    """
    TPEG pti10 Funicular submodes.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: FunicularSubmodeEnumeration = field(
        default=FunicularSubmodeEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
