from dataclasses import dataclass, field
from netex.limitation_status_enumeration import LimitationStatusEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VisualSignsAvailable:
    """
    Whether a PLACE has Visual signals available for the free access.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: LimitationStatusEnumeration = field(
        default=LimitationStatusEnumeration.UNKNOWN,
        metadata={
            "required": True,
        }
    )
