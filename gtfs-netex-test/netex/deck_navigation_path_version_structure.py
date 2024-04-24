from dataclasses import dataclass, field
from typing import List, Optional

from .access_feature_enumeration import AccessFeatureEnumeration
from .access_mode_enumeration import AccessModeEnumeration
from .access_summaries_rel_structure import AccessSummariesRelStructure
from .accessibility_assessment import AccessibilityAssessment
from .covered_enumeration import CoveredEnumeration
from .deck_navigation_path_type_enumeration import DeckNavigationPathTypeEnumeration
from .deck_path_link_end_structure import DeckPathLinkEndStructure
from .deck_places_in_sequence_rel_structure import DeckPlacesInSequenceRelStructure
from .gated_enumeration import GatedEnumeration
from .generic_navigation_path_version_structure import GenericNavigationPathVersionStructure
from .lighting_enumeration import LightingEnumeration
from .path_links_in_sequence_rel_structure import PathLinksInSequenceRelStructure
from .presentation_structure import PresentationStructure
from .public_use_enumeration import PublicUseEnumeration
from .service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from .transfer_duration_structure import TransferDurationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckNavigationPathVersionStructure(GenericNavigationPathVersionStructure):
    class Meta:
        name = "DeckNavigationPath_VersionStructure"

    from_value: Optional[DeckPathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to: Optional[DeckPathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_modes: List[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    summaries: Optional[AccessSummariesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transfer_duration: Optional[TransferDurationStructure] = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    public_use: Optional[PublicUseEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    covered: Optional[CoveredEnumeration] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gated: Optional[GatedEnumeration] = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    person_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_feature_list: List[AccessFeatureEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFeatureList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    deck_navigation_type: Optional[DeckNavigationPathTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "DeckNavigationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_places_in_sequence: Optional[DeckPlacesInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "deckPlacesInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    path_links_in_sequence: Optional[PathLinksInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
