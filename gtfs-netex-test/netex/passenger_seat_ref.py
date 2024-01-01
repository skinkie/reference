from dataclasses import dataclass
from .passenger_seat_ref_structure import PassengerSeatRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PassengerSeatRef(PassengerSeatRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
