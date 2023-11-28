from dataclasses import dataclass
from netex.vehicle_pooling_mode_of_operation_ref_structure import VehiclePoolingModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingRef(VehiclePoolingModeOfOperationRefStructure):
    """Reference to a VEHICLE POOLING MODE OF OPERATION.

    +V1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
