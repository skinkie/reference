from dataclasses import dataclass

from .connection_service_permission_structure import ConnectionServicePermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetablePermission(ConnectionServicePermissionStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"
