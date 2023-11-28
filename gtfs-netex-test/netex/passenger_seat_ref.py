from dataclasses import dataclass
from netex.passenger_seat_ref_structure import PassengerSeatRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PassengerSeatRef(PassengerSeatRefStructure):
    """
    Reference to a  PASSENGER SEAT +v1.1.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
