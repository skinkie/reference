from dataclasses import dataclass

from .money_service_ref_structure import MoneyServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class MoneyServiceRef(MoneyServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
