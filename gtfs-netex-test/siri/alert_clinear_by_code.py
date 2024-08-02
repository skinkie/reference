from dataclasses import dataclass, field
from typing import Optional

from .alert_cdirection import AlertCdirection
from .alert_clinear import AlertClinear
from .alert_clocation import AlertClocation
from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AlertClinearByCode(AlertClinear):
    class Meta:
        name = "AlertCLinearByCode"

    alert_cdirection: AlertCdirection = field(
        metadata={
            "name": "alertCDirection",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    location_code_for_linear_location: AlertClocation = field(
        metadata={
            "name": "locationCodeForLinearLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    alert_clinear_by_code_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearByCodeExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
