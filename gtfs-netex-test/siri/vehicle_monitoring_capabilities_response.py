from dataclasses import dataclass

from .vehicle_monitoring_capabilities_response_structure import VehicleMonitoringCapabilitiesResponseStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringCapabilitiesResponse(VehicleMonitoringCapabilitiesResponseStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
