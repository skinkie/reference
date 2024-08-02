from dataclasses import dataclass, field
from typing import List

from .permissions_structure import PermissionsStructure
from .production_timetable_permission import ProductionTimetablePermission

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ProductionTimetablePermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    production_timetable_permission: List[ProductionTimetablePermission] = field(
        default_factory=list,
        metadata={
            "name": "ProductionTimetablePermission",
            "type": "Element",
        },
    )
