from dataclasses import dataclass
from netex.mode_of_operation_ref_structure import ModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PersonalModeOfOperationRefStructure(ModeOfOperationRefStructure):
    """
    Type for a reference to a PERSONAL MODE OF OPERATION.
    """
