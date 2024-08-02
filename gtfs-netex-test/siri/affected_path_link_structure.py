from dataclasses import dataclass, field
from typing import List, Optional

from .accessibility_feature_enumeration_2 import AccessibilityFeatureEnumeration2
from .extensions_1 import Extensions1
from .link_projection_structure import LinkProjectionStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .offset_structure import OffsetStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedPathLinkStructure:
    link_ref: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "LinkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_feature: Optional[AccessibilityFeatureEnumeration2] = field(
        default=None,
        metadata={
            "name": "AccessibilityFeature",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_direction: List[str] = field(
        default_factory=list,
        metadata={
            "name": "LinkDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    link_projection: Optional[LinkProjectionStructure] = field(
        default=None,
        metadata={
            "name": "LinkProjection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
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
    extensions: Optional[Extensions1] = field(
        default=None,
        metadata={
            "name": "Extensions",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
