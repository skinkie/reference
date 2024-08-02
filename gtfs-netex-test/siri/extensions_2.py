from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class Extensions2:
    class Meta:
        name = "Extensions"
        namespace = "http://www.ifopt.org.uk/ifopt"

    any_element: Optional[object] = field(
        default=None,
        metadata={
            "type": "Wildcard",
            "namespace": "##any",
        },
    )
