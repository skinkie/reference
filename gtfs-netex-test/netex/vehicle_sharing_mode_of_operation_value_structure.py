from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_mode_of_operation_value_structure import AlternativeModeOfOperationValueStructure
from netex.vehicle_sharing_type_enumeration import VehicleSharingTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleSharingModeOfOperationValueStructure(AlternativeModeOfOperationValueStructure):
    """
    Type for a VEHICLE SHARING MODE OF OPERATION.

    :ivar vehicle_sharing_type: Allowed values for VEHICLE SHARING
        MODE.OF OPERATION.
    """
    class Meta:
        name = "VehicleSharingModeOfOperation_ValueStructure"

    vehicle_sharing_type: Optional[VehicleSharingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleSharingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
