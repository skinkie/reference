from dataclasses import dataclass
from netex.type_of_congestion_ref_structure import TypeOfCongestionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfCongestionRef(TypeOfCongestionRefStructure):
    """
    Reference to a TYPE OF CONGESTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
