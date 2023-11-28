from dataclasses import dataclass, field
from typing import Optional, Union
from netex.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class ReferenceType:
    """
    Gml:ReferenceType is intended to be used in application schemas directly, if a
    property element shall use a "by-reference only" encoding.
    """
    owns: bool = field(
        default=False,
        metadata={
            "type": "Attribute",
        }
    )
    nil_reason: Optional[Union[str, NilReasonEnumerationValue]] = field(
        default=None,
        metadata={
            "name": "nilReason",
            "type": "Attribute",
            "pattern": r"other:\w{2,}",
        }
    )
