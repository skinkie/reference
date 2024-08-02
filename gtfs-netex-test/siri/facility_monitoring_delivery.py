from dataclasses import dataclass

from .facility_monitoring_delivery_structure import FacilityMonitoringDeliveryStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringDelivery(FacilityMonitoringDeliveryStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
