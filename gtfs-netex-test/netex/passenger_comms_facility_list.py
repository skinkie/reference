from dataclasses import dataclass, field

from .passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class PassengerCommsFacilityList:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: list[PassengerCommsFacilityEnumeration] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
