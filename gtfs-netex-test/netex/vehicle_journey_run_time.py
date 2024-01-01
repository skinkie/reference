from dataclasses import dataclass
from .vehicle_journey_run_time_versioned_child_structure import (
    VehicleJourneyRunTimeVersionedChildStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourneyRunTime(VehicleJourneyRunTimeVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
