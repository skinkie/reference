from dataclasses import dataclass, field
from typing import Any

from .abstract_service_journey_interchange_structure import AbstractServiceJourneyInterchangeStructure
from .distributor_departure_stop_ref import DistributorDepartureStopRef
from .distributor_ref import DistributorRef
from .distributor_visit_number import DistributorVisitNumber
from .feeder_arrival_stop_ref import FeederArrivalStopRef
from .feeder_ref import FeederRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FromServiceJourneyInterchangeStructure(AbstractServiceJourneyInterchangeStructure):
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
    feeder_ref: FeederRef = field(
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    feeder_arrival_stop_ref: FeederArrivalStopRef = field(
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    distributor_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    distributor_departure_stop_ref: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    distributor_visit_number: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
