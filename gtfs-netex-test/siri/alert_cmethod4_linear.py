from dataclasses import dataclass, field
from typing import Optional

from .alert_cdirection import AlertCdirection
from .alert_clinear import AlertClinear
from .alert_cmethod4_primary_point_location import AlertCmethod4PrimaryPointLocation
from .alert_cmethod4_secondary_point_location import AlertCmethod4SecondaryPointLocation
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AlertCmethod4Linear(AlertClinear):
    class Meta:
        name = "AlertCMethod4Linear"

    alert_cdirection: AlertCdirection = field(
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod4_primary_point_location: AlertCmethod4PrimaryPointLocation = field(
        metadata={
            "name": "alertCMethod4PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod4_secondary_point_location: AlertCmethod4SecondaryPointLocation = field(
        metadata={
            "name": "alertCMethod4SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod4_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod4LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
