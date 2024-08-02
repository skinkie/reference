from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .overall_period import OverallPeriod
from .validity_status_enum import ValidityStatusEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class Validity:
    validity_status: ValidityStatusEnum = field(
        metadata={
            "name": "validityStatus",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    overrunning: Optional[bool] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    validity_time_specification: OverallPeriod = field(
        metadata={
            "name": "validityTimeSpecification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    validity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "validityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
