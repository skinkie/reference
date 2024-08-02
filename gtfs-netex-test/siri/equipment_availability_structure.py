from dataclasses import dataclass, field
from typing import List, Optional

from .equipment_ref_structure import EquipmentRefStructure
from .equipment_status_enumeration import EquipmentStatusEnumeration
from .equipment_type_ref_structure import EquipmentTypeRefStructure
from .extensions_1 import Extensions1
from .feature_ref_structure_2 import FeatureRefStructure2
from .half_open_timestamp_output_range_structure import HalfOpenTimestampOutputRangeStructure
from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EquipmentAvailabilityStructure:
    equipment_ref: Optional[EquipmentRefStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_type_ref: Optional[EquipmentTypeRefStructure] = field(
        default=None,
        metadata={
            "name": "EquipmentTypeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_period: Optional[HalfOpenTimestampOutputRangeStructure] = field(
        default=None,
        metadata={
            "name": "ValidityPeriod",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    equipment_status: EquipmentStatusEnumeration = field(
        default=EquipmentStatusEnumeration.NOT_AVAILABLE,
        metadata={
            "name": "EquipmentStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        },
    )
    equipment_features: Optional["EquipmentAvailabilityStructure.EquipmentFeatures"] = field(
        default=None,
        metadata={
            "name": "EquipmentFeatures",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class EquipmentFeatures:
        feature_ref: List[FeatureRefStructure2] = field(
            default_factory=list,
            metadata={
                "name": "FeatureRef",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
