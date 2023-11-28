from dataclasses import dataclass, field
from typing import List, Union
from netex.nil_reason_enumeration_value import NilReasonEnumerationValue

__NAMESPACE__ = "http://www.opengis.net/gml/3.2"


@dataclass(unsafe_hash=True, kw_only=True)
class MeasureOrNilReasonListType:
    """Gml:MeasureOrNilReasonListType provides for a list of quantities.

    An instance element may also include embedded values from
    NilReasonType. It is intended to be used in situations where a value
    is expected, but the value may be absent for some reason.
    """
    value: List[Union[str, NilReasonEnumerationValue]] = field(
        default_factory=list,
        metadata={
            "pattern": r"other:\w{2,}",
            "tokens": True,
        }
    )
    uom: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
            "pattern": r"[^: \n\r\t]+",
        }
    )
