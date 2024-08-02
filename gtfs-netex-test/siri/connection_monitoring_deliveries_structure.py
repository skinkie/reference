from dataclasses import dataclass, field
from typing import List, Union

from .connection_monitoring_distributor_delivery import ConnectionMonitoringDistributorDelivery
from .connection_monitoring_feeder_delivery import ConnectionMonitoringFeederDelivery

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringDeliveriesStructure:
    connection_monitoring_feeder_delivery_or_connection_monitoring_distributor_delivery: List[Union[ConnectionMonitoringFeederDelivery, ConnectionMonitoringDistributorDelivery]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ConnectionMonitoringFeederDelivery",
                    "type": ConnectionMonitoringFeederDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectionMonitoringDistributorDelivery",
                    "type": ConnectionMonitoringDistributorDelivery,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
