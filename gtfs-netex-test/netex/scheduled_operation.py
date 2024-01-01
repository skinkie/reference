from dataclasses import dataclass
from .scheduled_mode_of_operation_value_structure import (
    ScheduledModeOfOperationValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ScheduledOperation(ScheduledModeOfOperationValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
