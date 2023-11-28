from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.common_vehicle_service_version_structure import CommonVehicleServiceVersionStructure
from netex.fleet_refs_rel_structure import FleetRefsRelStructure
from netex.vehicle_rental_ref import VehicleRentalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRentalServiceVersionStructure(CommonVehicleServiceVersionStructure):
    """
    Type for VEHICLE RENTAL SERVICE.

    :ivar vehicle_rental_ref:
    :ivar maximum_rental_period: Maximum time period for rental;
    :ivar minimum_rental_period: Minmum time period for rental;
    :ivar rental_policy_url: Rental policy URL.
    :ivar fleets: fleets used by service
    """
    class Meta:
        name = "VehicleRentalService_VersionStructure"

    vehicle_rental_ref: VehicleRentalRef = field(
        metadata={
            "name": "VehicleRentalRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    maximum_rental_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumRentalPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_rental_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumRentalPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    rental_policy_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "RentalPolicyUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fleets: Optional[FleetRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
