from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(slots=True, kw_only=True)
class SubscriptionContextStructure:
    heartbeat_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "HeartbeatInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
