from dataclasses import dataclass
from netex.vehicle_sharing_service_ref_structure import VehicleSharingServiceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingServiceRef(VehicleSharingServiceRefStructure):
    """Identifier of an VEHICLE SHARING SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
