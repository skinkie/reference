from dataclasses import dataclass
from .point_of_interest_entrance_ref_structure import (
    PointOfInterestEntranceRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PointOfInterestEntranceRef(PointOfInterestEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
