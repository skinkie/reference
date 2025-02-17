from dataclasses import dataclass, field

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(slots=True, kw_only=True)
class AbstractMemberType:
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
