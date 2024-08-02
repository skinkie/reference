from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .accessibility_needs_filter_structure import AccessibilityNeedsFilterStructure
from .connection_link_ref import ConnectionLinkRef
from .extensions_1 import Extensions1
from .facility_ref import FacilityRef
from .feature_ref import FeatureRef
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .include_translations import IncludeTranslations
from .interchange_ref import InterchangeRef
from .line_ref import LineRef
from .site_ref import SiteRef
from .stop_place_component_ref_structure import StopPlaceComponentRefStructure
from .stop_place_ref_structure import StopPlaceRefStructure
from .stop_point_ref import StopPointRef
from .vehicle_journey_ref import VehicleJourneyRef
from .vehicle_ref import VehicleRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FacilityMonitoringRequestStructure(AbstractFunctionalServiceRequestStructure):
    preview_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreviewInterval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    start_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    facility_ref: List[FacilityRef] = field(
        default_factory=list,
        metadata={
            "name": "FacilityRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feature_ref: List[FeatureRef] = field(
        default_factory=list,
        metadata={
            "name": "FeatureRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRef] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: Optional[ConnectionLinkRef] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    framed_vehicle_journey_ref_or_vehicle_journey_ref: Optional[Union[FramedVehicleJourneyRefStructure, VehicleJourneyRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FramedVehicleJourneyRef",
                    "type": FramedVehicleJourneyRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "VehicleJourneyRef",
                    "type": VehicleJourneyRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    interchange_ref: Optional[InterchangeRef] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    vehicle_ref: Optional[VehicleRef] = field(
        default=None,
        metadata={
            "name": "VehicleRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_ref: Optional[StopPlaceRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_place_component_ref: Optional[StopPlaceComponentRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPlaceComponentRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    site_ref: Optional[SiteRef] = field(
        default=None,
        metadata={
            "name": "SiteRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    accessibility_needs_filter: List[AccessibilityNeedsFilterStructure] = field(
        default_factory=list,
        metadata={
            "name": "AccessibilityNeedsFilter",
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
    maximum_number_of_facility_conditions: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfFacilityConditions",
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
