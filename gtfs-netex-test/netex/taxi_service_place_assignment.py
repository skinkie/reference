from dataclasses import dataclass

from .taxi_service_place_assignment_version_structure import TaxiServicePlaceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TaxiServicePlaceAssignment(TaxiServicePlaceAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
