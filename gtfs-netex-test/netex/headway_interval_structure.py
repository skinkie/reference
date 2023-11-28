from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class HeadwayIntervalStructure:
    """
    Type for a HEADWAY INTERVAL.

    :ivar scheduled_headway_interval: Scheduled normal headway interval.
    :ivar minimum_headway_interval: Minimum headway interval.
    :ivar maximum_headway_interval: Maximum headway interval.
    """
    scheduled_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
