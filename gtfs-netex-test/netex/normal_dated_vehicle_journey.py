from dataclasses import dataclass
from .normal_dated_vehicle_journey_version_structure import (
    NormalDatedVehicleJourneyVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NormalDatedVehicleJourney(NormalDatedVehicleJourneyVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
