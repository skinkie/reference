from dataclasses import dataclass
from netex.travel_specification_ref_structure import TravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelSpecificationRef(TravelSpecificationRefStructure):
    """
    Reference to a TRAVEL SPECIFICATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
