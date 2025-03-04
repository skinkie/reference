from dataclasses import dataclass

from .distribution_assignment_version_structure import DistributionAssignmentVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DistributionAssignment(DistributionAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
