from dataclasses import dataclass, field
from typing import Any

from .abstract_service_journey_interchange_structure import AbstractServiceJourneyInterchangeStructure
from .distributor_departure_stop_ref import DistributorDepartureStopRef
from .distributor_ref import DistributorRef
from .feeder_arrival_stop_ref import FeederArrivalStopRef
from .feeder_ref import FeederRef
from .feeder_visit_number import FeederVisitNumber

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ToServiceJourneyInterchangeStructure(AbstractServiceJourneyInterchangeStructure):
    interchange_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    extra_interchange_or_cancellation: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    reason_for_removal: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    feeder_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    feeder_arrival_stop_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    feeder_visit_number: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    distributor_ref: DistributorRef = field(
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    distributor_departure_stop_ref: DistributorDepartureStopRef = field(
        metadata={
            "name": "DistributorDepartureStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
