from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .extension_type import ExtensionType
from .measured_value import MeasuredValue

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class SiteMeasurements:
    measurement_site_reference: str = field(
        metadata={
            "name": "measurementSiteReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    measurement_time_default: XmlDateTime = field(
        metadata={
            "name": "measurementTimeDefault",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    measured_value: List["SiteMeasurements.MeasuredValue"] = field(
        default_factory=list,
        metadata={
            "name": "measuredValue",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    site_measurements_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "siteMeasurementsExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )

    @dataclass(kw_only=True)
    class MeasuredValue(MeasuredValue):
        index: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
