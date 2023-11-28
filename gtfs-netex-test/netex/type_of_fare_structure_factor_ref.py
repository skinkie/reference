from dataclasses import dataclass
from netex.type_of_fare_structure_factor_ref_structure import TypeOfFareStructureFactorRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareStructureFactorRef(TypeOfFareStructureFactorRefStructure):
    """
    Reference to a TYPE OF FARE STRUCTURE FACTOR.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
