from dataclasses import dataclass

from .passenger_capacity_ref_structure import PassengerCapacityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerCapacityRef(PassengerCapacityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
