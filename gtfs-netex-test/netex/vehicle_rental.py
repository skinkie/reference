from dataclasses import dataclass, field
from netex.vehicle_rental_mode_of_operation_value_structure import VehicleRentalModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleRental(VehicleRentalModeOfOperationValueStructure):
    """An ALTERNATIVE MODE OF OPERATION of a vehicle, part of a FLEET (in general
    privately owned), available for use for a certain period of time and fee, with
    the constraint to bring it back at specified agencies.

    +v1.2.2

    :ivar id: Identifier of VEHICLE RENTAL MODE OF OPERATION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
