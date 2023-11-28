from dataclasses import dataclass, field
from typing import Optional
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.parking_area_refs_rel_structure import ParkingAreaRefsRelStructure
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.site_entrance_version_structure import SiteEntranceVersionStructure
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingEntranceForVehiclesVersionStructure(SiteEntranceVersionStructure):
    """
    Type for PARKING ENTRANCE.

    :ivar choice:
    :ivar areas: PARKING AREAs to which ENtrance gives access appky
        +v1.1.
    """
    class Meta:
        name = "ParkingEntranceForVehicles__VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    areas: Optional[ParkingAreaRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
