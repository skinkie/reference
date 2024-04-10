from dataclasses import dataclass

from .day_type_assignment_ref_structure import DayTypeAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DayTypeAssignmentRef(DayTypeAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
