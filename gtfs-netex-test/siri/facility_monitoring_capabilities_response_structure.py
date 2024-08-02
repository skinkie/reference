from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .extensions_1 import Extensions1
from .facility_monitoring_permissions import FacilityMonitoringPermissions
from .facility_monitoring_service_capabilities import FacilityMonitoringServiceCapabilities

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    facility_monitoring_service_capabilities: Optional[FacilityMonitoringServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_monitoring_permissions: Optional[FacilityMonitoringPermissions] = field(
        default=None,
        metadata={
            "name": "FacilityMonitoringPermissions",
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
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
