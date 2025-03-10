from dataclasses import dataclass

from .trip_plan_request_ref_structure import TripPlanRequestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TripPlanRequestRef(TripPlanRequestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
