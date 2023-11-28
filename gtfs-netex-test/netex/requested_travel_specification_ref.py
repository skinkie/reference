from dataclasses import dataclass
from netex.requested_travel_specification_ref_structure import RequestedTravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RequestedTravelSpecificationRef(RequestedTravelSpecificationRefStructure):
    """
    Reference to a REQUESTED TRAVEL SPECIFICATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
