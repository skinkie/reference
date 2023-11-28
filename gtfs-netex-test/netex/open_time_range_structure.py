from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class OpenTimeRangeStructure:
    """Data Type for a range of times.

    Start time must be specified, end time is optional.

    :ivar start_time: The (inclusive) start time.
    :ivar end_time: The (inclusive) end time. If omitted, the range end
        is open-ended, that is, it should be interpreted as "forever".
    """
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
