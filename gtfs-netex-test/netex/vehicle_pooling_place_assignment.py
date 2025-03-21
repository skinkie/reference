from dataclasses import dataclass

from .vehicle_pooling_place_assignment_version_structure import VehiclePoolingPlaceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingPlaceAssignment(VehiclePoolingPlaceAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
