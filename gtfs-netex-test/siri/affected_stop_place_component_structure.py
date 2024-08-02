from dataclasses import dataclass, field
from typing import List, Optional

from .accessibility_feature_enumeration_2 import AccessibilityFeatureEnumeration2
from .affected_facility_structure import AffectedFacilityStructure
from .affected_stop_place_element_structure import AffectedStopPlaceElementStructure
from .extensions_1 import Extensions1
from .link_projection import LinkProjection
from .natural_language_string_structure import NaturalLanguageStringStructure
from .offset_structure import OffsetStructure
from .point_projection import PointProjection
from .stop_place_component_ref_structure import StopPlaceComponentRefStructure
from .stop_place_component_type_enumeration import StopPlaceComponentTypeEnumeration
from .zone_projection import ZoneProjection

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedStopPlaceComponentStructure(AffectedStopPlaceElementStructure):
    component_ref: StopPlaceComponentRefStructure = field(
        metadata={
            "name": "ComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    component_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ComponentName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    component_type: Optional[StopPlaceComponentTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "ComponentType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    point_projection: Optional[PointProjection] = field(
        default=None,
        metadata={
            "name": "PointProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    link_projection: Optional[LinkProjection] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    zone_projection: Optional[ZoneProjection] = field(
        default=None,
        metadata={
            "name": "ZoneProjection",
            "type": "Element",
            "namespace": "http://www.ifopt.org.uk/ifopt",
        },
    )
    offset: Optional[OffsetStructure] = field(
        default=None,
        metadata={
            "name": "Offset",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    access_feature_type: Optional[AccessibilityFeatureEnumeration2] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_facilities: Optional["AffectedStopPlaceComponentStructure.AffectedFacilities"] = field(
        default=None,
        metadata={
            "name": "AffectedFacilities",
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
    class AffectedFacilities:
        affected_facility: List[AffectedFacilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "AffectedFacility",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
