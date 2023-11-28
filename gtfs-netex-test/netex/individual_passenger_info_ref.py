from dataclasses import dataclass
from netex.individual_passenger_info_ref_structure import IndividualPassengerInfoRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualPassengerInfoRef(IndividualPassengerInfoRefStructure):
    """Reference to a INDIVIDUAL PASSENGER  INFO.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
