from dataclasses import dataclass, field
from typing import Optional

from .extension_type import ExtensionType

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class AlertClinear:
    class Meta:
        name = "AlertCLinear"

    alert_clocation_country_code: str = field(
        metadata={
            "name": "alertCLocationCountryCode",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_number: str = field(
        metadata={
            "name": "alertCLocationTableNumber",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clocation_table_version: str = field(
        metadata={
            "name": "alertCLocationTableVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    alert_clinear_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "alertCLinearExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
