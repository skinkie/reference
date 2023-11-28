from dataclasses import dataclass, field
from typing import List
from netex.car_pooling_service import CarPoolingService
from netex.chauffeured_vehicle_service import ChauffeuredVehicleService
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.online_service import OnlineService
from netex.taxi_service import TaxiService
from netex.vehicle_rental_service import VehicleRentalService
from netex.vehicle_sharing_service import VehicleSharingService

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MobilityServicesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of MOBILITY SERVICEs.
    """
    class Meta:
        name = "mobilityServices_RelStructure"

    choice: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "OnlineService",
                    "type": OnlineService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalService",
                    "type": VehicleRentalService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingService",
                    "type": VehicleSharingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ChauffeuredVehicleService",
                    "type": ChauffeuredVehicleService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarPoolingService",
                    "type": CarPoolingService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TaxiService",
                    "type": TaxiService,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
