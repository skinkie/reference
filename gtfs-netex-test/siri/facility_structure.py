from dataclasses import dataclass, field
from typing import List, Optional

from .accessibility_assessment_structure import AccessibilityAssessmentStructure
from .all_facilities_feature_structure import AllFacilitiesFeatureStructure
from .audible_signals_available import AudibleSignalsAvailable
from .escalator_free_access import EscalatorFreeAccess
from .extensions_1 import Extensions1
from .facility_category_enumeration import FacilityCategoryEnumeration
from .facility_location_structure import FacilityLocationStructure
from .lift_free_access import LiftFreeAccess
from .monitoring_validity_condition_structure import MonitoringValidityConditionStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .organisation_ref_structure import OrganisationRefStructure
from .step_free_access import StepFreeAccess
from .suitability_structure import SuitabilityStructure
from .visual_signs_available import VisualSignsAvailable
from .wheelchair_access import WheelchairAccess

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityStructure:
    facility_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "FacilityCode",
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
    facility_class: List[FacilityCategoryEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "FacilityClass",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    features: Optional["FacilityStructure.Features"] = field(
        default=None,
        metadata={
            "name": "Features",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    owner_ref: Optional[OrganisationRefStructure] = field(
        default=None,
        metadata={
            "name": "OwnerRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    owner_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "OwnerName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    validity_condition: Optional[MonitoringValidityConditionStructure] = field(
        default=None,
        metadata={
            "name": "ValidityCondition",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_location: Optional[FacilityLocationStructure] = field(
        default=None,
        metadata={
            "name": "FacilityLocation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    limitations: Optional["FacilityStructure.Limitations"] = field(
        default=None,
        metadata={
            "name": "Limitations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    suitabilities: Optional["FacilityStructure.Suitabilities"] = field(
        default=None,
        metadata={
            "name": "Suitabilities",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_assessment: Optional[AccessibilityAssessmentStructure] = field(
        default=None,
        metadata={
            "name": "AccessibilityAssessment",
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
    class Features:
        feature: List[AllFacilitiesFeatureStructure] = field(
            default_factory=list,
            metadata={
                "name": "Feature",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )

    @dataclass(kw_only=True)
    class Limitations:
        wheelchair_access: WheelchairAccess = field(
            metadata={
                "name": "WheelchairAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
                "required": True,
            }
        )
        step_free_access: Optional[StepFreeAccess] = field(
            default=None,
            metadata={
                "name": "StepFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        escalator_free_access: Optional[EscalatorFreeAccess] = field(
            default=None,
            metadata={
                "name": "EscalatorFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        lift_free_access: Optional[LiftFreeAccess] = field(
            default=None,
            metadata={
                "name": "LiftFreeAccess",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        audible_signals_available: Optional[AudibleSignalsAvailable] = field(
            default=None,
            metadata={
                "name": "AudibleSignalsAvailable",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )
        visual_signs_available: Optional[VisualSignsAvailable] = field(
            default=None,
            metadata={
                "name": "VisualSignsAvailable",
                "type": "Element",
                "namespace": "http://www.ifopt.org.uk/acsb",
            },
        )

    @dataclass(kw_only=True)
    class Suitabilities:
        suitability: List[SuitabilityStructure] = field(
            default_factory=list,
            metadata={
                "name": "Suitability",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
            },
        )
