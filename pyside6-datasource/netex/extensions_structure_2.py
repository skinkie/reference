from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ExtensionsStructure2:
    """Type for Extensions to schema.

    Wraps an 'any' tag to ensure decidability.

    :ivar any_element: Placeholder for user extensions.
    """
    class Meta:
        name = "ExtensionsStructure"

    any_element: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        }
    )
