from dataclasses import dataclass
from netex.money_service_ref_structure import MoneyServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MoneyServiceRef(MoneyServiceRefStructure):
    """
    Identifier of an MONEY SERVICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
