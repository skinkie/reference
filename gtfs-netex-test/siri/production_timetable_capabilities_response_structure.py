from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .extensions_1 import Extensions1
from .production_timetable_permissions import ProductionTimetablePermissions
from .production_timetable_service_capabilities import ProductionTimetableServiceCapabilities

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    production_timetable_service_capabilities: Optional[ProductionTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "ProductionTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    production_timetable_permissions: Optional[ProductionTimetablePermissions] = field(
        default=None,
        metadata={
            "name": "ProductionTimetablePermissions",
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
