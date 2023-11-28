from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_mode_of_operation_value_structure import AlternativeModeOfOperationValueStructure
from netex.vehicle_pooling_type_enumeration import VehiclePoolingTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePoolingModeOfOperationValueStructure(AlternativeModeOfOperationValueStructure):
    """
    Type for a VEHICLE POOLING MODE OF OPERATION.

    :ivar vehicle_pooling_type: Allowed values for VEHICLE POOLING
        MODE.OF OPERATION.
    """
    class Meta:
        name = "VehiclePoolingModeOfOperation_ValueStructure"

    vehicle_pooling_type: Optional[VehiclePoolingTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VehiclePoolingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
