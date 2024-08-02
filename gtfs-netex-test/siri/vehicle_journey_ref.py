from dataclasses import dataclass

from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleJourneyRef(VehicleJourneyRefStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
