from dataclasses import dataclass

from .point_of_interest_ref_structure import PointOfInterestRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestRef(PointOfInterestRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
