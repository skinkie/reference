from dataclasses import dataclass, field
from typing import Optional

from .alert_clocation import AlertClocation
from .extension_type import ExtensionType
from .offset_distance import OffsetDistance

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AlertCmethod4SecondaryPointLocation:
    class Meta:
        name = "AlertCMethod4SecondaryPointLocation"

    alert_clocation: AlertClocation = field(
        metadata={
            "name": "alertCLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    offset_distance: OffsetDistance = field(
        metadata={
            "name": "offsetDistance",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod4_secondary_point_location_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4SecondaryPointLocationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
