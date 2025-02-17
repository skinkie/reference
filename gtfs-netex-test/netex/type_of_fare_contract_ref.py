from dataclasses import dataclass

from .type_of_fare_contract_ref_structure import TypeOfFareContractRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TypeOfFareContractRef(TypeOfFareContractRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
