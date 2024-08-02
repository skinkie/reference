from dataclasses import dataclass

from .connection_monitoring_distributor_delivery_structure import ConnectionMonitoringDistributorDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringDistributorDelivery(ConnectionMonitoringDistributorDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
