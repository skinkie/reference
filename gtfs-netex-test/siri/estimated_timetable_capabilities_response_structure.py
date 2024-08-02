from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .estimated_timetable_permissions import EstimatedTimetablePermissions
from .estimated_timetable_service_capabilities import EstimatedTimetableServiceCapabilities
from .extensions_1 import Extensions1

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    estimated_timetable_service_capabilities: Optional[EstimatedTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_permissions: Optional[EstimatedTimetablePermissions] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetablePermissions",
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
