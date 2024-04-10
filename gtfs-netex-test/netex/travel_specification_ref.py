from dataclasses import dataclass

from .travel_specification_ref_structure import TravelSpecificationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TravelSpecificationRef(TravelSpecificationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
