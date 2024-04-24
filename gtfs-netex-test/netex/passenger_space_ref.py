from dataclasses import dataclass

from .passenger_space_ref_structure import PassengerSpaceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpaceRef(PassengerSpaceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
