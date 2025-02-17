from dataclasses import dataclass

from .travel_specification_version_structure import TravelSpecificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TravelSpecification1(TravelSpecificationVersionStructure):
    class Meta:
        name = "TravelSpecification"
        namespace = "http://www.netex.org.uk/netex"
