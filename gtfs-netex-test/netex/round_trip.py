from dataclasses import dataclass
from .round_trip_version_structure import RoundTripVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RoundTrip(RoundTripVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
