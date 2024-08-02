from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType
from .situation_record import SituationRecord

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class NonRoadEventInformation(SituationRecord):
    non_road_event_information_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "nonRoadEventInformationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
