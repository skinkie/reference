from dataclasses import dataclass

from .vehicle_service_place_assignment_ref_structure import VehicleServicePlaceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleSharingPlaceAssignmentRefStructure(VehicleServicePlaceAssignmentRefStructure):
    pass
