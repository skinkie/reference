from dataclasses import dataclass, field
from typing import Any

from .abstract_service_journey_interchange_structure import AbstractServiceJourneyInterchangeStructure
from .distributor_departure_stop_ref import DistributorDepartureStopRef
from .distributor_ref import DistributorRef
from .feeder_arrival_stop_ref import FeederArrivalStopRef
from .feeder_ref import FeederRef
from .interchange_ref import InterchangeRef
from .reason_for_removal import ReasonForRemoval

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class RemovedServiceJourneyInterchangeStructure(AbstractServiceJourneyInterchangeStructure):
    interchange_code: Any = field(
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
    stay_seated: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    guaranteed: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    advertised: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    standard_wait_time: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    maximum_wait_time: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    maximum_automatic_wait_time: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    standard_transfer_time: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    minimum_transfer_time: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    maximum_transfer_time: Any = field(
        init=False,
        metadata={
            "type": "Ignore",
        },
    )
    interchange_ref: InterchangeRef = field(
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    reason_for_removal: ReasonForRemoval = field(
        metadata={
            "name": "ReasonForRemoval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
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
