from dataclasses import dataclass, field
from netex.money_facility_enumeration import MoneyFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MoneyFacility:
    """
    Classification of MONEY FACILITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: MoneyFacilityEnumeration = field(
        metadata={
            "required": True,
        }
    )
