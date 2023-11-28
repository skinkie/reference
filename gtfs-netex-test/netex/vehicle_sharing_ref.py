from dataclasses import dataclass
from netex.vehicle_sharing_mode_of_operation_ref_structure import VehicleSharingModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingRef(VehicleSharingModeOfOperationRefStructure):
    """Reference to a VEHICLE SHARING MODE OF OPERATION.

    +V1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
