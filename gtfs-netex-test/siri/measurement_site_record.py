from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .computation_method_enum import ComputationMethodEnum
from .direction_enum import DirectionEnum
from .extension_type import ExtensionType
from .location import Location
from .measurement_specific_characteristics import MeasurementSpecificCharacteristics
from .multilingual_string import MultilingualString

__NAMESPACE__ = "http://datex2.eu/schema/2_0RC1/2_0"


@dataclass(kw_only=True)
class MeasurementSiteRecord:
    measurement_site_record_version: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordVersion",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_record_version_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordVersionTime",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    computation_method: Optional[ComputationMethodEnum] = field(
        default=None,
        metadata={
            "name": "computationMethod",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_equipment_reference: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentReference",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    measurement_equipment_type_used: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementEquipmentTypeUsed",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "measurementSiteName",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_number_of_lanes: Optional[int] = field(
        default=None,
        metadata={
            "name": "measurementSiteNumberOfLanes",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_site_identification: Optional[str] = field(
        default=None,
        metadata={
            "name": "measurementSiteIdentification",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "max_length": 1024,
        },
    )
    measurement_side: Optional[DirectionEnum] = field(
        default=None,
        metadata={
            "name": "measurementSide",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    measurement_specific_characteristics: List["MeasurementSiteRecord.MeasurementSpecificCharacteristics"] = field(
        default_factory=list,
        metadata={
            "name": "measurementSpecificCharacteristics",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "min_occurs": 1,
        },
    )
    measurement_site_location: Location = field(
        metadata={
            "name": "measurementSiteLocation",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
            "required": True,
        }
    )
    measurement_site_record_extension: Optional[ExtensionType] = field(
        default=None,
        metadata={
            "name": "measurementSiteRecordExtension",
            "type": "Element",
            "namespace": "http://datex2.eu/schema/2_0RC1/2_0",
        },
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )

    @dataclass(kw_only=True)
    class MeasurementSpecificCharacteristics(MeasurementSpecificCharacteristics):
        index: int = field(
            metadata={
                "type": "Attribute",
                "required": True,
            }
        )
