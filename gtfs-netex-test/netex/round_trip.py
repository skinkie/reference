from dataclasses import dataclass, field
from netex.round_trip_version_structure import RoundTripVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RoundTrip(RoundTripVersionStructure):
    """
    Properties relating to single or return trip use of a fare.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
