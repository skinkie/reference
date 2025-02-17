from dataclasses import dataclass

from .requested_travel_specification_ref_structure import RequestedTravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RequestedTravelSpecificationRef(RequestedTravelSpecificationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
