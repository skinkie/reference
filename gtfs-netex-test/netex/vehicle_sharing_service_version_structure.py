from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.common_vehicle_service_version_structure import CommonVehicleServiceVersionStructure
from netex.fleet_refs_rel_structure import FleetRefsRelStructure
from netex.vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingServiceVersionStructure(CommonVehicleServiceVersionStructure):
    """
    Type for VEHICLE SHARING SERVICE.

    :ivar vehicle_sharing_ref:
    :ivar sharing_policy_url: URL for info on Sharing policy.
    :ivar minimum_sharing_period: Minmum time period for sharing.
    :ivar maximum_sharing_period: Maximum time period for sharing.
    :ivar floating_vehicles: Whether vehicles are floating of issued
        from fixed stations.
    :ivar fleets: FLEETs used by service
    """
    class Meta:
        name = "VehicleSharingService_VersionStructure"

    vehicle_sharing_ref: VehicleSharingRef = field(
        metadata={
            "name": "VehicleSharingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    sharing_policy_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "SharingPolicyUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_sharing_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumSharingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_sharing_period: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumSharingPeriod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    floating_vehicles: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FloatingVehicles",
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
