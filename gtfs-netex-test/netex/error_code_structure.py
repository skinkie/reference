from dataclasses import dataclass, field
from typing import Optional


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ErrorCodeStructure:
    error_text: Optional[str] = field(
        default=None,
        metadata={
            "name": "ErrorText",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
