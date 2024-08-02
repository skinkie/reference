from dataclasses import dataclass, field
from typing import Optional

from .abstract_permission_structure import AbstractPermissionStructure
from .extensions_1 import Extensions1
from .line_permissions import LinePermissions
from .operator_permissions import OperatorPermissions

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class SituationExchangeServicePermissionStructure(AbstractPermissionStructure):
    operator_permissions: OperatorPermissions = field(
        metadata={
            "name": "OperatorPermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    line_permissions: LinePermissions = field(
        metadata={
            "name": "LinePermissions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
