from dataclasses import dataclass
from .vehicle_sharing_mode_of_operation_ref_structure import (
    VehicleSharingModeOfOperationRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleSharingRef(VehicleSharingModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
