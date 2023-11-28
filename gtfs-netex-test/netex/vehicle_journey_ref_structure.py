from dataclasses import dataclass
from netex.journey_ref_structure import JourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleJourneyRefStructure(JourneyRefStructure):
    """
    Type for a reference to a VEHICLE JOURNEY.
    """
