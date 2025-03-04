from dataclasses import dataclass

from .vehicle_pooling_mode_of_operation_ref_structure import VehiclePoolingModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehiclePoolingRef(VehiclePoolingModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
