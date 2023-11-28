from dataclasses import dataclass, field
from netex.uic_rate_type_enumeration import UicRateTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class UicTrainRate:
    """Classification of UIC Rate Type FACILITY type - UIC 5163 Code list."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: UicRateTypeEnumeration = field(
        metadata={
            "required": True,
        }
    )
