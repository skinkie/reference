from dataclasses import dataclass

from .scheduled_mode_of_operation_ref_structure import ScheduledModeOfOperationRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ScheduledModeOfOperationRef(ScheduledModeOfOperationRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
