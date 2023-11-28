from dataclasses import dataclass, field
from netex.alternative_mode_of_operation_value_structure import AlternativeModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AlternativeModeOfOperation(AlternativeModeOfOperationValueStructure):
    """Any publicly advertised mode of operation different from the CONVENTIONAL
    MODE OF OPERATION, for example: VEHICLE SHARING, VEHICLE RENTAL, VEHICLE
    POOLING.

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
