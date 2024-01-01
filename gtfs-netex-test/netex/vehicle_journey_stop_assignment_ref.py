from dataclasses import dataclass
from .vehicle_journey_stop_assignment_ref_structure import (
    VehicleJourneyStopAssignmentRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyStopAssignmentRef(
    VehicleJourneyStopAssignmentRefStructure
):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
