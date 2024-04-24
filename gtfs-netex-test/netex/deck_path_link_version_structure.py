from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .access_feature_enumeration import AccessFeatureEnumeration
from .accessibility_assessment import AccessibilityAssessment
from .accessibility_assessment_ref import AccessibilityAssessmentRef
from .border_type_enumeration import BorderTypeEnumeration
from .check_constraints_rel_structure import CheckConstraintsRelStructure
from .class_of_use_ref import ClassOfUseRef
from .covered_enumeration import CoveredEnumeration
from .deck_level_ref import DeckLevelRef
from .deck_path_link_end_structure import DeckPathLinkEndStructure
from .deck_ref import DeckRef
from .equipment_places_rel_structure import EquipmentPlacesRelStructure
from .fare_class import FareClass
from .flooring_status_enumeration import FlooringStatusEnumeration
from .flooring_type_enumeration import FlooringTypeEnumeration
from .gated_enumeration import GatedEnumeration
from .generic_path_link_version_structure import GenericPathLinkVersionStructure
from .gradient_enumeration import GradientEnumeration
from .lighting_enumeration import LightingEnumeration
from .local_services_rel_structure import LocalServicesRelStructure
from .multilingual_string import MultilingualString
from .passage_type_enumeration import PassageTypeEnumeration
from .path_direction_enumeration import PathDirectionEnumeration
from .place_equipments_rel_structure import PlaceEquipmentsRelStructure
from .public_use_enumeration import PublicUseEnumeration
from .tactile_guiding_strip_status_enumeration import TactileGuidingStripStatusEnumeration
from .tactile_warning_strip_enumeration import TactileWarningStripEnumeration
from .tilt_type_enumeration import TiltTypeEnumeration
from .transfer_duration_structure import TransferDurationStructure
from .transition_enumeration import TransitionEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class DeckPathLinkVersionStructure(GenericPathLinkVersionStructure):
    class Meta:
        name = "DeckPathLink_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    accessibility_assessment_ref_or_accessibility_assessment: Optional[Union[AccessibilityAssessmentRef, AccessibilityAssessment]] = field(
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
    towards: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Towards",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    back: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Back",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    number_of_steps: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfSteps",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_height: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumHeight",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_width: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "MinimumWidth",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    allowed_use: Optional[PathDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "AllowedUse",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transition: Optional[TransitionEnumeration] = field(
        default=None,
        metadata={
            "name": "Transition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient: Optional[int] = field(
        default=None,
        metadata={
            "name": "Gradient",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    gradient_type: Optional[GradientEnumeration] = field(
        default=None,
        metadata={
            "name": "GradientType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_angle: Optional[int] = field(
        default=None,
        metadata={
            "name": "TiltAngle",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tilt_type: Optional[TiltTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "TiltType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    access_feature_type: Optional[AccessFeatureEnumeration] = field(
        default=None,
        metadata={
            "name": "AccessFeatureType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    passage_type: Optional[PassageTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "PassageType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flooring_type: Optional[FlooringTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "FlooringType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    flooring_status: Optional[FlooringStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "FlooringStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    right_side_border: Optional[BorderTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RightSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    left_side_border: Optional[BorderTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "LeftSideBorder",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_warning_strip: Optional[TactileWarningStripEnumeration] = field(
        default=None,
        metadata={
            "name": "TactileWarningStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_warning_strip_contrast: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileWarningStripContrast",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guiding_strip: Optional[bool] = field(
        default=None,
        metadata={
            "name": "TactileGuidingStrip",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    tactile_guiding_strip_status: Optional[TactileGuidingStripStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "TactileGuidingStripStatus",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_flow_per_minute: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumFlowPerMinute",
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
    deck_ref: Optional[DeckRef] = field(
        default=None,
        metadata={
            "name": "DeckRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    deck_level_ref: Optional[DeckLevelRef] = field(
        default=None,
        metadata={
            "name": "DeckLevelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_class: Optional[FareClass] = field(
        default=None,
        metadata={
            "name": "FareClass",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    class_of_use_ref: Optional[ClassOfUseRef] = field(
        default=None,
        metadata={
            "name": "ClassOfUseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    check_constraints: Optional[CheckConstraintsRelStructure] = field(
        default=None,
        metadata={
            "name": "checkConstraints",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_places: Optional[EquipmentPlacesRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentPlaces",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    place_equipments: Optional[PlaceEquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "placeEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    local_services: Optional[LocalServicesRelStructure] = field(
        default=None,
        metadata={
            "name": "localServices",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    label: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    from_equipable_space: DeckPathLinkEndStructure = field(
        metadata={
            "name": "FromEquipableSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_equipable_space: DeckPathLinkEndStructure = field(
        metadata={
            "name": "ToEquipableSpace",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
