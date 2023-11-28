from dataclasses import dataclass, field
from netex.type_of_fare_contract_version_structure import TypeOfFareContractVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareContract(TypeOfFareContractVersionStructure):
    """
    A classification of FARE CONTRACT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
