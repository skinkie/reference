from dataclasses import dataclass
from netex.conventional_mode_of_operation_ref_structure import ConventionalModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledModeOfOperationRefStructure(ConventionalModeOfOperationRefStructure):
    """
    Type for a reference to a SCHEDULED MODE OF OPERATION.
    """
