from dataclasses import dataclass, field

from .normal_dated_vehicle_journey_version_structure import NormalDatedVehicleJourneyVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class NormalDatedVehicleJourney(NormalDatedVehicleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
