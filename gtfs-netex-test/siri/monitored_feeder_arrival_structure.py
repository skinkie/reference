from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDateTime

from .abstract_feeder_item_structure import AbstractFeederItemStructure
from .aimed_arrival_time import AimedArrivalTime
from .arrival_platform_name import ArrivalPlatformName
from .clear_down_ref_structure import ClearDownRefStructure
from .extensions_1 import Extensions1
from .interchange_journey_structure import InterchangeJourneyStructure
from .vehicle_at_stop import VehicleAtStop

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class MonitoredFeederArrivalStructure(AbstractFeederItemStructure):
    clear_down_ref: Optional[ClearDownRefStructure] = field(
        default=None,
        metadata={
            "name": "ClearDownRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_journey: InterchangeJourneyStructure = field(
        metadata={
            "name": "FeederJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    vehicle_at_stop: Optional[VehicleAtStop] = field(
        default=None,
        metadata={
            "name": "VehicleAtStop",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    number_of_transfer_passengers: Optional[int] = field(
        default=None,
        metadata={
            "name": "NumberOfTransferPassengers",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time: Optional[AimedArrivalTime] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_arrival_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    arrival_platform_name: Optional[ArrivalPlatformName] = field(
        default=None,
        metadata={
            "name": "ArrivalPlatformName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    suggested_wait_decision_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "SuggestedWaitDecisionTime",
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
