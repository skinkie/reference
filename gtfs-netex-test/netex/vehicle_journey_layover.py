from dataclasses import dataclass

from .vehicle_journey_layover_versioned_child_structure import VehicleJourneyLayoverVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleJourneyLayover(VehicleJourneyLayoverVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
