from dataclasses import dataclass
from netex.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DatedVehicleJourneyRefStructure(VehicleJourneyRefStructure):
    """
    Type for a reference to a DATED VEHICLE JOURNEY.
    """
