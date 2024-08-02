from dataclasses import dataclass, field
from typing import ForwardRef, List, Optional, Union

from xsdata.models.datatype import XmlDateTime, XmlDuration

from .connecting_journey_ref_structure import ConnectingJourneyRefStructure
from .connection_link_ref_structure import ConnectionLinkRefStructure
from .empty_type import EmptyType
from .extensions_1 import Extensions1
from .interchange_ref import InterchangeRef
from .interchange_status_enumeration import InterchangeStatusEnumeration
from .stop_point_ref_structure import StopPointRefStructure
from .will_wait_structure import WillWaitStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class EstimatedServiceJourneyInterchangeStructure:
    choice: List[
        Union[
            InterchangeRef,
            str,
            ConnectionLinkRefStructure,
            "EstimatedServiceJourneyInterchangeStructure.FeederJourneyRef",
            "EstimatedServiceJourneyInterchangeStructure.FeederArrivalStopRef",
            "EstimatedServiceJourneyInterchangeStructure.FeederVisitNumber",
            "EstimatedServiceJourneyInterchangeStructure.FeederStopOrder",
            "EstimatedServiceJourneyInterchangeStructure.AimedArrivalTimeOfFeeder",
            "EstimatedServiceJourneyInterchangeStructure.DistributorJourneyRef",
            "EstimatedServiceJourneyInterchangeStructure.DistributorDepartureStopRef",
            "EstimatedServiceJourneyInterchangeStructure.DistributorVisitNumber",
            "EstimatedServiceJourneyInterchangeStructure.DistributorStopOrder",
            "EstimatedServiceJourneyInterchangeStructure.AimedDepartureTimeOfDistributor",
            "EstimatedServiceJourneyInterchangeStructure.StaySeated",
            "EstimatedServiceJourneyInterchangeStructure.Guaranteed",
            "EstimatedServiceJourneyInterchangeStructure.Advertised",
        ]
    ] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "InterchangeRef",
                    "type": InterchangeRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "InterchangeCode",
                    "type": str,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectionLinkRef",
                    "type": ConnectionLinkRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FeederJourneyRef",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.FeederJourneyRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FeederArrivalStopRef",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.FeederArrivalStopRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FeederVisitNumber",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.FeederVisitNumber"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "FeederStopOrder",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.FeederStopOrder"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedArrivalTimeOfFeeder",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.AimedArrivalTimeOfFeeder"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DistributorJourneyRef",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.DistributorJourneyRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DistributorDepartureStopRef",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.DistributorDepartureStopRef"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DistributorVisitNumber",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.DistributorVisitNumber"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DistributorStopOrder",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.DistributorStopOrder"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "AimedDepartureTimeOfDistributor",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.AimedDepartureTimeOfDistributor"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "StaySeated",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.StaySeated"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Guaranteed",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.Guaranteed"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Advertised",
                    "type": ForwardRef("EstimatedServiceJourneyInterchangeStructure.Advertised"),
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
            "max_occurs": 15,
        },
    )
    interchange_status: Optional[InterchangeStatusEnumeration] = field(
        default=None,
        metadata={
            "name": "InterchangeStatus",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    will_not_wait_or_will_wait: Optional[Union[EmptyType, WillWaitStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "WillNotWait",
                    "type": EmptyType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "WillWait",
                    "type": WillWaitStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    expected_arrival_time_of_feeder: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedArrivalTimeOfFeeder",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    expected_departure_time_of_distributor: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ExpectedDepartureTimeOfDistributor",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoring",
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

    @dataclass(kw_only=True)
    class FeederJourneyRef(ConnectingJourneyRefStructure):
        pass

    @dataclass(kw_only=True)
    class FeederArrivalStopRef(StopPointRefStructure):
        pass

    @dataclass(kw_only=True)
    class FeederVisitNumber:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class FeederStopOrder:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class AimedArrivalTimeOfFeeder:
        value: XmlDateTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class DistributorJourneyRef(ConnectingJourneyRefStructure):
        pass

    @dataclass(kw_only=True)
    class DistributorDepartureStopRef(StopPointRefStructure):
        pass

    @dataclass(kw_only=True)
    class DistributorVisitNumber:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class DistributorStopOrder:
        value: int = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class AimedDepartureTimeOfDistributor:
        value: XmlDateTime = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class StaySeated:
        value: bool = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Guaranteed:
        value: bool = field(
            metadata={
                "required": True,
            }
        )

    @dataclass(kw_only=True)
    class Advertised:
        value: bool = field(
            metadata={
                "required": True,
            }
        )
