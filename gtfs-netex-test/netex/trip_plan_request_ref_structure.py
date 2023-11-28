from dataclasses import dataclass
from netex.passenger_information_request_ref_structure import PassengerInformationRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TripPlanRequestRefStructure(PassengerInformationRequestRefStructure):
    """
    Type for Reference to a TRIP PLAN REQUEST.
    """
