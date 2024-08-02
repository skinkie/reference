from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .abstract_subscription_structure import AbstractSubscriptionStructure
from .connection_monitoring_request import ConnectionMonitoringRequest
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringSubscriptionRequestStructure(AbstractSubscriptionStructure):
    connection_monitoring_request: ConnectionMonitoringRequest = field(
        metadata={
            "name": "ConnectionMonitoringRequest",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    change_before_updates: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ChangeBeforeUpdates",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
