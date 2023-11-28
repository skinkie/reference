from dataclasses import dataclass
from netex.travel_specification_version_structure import TravelSpecificationVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OfferedTravelSpecificationVersionStructure(TravelSpecificationVersionStructure):
    """
    Type for OFFERED TRAVEL SPECIFICATION.
    """
    class Meta:
        name = "OfferedTravelSpecification_VersionStructure"
