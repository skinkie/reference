from dataclasses import dataclass

from .assignment_ref_structure import AssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AssignmentRef(AssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
