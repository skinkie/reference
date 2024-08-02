from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .header_information import HeaderInformation
from .payload_publication import PayloadPublication
from .site_measurements import SiteMeasurements

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class MeasuredDataPublication(PayloadPublication):
    measurement_site_table_reference: str = field(
        metadata={
            "name": "measurementSiteTableReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
            "max_length": 1024,
        }
    )
    header_information: HeaderInformation = field(
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    site_measurements: List[SiteMeasurements] = field(
        default_factory=list,
        metadata={
            "name": "siteMeasurements",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measured_data_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measuredDataPublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
