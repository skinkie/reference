from dataclasses import dataclass, field
from netex.scheduled_mode_of_operation_value_structure import ScheduledModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledOperation(ScheduledModeOfOperationValueStructure):
    """The operation of a transportation using any kind of vehicle with a
    predefined time table.

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
