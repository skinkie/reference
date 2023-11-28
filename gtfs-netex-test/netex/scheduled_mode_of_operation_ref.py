from dataclasses import dataclass
from netex.scheduled_mode_of_operation_ref_structure import ScheduledModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ScheduledModeOfOperationRef(ScheduledModeOfOperationRefStructure):
    """Reference to a SCHEDULED MODE OF OPERATION.

    +V1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
