from dataclasses import dataclass
from .dynamic_stop_assignment_ref_structure import (
    DynamicStopAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DynamicStopAssignmentRef(DynamicStopAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
