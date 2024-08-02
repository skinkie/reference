from dataclasses import dataclass, field
from typing import Optional

from .activity import Activity
from .disturbance_activity_type_enum import DisturbanceActivityTypeEnum
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class DisturbanceActivity(Activity):
    disturbance_activity_type: DisturbanceActivityTypeEnum = field(
        metadata={
            "name": "disturbanceActivityType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    disturbance_activity_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "disturbanceActivityExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
