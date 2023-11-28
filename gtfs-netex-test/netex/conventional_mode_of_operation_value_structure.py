from dataclasses import dataclass
from netex.mode_of_operation_value_structure import ModeOfOperationValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ConventionalModeOfOperationValueStructure(ModeOfOperationValueStructure):
    """
    Type for a CONVENTIONAL MODE OF OPERATION.
    """
    class Meta:
        name = "ConventionalModeOfOperation_ValueStructure"
