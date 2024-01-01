from dataclasses import dataclass
from .vehicle_journey_version_structure import VehicleJourneyVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleJourney(VehicleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
