from dataclasses import dataclass, field
from xsdata.models.datatype import XmlTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClosedTimeRangeStructure:
    """Data Type for a range of times.

    Both start and end time are required.

    :ivar start_time: The (inclusive) start time.
    :ivar end_time: The (inclusive) end time.
    """
    start_time: XmlTime = field(
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_time: XmlTime = field(
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
