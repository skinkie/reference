from dataclasses import dataclass

from .point_in_single_journey_path_ref_structure import PointInSingleJourneyPathRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointInSingleJourneyPathRef(PointInSingleJourneyPathRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
