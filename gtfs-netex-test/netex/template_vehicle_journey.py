from dataclasses import dataclass

from .template_vehicle_journey_version_structure import TemplateVehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TemplateVehicleJourney(TemplateVehicleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
