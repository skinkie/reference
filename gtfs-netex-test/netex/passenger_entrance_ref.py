from dataclasses import dataclass

from .passenger_entrance_ref_structure import PassengerEntranceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerEntranceRef(PassengerEntranceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
