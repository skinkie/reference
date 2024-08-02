from dataclasses import dataclass

from .vehicle_monitoring_request_structure import VehicleMonitoringRequestStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleMonitoringRequest(VehicleMonitoringRequestStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
