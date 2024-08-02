from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class FilterExitManagement:
    filter_end: bool = field(
        metadata={
            "name": "filterEnd",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    filter_out_of_range: bool = field(
        metadata={
            "name": "filterOutOfRange",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    filter_exit_management_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "filterExitManagementExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
