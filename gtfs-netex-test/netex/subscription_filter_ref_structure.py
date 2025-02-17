from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class SubscriptionFilterRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
