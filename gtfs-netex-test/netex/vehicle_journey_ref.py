from dataclasses import dataclass
from netex.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyRef(VehicleJourneyRefStructure):
    """Reference to a VEHICLE JOURNEY.

    If given by context does not need to be repeated.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
