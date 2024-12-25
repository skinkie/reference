from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class CoordinatesStructure:
    value: list[str] = field(
        default_factory=list,
        metadata={
            "tokens": True,
        },
    )
