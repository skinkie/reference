from dataclasses import dataclass

from .round_trip_version_structure import RoundTripVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RoundTrip(RoundTripVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
