from dataclasses import dataclass

from .recharging_point_assignment_version_structure import (
    RechargingPointAssignmentVersionStructure,
)

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingPointAssignment(RechargingPointAssignmentVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
