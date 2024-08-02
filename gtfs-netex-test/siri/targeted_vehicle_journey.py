from dataclasses import dataclass

from .targeted_vehicle_journey_structure import TargetedVehicleJourneyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TargetedVehicleJourney(TargetedVehicleJourneyStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
