from dataclasses import dataclass, field

from .data_object_service_permission_structure import DataObjectServicePermissionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DataObjectPermissions:
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    data_object_permission: list[DataObjectServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectPermission",
            "type": "Element",
        },
    )
