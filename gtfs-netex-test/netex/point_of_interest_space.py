from dataclasses import dataclass
from .point_of_interest_space_version_structure import (
    PointOfInterestSpaceVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestSpace(PointOfInterestSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
