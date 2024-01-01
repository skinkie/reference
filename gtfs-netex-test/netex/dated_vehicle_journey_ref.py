from dataclasses import dataclass
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DatedVehicleJourneyRef(VehicleJourneyRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
