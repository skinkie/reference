from dataclasses import dataclass, field
from decimal import Decimal
from typing import List, Optional
from netex.access_feature_enumeration import AccessFeatureEnumeration
from netex.access_mode_enumeration import AccessModeEnumeration
from netex.accessibility_assessment import AccessibilityAssessment
from netex.accessibility_assessment_ref import AccessibilityAssessmentRef
from netex.border_type_enumeration import BorderTypeEnumeration
from netex.covered_enumeration import CoveredEnumeration
from netex.flooring_type_enumeration import FlooringTypeEnumeration
from netex.gated_enumeration import GatedEnumeration
from netex.gradient_enumeration import GradientEnumeration
from netex.lighting_enumeration import LightingEnumeration
from netex.link_version_structure import LinkVersionStructure
from netex.multilingual_string import MultilingualString
from netex.passage_type_enumeration import PassageTypeEnumeration
from netex.path_direction_enumeration import PathDirectionEnumeration
from netex.path_link_end_structure import PathLinkEndStructure
from netex.presentation_structure import PresentationStructure
from netex.public_use_enumeration import PublicUseEnumeration
from netex.site_facility_sets_rel_structure import SiteFacilitySetsRelStructure
from netex.tactile_warning_strip_enumeration import TactileWarningStripEnumeration
from netex.tilt_type_enumeration import TiltTypeEnumeration
from netex.transfer_duration_structure import TransferDurationStructure
from netex.transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PathLinkVersionStructure(LinkVersionStructure):
    """
    Type for a PATH LINK.

    :ivar from_value: Origin end of PATH LINK.
    :ivar to: Destination end of PATH LINK.
    :ivar description: Description of PATH LINK.
    :ivar accessibility_assessment_ref_or_accessibility_assessment:
    :ivar access_modes: Allowed MODEs to use in component.
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
    :ivar towards: Direction heading to show for PATH LINK when
        travelling  in its FROM / TO sense.
    :ivar back: Direction heading to show for PATH LINK when travelling
        in its TO / FROM sense.
    :ivar number_of_steps: Number of steps to take PATH LINK.
    :ivar minimum_height: Minimum Height of PATH LINK. +v1.1
    :ivar minimum_width: Minimum Width of PATH LINK. +v1.1
    :ivar allowed_use: Allowed direction of use: one way or two way.
        Default is two way.
    :ivar transition: Whether PATH LINK is up down or level in from to
        direction.
    :ivar gradient: Maximum gradient in degrees  (in the direction of
        the PATH LINK way). +v1.1
    :ivar gradient_type: Coded value of the maximum gradient.+v1.1
    :ivar tilt_angle: Maximum Tilt angle in degrees between -20 and 20
        (in the direction of the PATH LINK way). +v1.1
    :ivar tilt_type: Coded value of the maximum  tilt.  See allowed
        va;ues. +v1.1
    :ivar access_feature_type: Type of physical feature of PATH LINK.
    :ivar passage_type: Type of passage feature of PATH LINK.
    :ivar flooring_type: Type of flooring of the walking surface. +v1.1
    :ivar right_side_border: Type of border on the right side (in the
        direction of the PATH LINK).
    :ivar left_side_border: Type of border on the left side (in the
        direction of the PATH LINK). +v1.1
    :ivar tactile_warning_strip: Nature of the  tactile warning strips
        (in the direction of the PATH LINK). +v1.1
    :ivar tactile_guiding_strip: Indicates whether there are guiding
        strips. +v1.1
    :ivar maximum_flow_per_minute: Maximum number of passengers who can
        traverse PATH LINK per minute.
    :ivar transfer_duration: Timings for the transfer.
    """
    class Meta:
        name = "PathLink_VersionStructure"

    from_value: PathLinkEndStructure = field(
        metadata={
            "name": "From",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to: PathLinkEndStructure = field(
        metadata={
            "name": "To",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    accessibility_assessment_ref_or_accessibility_assessment: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AccessibilityAssessmentRef",
                    "type": AccessibilityAssessmentRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessibilityAssessment",
                    "type": AccessibilityAssessment,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
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
    towards: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Towards",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    back: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Back",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    allowed_use: Optional[PathDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "AllowedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gradient: Optional[int] = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    gradient_type: Optional[GradientEnumeration] = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tilt_angle: Optional[int] = field(
        default=None,
        metadata={
            "name": "TiltAngle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tilt_type: Optional[TiltTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TiltType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_feature_type: Optional[AccessFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    passage_type: Optional[PassageTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    flooring_type: Optional[FlooringTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlooringType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    right_side_border: Optional[BorderTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RightSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    left_side_border: Optional[BorderTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LeftSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_warning_strip: Optional[TactileWarningStripEnumeration] = field(
        default=None,
        metadata={
            "name": "TactileWarningStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    tactile_guiding_strip: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGuidingStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_flow_per_minute: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumFlowPerMinute",
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
