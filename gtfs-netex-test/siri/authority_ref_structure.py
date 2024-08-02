from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AuthorityRefStructure:
    value: str = field(
        default="",
        metadata={
            "required": True,
            "max_length": 2,
        },
    )
