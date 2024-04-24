from dataclasses import dataclass

from .passenger_entrance_version_structure import PassengerEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerEntrance(PassengerEntranceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
