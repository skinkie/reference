from dataclasses import dataclass

from .dated_vehicle_journey_version_structure import DatedVehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedVehicleJourney(DatedVehicleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
