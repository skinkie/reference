from dataclasses import dataclass, field
from typing import List, Optional
from netex.access_feature_enumeration import AccessFeatureEnumeration
from netex.access_mode_enumeration import AccessModeEnumeration
from netex.access_summaries_rel_structure import AccessSummariesRelStructure
from netex.accessibility_assessment import AccessibilityAssessment
from netex.covered_enumeration import CoveredEnumeration
from netex.gated_enumeration import GatedEnumeration
from netex.lighting_enumeration import LightingEnumeration
from netex.navigation_type_enumeration import NavigationTypeEnumeration
from netex.path_link_end_structure import PathLinkEndStructure
from netex.path_links_in_sequence_rel_structure import PathLinksInSequenceRelStructure
from netex.places_in_sequence_rel_structure import PlacesInSequenceRelStructure
from netex.presentation_structure import PresentationStructure
from netex.public_use_enumeration import PublicUseEnumeration
from netex.section_in_sequence_versioned_child_structure import LinkSequenceVersionStructure
from netex.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.transfer_duration_structure import TransferDurationStructure
from netex.transfer_refs_rel_structure import TransferRefsRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class NavigationPathVersionStructure(LinkSequenceVersionStructure):
    """
    Type for NAVIGATION PATH.

    :ivar from_value: Origin end of NAVIGATION PATH. Only needed if
        detailed PATH LINKs are not given.
    :ivar to: Destination end of NAVIGATION PATH. Only needed if
        detailed PATH LINKs not given.
    :ivar accessibility_assessment:
    :ivar access_modes: MODEs of access which may used at associated
        place, e.g. foot access, bicycle access.
    :ivar summaries: Summaries of access features encountered in path.
    :ivar transfer_duration: Total time needed to navigate path (May be
        derived from links).
    :ivar public_use: Whether the component is available for public use
        or is restricted.
    :ivar covered: Whether the component is Indoors or outdoors. Default
        is Indoors.
    :ivar gated: Whether the component is within a gated area or freely
        accessible without a pass or ticket.
    :ivar lighting: Whether the component is lit or not. Default is well
        Lit.
    :ivar all_areas_wheelchair_accessible: Whether all areas of the
        component are wheelchair accessible.
    :ivar person_capacity: Total number of people that component can
        contain.
    :ivar presentation: Presentation defaults for SITE ELEMENT. +V1.2.2
    :ivar facilities: Facilities available at SITe.
    :ivar access_feature_list: Classification of Overall Accessibility
        of NAVIGATION PATH.
    :ivar navigation_type: Classification of Navigation.
    :ivar places_in_sequence: Ordered collection of References to STOP
        PLACE spaces Use for a branch path.
    :ivar path_links_in_sequence: Ordered collection of References to
        PATH LINKs.
    :ivar transfers: Access Links that NAVIGATION PATH serves.
    """
    class Meta:
        name = "NavigationPath_VersionStructure"

    from_value: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to: Optional[PathLinkEndStructure] = field(
        default=None,
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment: Optional[AccessibilityAssessment] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_modes: List[AccessModeEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessModes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    summaries: Optional[AccessSummariesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer_duration: Optional[TransferDurationStructure] = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    public_use: Optional[PublicUseEnumeration] = field(
        default=None,
        metadata={
            "name": "PublicUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    covered: Optional[CoveredEnumeration] = field(
        default=None,
        metadata={
            "name": "Covered",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gated: Optional[GatedEnumeration] = field(
        default=None,
        metadata={
            "name": "Gated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    lighting: Optional[LightingEnumeration] = field(
        default=None,
        metadata={
            "name": "Lighting",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    all_areas_wheelchair_accessible: Optional[bool] = field(
        default=None,
        metadata={
            "name": "AllAreasWheelchairAccessible",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    person_capacity: Optional[int] = field(
        default=None,
        metadata={
            "name": "PersonCapacity",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation: Optional[PresentationStructure] = field(
        default=None,
        metadata={
            "name": "Presentation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facilities: Optional[SiteFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_feature_list: List[AccessFeatureEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "AccessFeatureList",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    navigation_type: Optional[NavigationTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "NavigationType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    places_in_sequence: Optional[PlacesInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "placesInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    path_links_in_sequence: Optional[PathLinksInSequenceRelStructure] = field(
        default=None,
        metadata={
            "name": "pathLinksInSequence",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfers: Optional[TransferRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
