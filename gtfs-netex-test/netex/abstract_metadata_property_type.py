from dataclasses import dataclass, field


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(kw_only=True)
class AbstractMetadataPropertyType:
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        },
    )
