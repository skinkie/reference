from dataclasses import dataclass
from netex.offered_travel_specification_ref_structure import OfferedTravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OfferedTravelSpecificationRef(OfferedTravelSpecificationRefStructure):
    """
    Reference to an OFFERED TRAVEL SPECIFICATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
