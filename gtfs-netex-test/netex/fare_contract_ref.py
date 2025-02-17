from dataclasses import dataclass

from .fare_contract_ref_structure import FareContractRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class FareContractRef(FareContractRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
