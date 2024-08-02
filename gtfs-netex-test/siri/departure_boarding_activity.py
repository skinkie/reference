from dataclasses import dataclass, field

from .departure_boarding_activity_enumeration import DepartureBoardingActivityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DepartureBoardingActivity:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: DepartureBoardingActivityEnumeration = field(
        default=DepartureBoardingActivityEnumeration.BOARDING,
        metadata={
            "required": True,
        },
    )
