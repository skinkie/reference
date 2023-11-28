from dataclasses import dataclass, field
from typing import Optional
from netex.car_pooling_service_ref import CarPoolingServiceRef
from netex.chauffeured_vehicle_service_ref import ChauffeuredVehicleServiceRef
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.mobility_service_constraint_zone_ref import MobilityServiceConstraintZoneRef
from netex.online_service_ref import OnlineServiceRef
from netex.parking_component_refs_rel_structure import ParkingComponentRefsRelStructure
from netex.parking_ref import ParkingRef
from netex.taxi_service_ref import TaxiServiceRef
from netex.vehicle_refs_rel_structure import VehicleRefsRelStructure
from netex.vehicle_rental_service_ref import VehicleRentalServiceRef
from netex.vehicle_sharing_service_ref import VehicleSharingServiceRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PoolOfVehiclesVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for POOL OF VEHICLEs restricts id.

    :ivar choice:
    :ivar mobility_service_constraint_zone_ref:
    :ivar parking_ref:
    :ivar parking_components: Vehclie restrictions in Zone
    :ivar must_return_to_same_bay: Whether a VEICLE must be returned to
        same bay as it was was taken from.
    :ivar vehicles: VEHICLEs in POOL OF VEHICLEs.
    """
    class Meta:
        name = "PoolOfVehicles_VersionStructure"

    choice: Optional[object] = field(
        default=None,
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
    mobility_service_constraint_zone_ref: Optional[MobilityServiceConstraintZoneRef] = field(
        default=None,
        metadata={
            "name": "MobilityServiceConstraintZoneRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_ref: Optional[ParkingRef] = field(
        default=None,
        metadata={
            "name": "ParkingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parking_components: Optional[ParkingComponentRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "parkingComponents",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    must_return_to_same_bay: Optional[bool] = field(
        default=None,
        metadata={
            "name": "MustReturnToSameBay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicles: Optional[VehicleRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
