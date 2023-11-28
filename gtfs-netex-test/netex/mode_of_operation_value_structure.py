from dataclasses import dataclass, field
from typing import Optional
from netex.submodes_rel_structure import SubmodesRelStructure
from netex.type_of_mode_of_operation_ref import TypeOfModeOfOperationRef
from netex.type_of_value_version_structure import TypeOfValueVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ModeOfOperationValueStructure(TypeOfValueVersionStructure):
    """
    Type for a MODE OF OPERATION.

    :ivar type_of_mode_of_operation_ref:
    :ivar submodes: SUBMODEs associated with MODE OF OPERATION.
    """
    class Meta:
        name = "ModeOfOperation_ValueStructure"

    type_of_mode_of_operation_ref: Optional[TypeOfModeOfOperationRef] = field(
        default=None,
        metadata={
            "name": "TypeOfModeOfOperationRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    submodes: Optional[SubmodesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
