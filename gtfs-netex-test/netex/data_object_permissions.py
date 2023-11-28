from dataclasses import dataclass, field
from typing import List

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DataObjectPermissions:
    """
    Participants permissions to use the service, Only returned if requested.

    :ivar data_object_permission: Permission for a single participant or
        all participants to use an aspect of the service.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    data_object_permission: List[float] = field(
        default_factory=list,
        metadata={
            "name": "DataObjectPermission",
            "type": "Element",
        }
    )
