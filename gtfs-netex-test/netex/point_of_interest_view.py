from dataclasses import dataclass

from .point_of_interest_derived_view_structure import PointOfInterestDerivedViewStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterestView(PointOfInterestDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
