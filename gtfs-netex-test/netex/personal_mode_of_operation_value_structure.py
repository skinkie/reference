from dataclasses import dataclass, field
from typing import Optional
from netex.mode_of_operation_value_structure import ModeOfOperationValueStructure
from netex.personal_operation_type_enumeration import PersonalOperationTypeEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PersonalModeOfOperationValueStructure(ModeOfOperationValueStructure):
    """
    Type for a PERSONAL MODE OF OPERATION.

    :ivar personal_operation_type: Allowed values for PERSONAL MODE OF
        OPERATION.
    """
    class Meta:
        name = "PersonalModeOfOperation_ValueStructure"

    personal_operation_type: Optional[PersonalOperationTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PersonalOperationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
