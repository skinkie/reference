from dataclasses import dataclass, field
from typing import List

from .permissions_structure import PermissionsStructure
from .situation_exchange_service_permission_structure import SituationExchangeServicePermissionStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangePermissions(PermissionsStructure):
    class Meta:
        namespace = "http://www.siri.org.uk/siri"

    situation_exchange_permission: List[SituationExchangeServicePermissionStructure] = field(
        default_factory=list,
        metadata={
            "name": "SituationExchangePermission",
            "type": "Element",
        },
    )
