from dataclasses import dataclass

from .point_of_interest_version_structure import PointOfInterestVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PointOfInterest(PointOfInterestVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
