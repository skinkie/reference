from dataclasses import dataclass

from .vehicle_sharing_place_assignment_version_structure import VehicleSharingPlaceAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleSharingPlaceAssignment(VehicleSharingPlaceAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
