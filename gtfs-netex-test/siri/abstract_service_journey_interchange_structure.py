from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .aimed_arrival_time_of_feeder import AimedArrivalTimeOfFeeder
from .aimed_departure_time_of_distributor import AimedDepartureTimeOfDistributor
from .connection_link_ref import ConnectionLinkRef
from .distributor_departure_stop_ref import DistributorDepartureStopRef
from .distributor_ref import DistributorRef
from .distributor_stop_order import DistributorStopOrder
from .distributor_visit_number import DistributorVisitNumber
from .extensions_1 import Extensions1
from .extra_interchange import ExtraInterchange
from .feeder_arrival_stop_ref import FeederArrivalStopRef
from .feeder_ref import FeederRef
from .feeder_stop_order import FeederStopOrder
from .feeder_visit_number import FeederVisitNumber
from .interchange_code import InterchangeCode
from .interchange_ref import InterchangeRef
from .reason_for_removal import ReasonForRemoval

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractServiceJourneyInterchangeStructure:
    interchange_code_or_interchange_ref: Optional[Union[InterchangeCode, InterchangeRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InterchangeCode",
                    "type": InterchangeCode,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "InterchangeRef",
                    "type": InterchangeRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
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
    extra_interchange_or_cancellation: Optional[Union[ExtraInterchange, bool]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ExtraInterchange",
                    "type": ExtraInterchange,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Cancellation",
                    "type": bool,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    reason_for_removal: Optional[ReasonForRemoval] = field(
        default=None,
        metadata={
            "name": "ReasonForRemoval",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_ref: Optional[FeederRef] = field(
        default=None,
        metadata={
            "name": "FeederRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_arrival_stop_ref: Optional[FeederArrivalStopRef] = field(
        default=None,
        metadata={
            "name": "FeederArrivalStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_visit_number: Optional[FeederVisitNumber] = field(
        default=None,
        metadata={
            "name": "FeederVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_stop_order: Optional[FeederStopOrder] = field(
        default=None,
        metadata={
            "name": "FeederStopOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_arrival_time_of_feeder: Optional[AimedArrivalTimeOfFeeder] = field(
        default=None,
        metadata={
            "name": "AimedArrivalTimeOfFeeder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_ref: Optional[DistributorRef] = field(
        default=None,
        metadata={
            "name": "DistributorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_departure_stop_ref: Optional[DistributorDepartureStopRef] = field(
        default=None,
        metadata={
            "name": "DistributorDepartureStopRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_visit_number: Optional[DistributorVisitNumber] = field(
        default=None,
        metadata={
            "name": "DistributorVisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_stop_order: Optional[DistributorStopOrder] = field(
        default=None,
        metadata={
            "name": "DistributorStopOrder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    aimed_departure_time_of_distributor: Optional[AimedDepartureTimeOfDistributor] = field(
        default=None,
        metadata={
            "name": "AimedDepartureTimeOfDistributor",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stay_seated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "StaySeated",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    guaranteed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Guaranteed",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    advertised: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Advertised",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
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
