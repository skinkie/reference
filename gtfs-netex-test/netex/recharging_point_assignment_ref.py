from dataclasses import dataclass

from .recharging_point_assignment_ref_structure import RechargingPointAssignmentRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RechargingPointAssignmentRef(RechargingPointAssignmentRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
