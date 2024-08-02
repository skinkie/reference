from dataclasses import dataclass, field
from typing import Optional

__NAMESPACE__ = "http://www.ifopt.org.uk/ifopt"


@dataclass(kw_only=True)
class AliasStructure:
    private_code: str = field(
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
            "required": True,
        }
    )
    identifier_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentifierType",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
