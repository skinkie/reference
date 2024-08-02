from dataclasses import dataclass, field
from typing import List, Optional

from .accessibility_assessment_structure import AccessibilityAssessmentStructure
from .block_ref_structure import BlockRefStructure
from .course_of_journey_ref_structure import CourseOfJourneyRefStructure
from .extensions_1 import Extensions1
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .location_structure import LocationStructure
from .operator_ref_structure import OperatorRefStructure
from .product_category_ref_structure import ProductCategoryRefStructure
from .service_feature_ref import ServiceFeatureRef
from .train_block_part_structure import TrainBlockPartStructure
from .vehicle_feature_ref_structure import VehicleFeatureRefStructure
from .vehicle_ref_structure import VehicleRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedVehicleStructure:
    vehicle_ref: VehicleRefStructure = field(
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    vehicle_registration_number_plate: List[str] = field(
        default_factory=list,
        metadata={
            "name": "VehicleRegistrationNumberPlate",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    phone_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "PhoneNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    ipaddress: Optional[str] = field(
        default=None,
        metadata={
            "name": "IPAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    radio_address: Optional[str] = field(
        default=None,
        metadata={
            "name": "RadioAddress",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "Location",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    current_location: Optional[LocationStructure] = field(
        default=None,
        metadata={
            "name": "CurrentLocation",
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
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    product_category_ref: Optional[ProductCategoryRefStructure] = field(
        default=None,
        metadata={
            "name": "ProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    service_feature_ref: List[ServiceFeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "ServiceFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_feature_ref: List[VehicleFeatureRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleFeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_block_part: List[TrainBlockPartStructure] = field(
        default_factory=list,
        metadata={
            "name": "TrainBlockPart",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    block_ref: Optional[BlockRefStructure] = field(
        default=None,
        metadata={
            "name": "BlockRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    course_of_journey_ref: Optional[CourseOfJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "CourseOfJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    in_congestion: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InCongestion",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    in_panic: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InPanic",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    headway_service: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HeadwayService",
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
