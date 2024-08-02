from dataclasses import dataclass, field
from typing import Optional

from .abstract_service_capabilities_response_structure import AbstractServiceCapabilitiesResponseStructure
from .extensions_1 import Extensions1
from .stop_timetable_permissions import StopTimetablePermissions
from .stop_timetable_service_capabilities import StopTimetableServiceCapabilities

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class StopTimetableCapabilitiesResponseStructure(AbstractServiceCapabilitiesResponseStructure):
    stop_timetable_service_capabilities: Optional[StopTimetableServiceCapabilities] = field(
        default=None,
        metadata={
            "name": "StopTimetableServiceCapabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_timetable_permissions: Optional[StopTimetablePermissions] = field(
        default=None,
        metadata={
            "name": "StopTimetablePermissions",
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
