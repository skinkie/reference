from dataclasses import dataclass

from .vehicle_journey_headway_versioned_child_structure import VehicleJourneyHeadwayVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleJourneyHeadway(VehicleJourneyHeadwayVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
