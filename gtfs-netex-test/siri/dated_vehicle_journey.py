from dataclasses import dataclass

from .dated_vehicle_journey_structure import DatedVehicleJourneyStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedVehicleJourney(DatedVehicleJourneyStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
