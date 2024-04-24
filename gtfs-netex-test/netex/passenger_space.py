from dataclasses import dataclass

from .passenger_space_version_structure import PassengerSpaceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSpace(PassengerSpaceVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
