from dataclasses import dataclass

from .estimated_vehicle_journey_structure import EstimatedVehicleJourneyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedVehicleJourney(EstimatedVehicleJourneyStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
