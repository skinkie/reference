from dataclasses import dataclass, field
from xsdata.models.datatype import XmlDateTime

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ClosedTimestampRangeStructure:
    """Data Type for a range of date and times.

    Both start and end time are required.

    :ivar start_time: The (inclusive) start date and time.
    :ivar end_time: The (inclusive) end date and time.
    """
    start_time: XmlDateTime = field(
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_time: XmlDateTime = field(
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
