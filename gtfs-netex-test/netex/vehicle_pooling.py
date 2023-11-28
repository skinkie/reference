from dataclasses import dataclass, field
from netex.vehicle_pooling_mode_of_operation_value_structure import VehiclePoolingModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehiclePooling(VehiclePoolingModeOfOperationValueStructure):
    """An ALTERNATIVE MODE OF OPERATION of a privately-owned vehicle consisting in
    sharing the vehicle for a trip between the driver who is at the same time
    performing a trip and at least another traveller.

    +v1.2.2

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
