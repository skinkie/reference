from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .common_vehicle_service_version_structure import CommonVehicleServiceVersionStructure
from .fleet_refs_rel_structure import FleetRefsRelStructure
from .vehicle_rental_ref import VehicleRentalRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleRentalServiceVersionStructure(CommonVehicleServiceVersionStructure):
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
        },
    )
    minimum_rental_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumRentalPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rental_policy_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "RentalPolicyUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fleets: Optional[FleetRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
