from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/acsb"


@dataclass(kw_only=True)
class LimitationRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
        },
    )
