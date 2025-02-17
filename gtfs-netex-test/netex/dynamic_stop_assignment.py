from dataclasses import dataclass

from .dynamic_stop_assignment_version_structure import DynamicStopAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DynamicStopAssignment(DynamicStopAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
