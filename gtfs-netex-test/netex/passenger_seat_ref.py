from dataclasses import dataclass

from .passenger_seat_ref_structure import PassengerSeatRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerSeatRef(PassengerSeatRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
