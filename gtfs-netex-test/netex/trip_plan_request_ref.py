from dataclasses import dataclass
from netex.trip_plan_request_ref_structure import TripPlanRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TripPlanRequestRef(TripPlanRequestRefStructure):
    """
    Reference to a TRIP PLAN REQUEST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
