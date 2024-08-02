from dataclasses import dataclass, field

from .arrival_boarding_activity_enumeration import ArrivalBoardingActivityEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ArrivalBoardingActivity:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: ArrivalBoardingActivityEnumeration = field(
        default=ArrivalBoardingActivityEnumeration.ALIGHTING,
        metadata={
            "required": True,
        },
    )
