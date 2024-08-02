from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .abstract_identified_item_structure import AbstractIdentifiedItemStructure
from .extensions_1 import Extensions1
from .monitored_vehicle_journey_structure import MonitoredVehicleJourneyStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .progress_between_stops_structure import ProgressBetweenStopsStructure
from .vehicle_monitoring_ref_structure import VehicleMonitoringRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class VehicleActivityStructure(AbstractIdentifiedItemStructure):
    valid_until_time: XmlDateTime = field(
        metadata={
            "name": "ValidUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    vehicle_monitoring_ref: Optional[VehicleMonitoringRefStructure] = field(
        default=None,
        metadata={
            "name": "VehicleMonitoringRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitoring_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "MonitoringName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    progress_between_stops: Optional[ProgressBetweenStopsStructure] = field(
        default=None,
        metadata={
            "name": "ProgressBetweenStops",
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
    vehicle_activity_note: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "VehicleActivityNote",
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
