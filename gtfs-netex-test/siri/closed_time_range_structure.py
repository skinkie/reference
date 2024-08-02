from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlTime

from .end_time_precision_enumeration import EndTimePrecisionEnumeration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ClosedTimeRangeStructure:
    start_time: XmlTime = field(
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    end_time: XmlTime = field(
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    end_time_precision: Optional[EndTimePrecisionEnumeration] = field(
        default=None,
        metadata={
            "name": "EndTimePrecision",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
