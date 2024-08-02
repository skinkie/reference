from dataclasses import dataclass

from .connection_monitoring_feeder_delivery_structure import ConnectionMonitoringFeederDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringFeederDelivery(ConnectionMonitoringFeederDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
