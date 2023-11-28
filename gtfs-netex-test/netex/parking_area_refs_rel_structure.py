from dataclasses import dataclass, field
from typing import List
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure
from netex.parking_area_ref import ParkingAreaRef
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingAreaRefsRelStructure(OneToManyRelationshipStructure):
    """
    Type for a collection of one or more references to a PARKING AREA.
    """
    class Meta:
        name = "parkingAreaRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingParkingAreaRef",
                    "type": VehiclePoolingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingAreaRef",
                    "type": VehicleSharingParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingAreaRef",
                    "type": TaxiParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingAreaRef",
                    "type": ParkingAreaRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
