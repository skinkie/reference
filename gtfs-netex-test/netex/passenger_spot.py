from dataclasses import dataclass

from .passenger_spot_version_structure import PassengerSpotVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpot(PassengerSpotVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
