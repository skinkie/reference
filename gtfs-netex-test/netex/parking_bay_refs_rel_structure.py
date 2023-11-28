from dataclasses import dataclass, field
from typing import List
from netex.monitored_vehicle_sharing_parking_bay_ref import MonitoredVehicleSharingParkingBayRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.parking_bay_ref import ParkingBayRef
from netex.vehicle_pooling_parking_bay_ref import VehiclePoolingParkingBayRef
from netex.vehicle_sharing_parking_bay_ref import VehicleSharingParkingBayRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingBayRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more a references to a PARKING BAY.
    """
    class Meta:
        name = "parkingBayRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingParkingBayRef",
                    "type": VehiclePoolingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "MonitoredVehicleSharingParkingBayRef",
                    "type": MonitoredVehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingBayRef",
                    "type": VehicleSharingParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingBayRef",
                    "type": ParkingBayRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
