from dataclasses import dataclass

from .trip_leg_ref_structure import TripLegRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TripLegRef(TripLegRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
