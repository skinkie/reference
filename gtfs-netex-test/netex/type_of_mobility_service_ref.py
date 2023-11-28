from dataclasses import dataclass
from netex.type_of_mobility_service_ref_structure import TypeOfMobilityServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TypeOfMobilityServiceRef(TypeOfMobilityServiceRefStructure):
    """Reference to a TYPE OF MobilityService.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
