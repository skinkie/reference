from dataclasses import dataclass
from netex.taxi_service_place_assignment_ref_structure import TaxiServicePlaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TaxiServicePlaceAssignmentRef(TaxiServicePlaceAssignmentRefStructure):
    """Reference to a TAXI SERVICE PLACE ASSIGNMENT.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
