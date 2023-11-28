from dataclasses import dataclass, field
from typing import Optional
from netex.conventional_mode_of_operation_value_structure import ConventionalModeOfOperationValueStructure
from netex.scheduled_operation_type_enumeration import ScheduledOperationTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledModeOfOperationValueStructure(ConventionalModeOfOperationValueStructure):
    """
    Type for a SCHEDULED  MODE OF OPERATION.

    :ivar scheduled_operation_type: Allowed values for SCHEDULED  MODE
        OF OPERATION.
    """
    class Meta:
        name = "ScheduledModeOfOperation_ValueStructure"

    scheduled_operation_type: Optional[ScheduledOperationTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ScheduledOperationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
