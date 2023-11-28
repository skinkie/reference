from dataclasses import dataclass
from netex.fare_request_ref_structure import FareRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SingleTripFareRequestRefStructure(FareRequestRefStructure):
    """
    Type for Reference to a SINGLE TRIP FARE REQUEST.
    """
