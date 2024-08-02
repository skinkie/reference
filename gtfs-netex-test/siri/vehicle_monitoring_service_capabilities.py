from dataclasses import dataclass

from .vehicle_monitoring_service_capabilities_structure import VehicleMonitoringServiceCapabilitiesStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringServiceCapabilities(VehicleMonitoringServiceCapabilitiesStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
