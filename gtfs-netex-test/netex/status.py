from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class Status:
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    value: bool = field(
        default=True,
        metadata={
            "required": True,
        },
    )
