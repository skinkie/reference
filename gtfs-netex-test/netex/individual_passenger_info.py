from dataclasses import dataclass, field
from netex.individual_passenger_info_version_structure import IndividualPassengerInfoVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class IndividualPassengerInfo(IndividualPassengerInfoVersionStructure):
    """Information characterising an INDIVIDUAL TRAVELER as a driver of a VEHICLE
    POOLING SERVICE.

    +v1.2.2
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
