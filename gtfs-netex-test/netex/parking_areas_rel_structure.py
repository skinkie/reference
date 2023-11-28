from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.parking_area import ParkingArea
from netex.parking_area_ref import ParkingAreaRef
from netex.taxi_parking_area import TaxiParkingArea
from netex.taxi_parking_area_ref import TaxiParkingAreaRef
from netex.vehicle_pooling_parking_area import VehiclePoolingParkingArea
from netex.vehicle_pooling_parking_area_ref import VehiclePoolingParkingAreaRef
from netex.vehicle_sharing_parking_area import VehicleSharingParkingArea
from netex.vehicle_sharing_parking_area_ref import VehicleSharingParkingAreaRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ParkingAreasRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of PARKING AREAs.
    """
    class Meta:
        name = "parkingAreas_RelStructure"

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
                {
                    "name": "VehiclePoolingParkingArea",
                    "type": VehiclePoolingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingParkingArea",
                    "type": VehicleSharingParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiParkingArea",
                    "type": TaxiParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingArea",
                    "type": ParkingArea,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
