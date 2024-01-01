from dataclasses import dataclass
from .trip_ref_structure import TripRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TripRef(TripRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
