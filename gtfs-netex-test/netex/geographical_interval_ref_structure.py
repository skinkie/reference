from dataclasses import dataclass
from netex.fare_interval_ref_structure import FareIntervalRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalIntervalRefStructure(FareIntervalRefStructure):
    """
    Type for Reference to a GEOGRAPHICAL INTERVAL.
    """
