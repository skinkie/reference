from dataclasses import dataclass, field
from typing import Optional
from netex.common_vehicle_service_version_structure import CommonVehicleServiceVersionStructure
from netex.vehicle_pooling_ref import VehiclePoolingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingServiceVersionStructure(CommonVehicleServiceVersionStructure):
    """
    Type for VEHICLE POOLING SERVICE.

    :ivar vehicle_pooling_ref:
    :ivar pooling_policy_url: URL for info on Pooling policy.
    """
    class Meta:
        name = "VehiclePoolingService_VersionStructure"

    vehicle_pooling_ref: VehiclePoolingRef = field(
        metadata={
            "name": "VehiclePoolingRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    pooling_policy_url: Optional[str] = field(
        default=None,
        metadata={
            "name": "PoolingPolicyUrl",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
