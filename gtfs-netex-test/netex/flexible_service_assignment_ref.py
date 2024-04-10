from dataclasses import dataclass

from .flexible_service_assignment_ref_structure import FlexibleServiceAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FlexibleServiceAssignmentRef(FlexibleServiceAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
