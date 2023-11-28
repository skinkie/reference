from dataclasses import dataclass
from netex.travel_specification_ref_structure import TravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RequestedTravelSpecificationRefStructure(TravelSpecificationRefStructure):
    """
    Type for Reference to a REQUESTED TRAVEL SPECIFICATION.
    """
