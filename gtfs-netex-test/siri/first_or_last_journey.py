from dataclasses import dataclass, field

from .first_or_last_journey_enumeration import FirstOrLastJourneyEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FirstOrLastJourney:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: FirstOrLastJourneyEnumeration = field(
        default=FirstOrLastJourneyEnumeration.UNSPECIFIED,
        metadata={
            "required": True,
        },
    )
