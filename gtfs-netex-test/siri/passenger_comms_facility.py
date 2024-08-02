from dataclasses import dataclass, field

from .passenger_comms_facility_enumeration import PassengerCommsFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PassengerCommsFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PassengerCommsFacilityEnumeration = field(
        default=PassengerCommsFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
