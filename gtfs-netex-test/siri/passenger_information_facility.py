from dataclasses import dataclass, field

from .passenger_information_facility_enumeration import PassengerInformationFacilityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class PassengerInformationFacility:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: PassengerInformationFacilityEnumeration = field(
        default=PassengerInformationFacilityEnumeration.UNKNOWN,
        metadata={
            "required": True,
        },
    )
