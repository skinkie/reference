from dataclasses import dataclass

from .passenger_spot_ref_structure import PassengerSpotRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpotRef(PassengerSpotRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
