from dataclasses import dataclass
from netex.journey_timing_ref_structure import JourneyTimingRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleTypePreferenceRefStructure(JourneyTimingRefStructure):
    """
    Type for a reference to a VEHICLE TYPE PREFERENCE.
    """
