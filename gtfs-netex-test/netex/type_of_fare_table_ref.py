from dataclasses import dataclass
from netex.type_of_fare_table_ref_structure import TypeOfFareTableRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfFareTableRef(TypeOfFareTableRefStructure):
    """
    Reference to a TYPE OF FARE TABLE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
