from dataclasses import dataclass, field
from typing import Optional

from .conventional_mode_of_operation_value_structure import ConventionalModeOfOperationValueStructure
from .flexible_operation_type_enumeration import FlexibleOperationTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleModeOfOperationValueStructure(ConventionalModeOfOperationValueStructure):
    class Meta:
        name = "FlexibleModeOfOperation_ValueStructure"

    flexible_operation_type: Optional[FlexibleOperationTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlexibleOperationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
