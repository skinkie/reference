from dataclasses import dataclass, field
from typing import Optional

from .activity import Activity
from .extension_type import ExtensionType
from .public_event_type_enum import PublicEventTypeEnum

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class PublicEvent(Activity):
    public_event_type: PublicEventTypeEnum = field(
        metadata={
            "name": "publicEventType",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    public_event_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "publicEventExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
