from dataclasses import dataclass, field
from typing import List, Optional

from .extension_type import ExtensionType
from .header_information import HeaderInformation
from .measurement_site_table import MeasurementSiteTable
from .payload_publication import PayloadPublication

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class MeasurementSiteTablePublication(PayloadPublication):
    header_information: HeaderInformation = field(
        metadata={
            "name": "headerInformation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    measurement_site_table: List[MeasurementSiteTable] = field(
        default_factory=list,
        metadata={
            "name": "measurementSiteTable",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_table_publication_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteTablePublicationExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
