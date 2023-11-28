from dataclasses import dataclass, field
from typing import Optional
from netex.extensions_1 import Extensions1
from netex.request_structure import RequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckStatusRequestStructure(RequestStructure):
    """
    Type for check status request.

    :ivar extensions:
    :ivar version: Version number of request.
    """
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        }
    )
    version: str = field(
        default="2.0",
        metadata={
            "type": "Attribute",
        }
    )
