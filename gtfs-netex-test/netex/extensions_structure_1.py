from dataclasses import dataclass, field
from typing import Optional


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ExtensionsStructure1:
    class Meta:
        name = "ExtensionsStructure"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
