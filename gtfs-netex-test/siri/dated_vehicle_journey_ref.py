from dataclasses import dataclass

from .dated_vehicle_journey_ref_structure import DatedVehicleJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedVehicleJourneyRef(DatedVehicleJourneyRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
