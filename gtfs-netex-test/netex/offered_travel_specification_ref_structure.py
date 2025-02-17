from dataclasses import dataclass

from .travel_specification_ref_structure import TravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OfferedTravelSpecificationRefStructure(TravelSpecificationRefStructure):
    pass
