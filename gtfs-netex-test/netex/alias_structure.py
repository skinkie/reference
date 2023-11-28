from dataclasses import dataclass, field
from typing import Optional
from netex.private_code import PrivateCode

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AliasStructure:
    """
    Alternative Private Code for a STOP PLACE.

    :ivar private_code:
    :ivar identifier_type: Type of identifier.
    """
    private_code: PrivateCode = field(
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    identifier_type: Optional[str] = field(
        default=None,
        metadata={
            "name": "IdentifierType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
