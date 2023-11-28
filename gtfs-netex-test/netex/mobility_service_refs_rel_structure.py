from dataclasses import dataclass, field
from typing import List
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.online_service_ref import OnlineServiceRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServiceRefsRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of refernces to MOBILITY SERVICEs.
    """
    class Meta:
        name = "mobilityServiceRefs_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineServiceRef",
                    "type": OnlineServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalServiceRef",
                    "type": VehicleRentalServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingServiceRef",
                    "type": VehicleSharingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleServiceRef",
                    "type": ChauffeuredVehicleServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiServiceRef",
                    "type": TaxiServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingServiceRef",
                    "type": CarPoolingServiceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
