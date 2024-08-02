from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDuration

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .estimated_timetable_detail_enumeration import EstimatedTimetableDetailEnumeration
from .extensions_1 import Extensions1
from .include_interchanges import IncludeInterchanges
from .include_journey_relations import IncludeJourneyRelations
from .include_train_formations import IncludeTrainFormations
from .include_translations import IncludeTranslations
from .line_direction_structure import LineDirectionStructure
from .operator_ref_structure import OperatorRefStructure
from .product_category_ref_structure import ProductCategoryRefStructure
from .stop_point_ref_structure import StopPointRefStructure
from .vehicle_modes_enumeration import VehicleModesEnumeration
from .version_ref_structure import VersionRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedTimetableRequestStructure(AbstractFunctionalServiceRequestStructure):
    preview_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreviewInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    timetable_version_ref: Optional[VersionRefStructure] = field(
        default=None,
        metadata={
            "name": "TimetableVersionRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: List[OperatorRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    lines: Optional["EstimatedTimetableRequestStructure.Lines"] = field(
        default=None,
        metadata={
            "name": "Lines",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_mode: List[VehicleModesEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "VehicleMode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_ref: List[ProductCategoryRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_ref: List[StopPointRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_translations: Optional[IncludeTranslations] = field(
        default=None,
        metadata={
            "name": "IncludeTranslations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_interchanges: Optional[IncludeInterchanges] = field(
        default=None,
        metadata={
            "name": "IncludeInterchanges",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_journey_relations: Optional[IncludeJourneyRelations] = field(
        default=None,
        metadata={
            "name": "IncludeJourneyRelations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_train_formations: Optional[IncludeTrainFormations] = field(
        default=None,
        metadata={
            "name": "IncludeTrainFormations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    estimated_timetable_detail_level: Optional[EstimatedTimetableDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "EstimatedTimetableDetailLevel",
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
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )

    @dataclass(kw_only=True)
    class Lines:
        line_direction: List[LineDirectionStructure] = field(
            default_factory=list,
            metadata={
                "name": "LineDirection",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
