from dataclasses import dataclass, field
from typing import Optional

from .alert_cdirection import AlertCdirection
from .alert_clinear import AlertClinear
from .alert_cmethod2_primary_point_location import AlertCmethod2PrimaryPointLocation
from .alert_cmethod2_secondary_point_location import AlertCmethod2SecondaryPointLocation
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AlertCmethod2Linear(AlertClinear):
    class Meta:
        name = "AlertCMethod2Linear"

    alert_cdirection: AlertCdirection = field(
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod2_primary_point_location: AlertCmethod2PrimaryPointLocation = field(
        metadata={
            "name": "alertCMethod2PrimaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod2_secondary_point_location: AlertCmethod2SecondaryPointLocation = field(
        metadata={
            "name": "alertCMethod2SecondaryPointLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_cmethod2_linear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCMethod2LinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
