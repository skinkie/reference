from dataclasses import dataclass, field
from typing import Optional

from .activity import Activity
from .authority_operation_type_enum import AuthorityOperationTypeEnum
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AuthorityOperation(Activity):
    authority_operation_type: AuthorityOperationTypeEnum = field(
        metadata={
            "name": "authorityOperationType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    authority_operation_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "authorityOperationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
