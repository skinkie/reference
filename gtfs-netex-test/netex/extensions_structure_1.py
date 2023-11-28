from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class ExtensionsStructure1:
    """Type for Extensions to schema.

    Wraps an 'any' tag to ensure decidability.

    :ivar any_element: Placeholder for user extensions.
    """
    class Meta:
        name = "ExtensionsStructure"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
