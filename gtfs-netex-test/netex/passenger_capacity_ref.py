from dataclasses import dataclass
from netex.passenger_capacity_ref_structure import PassengerCapacityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerCapacityRef(PassengerCapacityRefStructure):
    """
    Reference to a PASSENGER CAPACITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
