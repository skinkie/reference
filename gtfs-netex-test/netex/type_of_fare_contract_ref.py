from dataclasses import dataclass
from netex.type_of_fare_contract_ref_structure import TypeOfFareContractRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareContractRef(TypeOfFareContractRefStructure):
    """
    Reference to a TYPE OF FARE CONTRACT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
