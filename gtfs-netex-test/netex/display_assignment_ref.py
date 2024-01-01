from dataclasses import dataclass
from .display_assignment_ref_structure import DisplayAssignmentRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DisplayAssignmentRef(DisplayAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
