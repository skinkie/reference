from dataclasses import dataclass
from .trip_leg_ref_structure import TripLegRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TripLegRef(TripLegRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
