from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_mode_of_operation_value_structure import AlternativeModeOfOperationValueStructure
from netex.vehicle_rental_type_enumeration import VehicleRentalTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRentalModeOfOperationValueStructure(AlternativeModeOfOperationValueStructure):
    """
    Type for a VEHICLE RENTAL MODE OF OPERATION.

    :ivar vehicle_rental_type: Allowed values for VEHICLE RENTAL MODE.OF
        OPERATION.
    """
    class Meta:
        name = "VehicleRentalModeOfOperation_ValueStructure"

    vehicle_rental_type: Optional[VehicleRentalTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "VehicleRentalType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
