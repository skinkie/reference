from dataclasses import dataclass, field
from typing import Optional
from netex.conventional_mode_of_operation_value_structure import ConventionalModeOfOperationValueStructure
from netex.flexible_operation_type_enumeration import FlexibleOperationTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FlexibleModeOfOperationValueStructure(ConventionalModeOfOperationValueStructure):
    """
    Type for a FLEXIBLE MODE OF OPERATION.

    :ivar flexible_operation_type: Allowed values for FLEXIBLE  MODE OF
        OPERATION.
    """
    class Meta:
        name = "FlexibleModeOfOperation_ValueStructure"

    flexible_operation_type: Optional[FlexibleOperationTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleOperationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
