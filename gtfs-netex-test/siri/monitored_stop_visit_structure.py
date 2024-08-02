from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .abstract_identified_item_structure import AbstractIdentifiedItemStructure
from .clear_down_ref_structure import ClearDownRefStructure
from .extensions_1 import Extensions1
from .facility_ref_structure import FacilityRefStructure
from .monitored_vehicle_journey_structure import MonitoredVehicleJourneyStructure
from .monitoring_ref_structure import MonitoringRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredStopVisitStructure(AbstractIdentifiedItemStructure):
    valid_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_ref: Optional[MonitoringRefStructure] = field(
        default=None,
        metadata={
            "name": "MonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    clear_down_ref: Optional[ClearDownRefStructure] = field(
        default=None,
        metadata={
            "name": "ClearDownRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored_vehicle_journey: MonitoredVehicleJourneyStructure = field(
        metadata={
            "name": "MonitoredVehicleJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    stop_visit_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "StopVisitNote",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_facility: Optional[FacilityRefStructure] = field(
        default=None,
        metadata={
            "name": "StopFacility",
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
