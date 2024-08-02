from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDuration

from .connection_link_ref_structure import ConnectionLinkRefStructure
from .contextualised_connection_link_structure import ContextualisedConnectionLinkStructure
from .dated_vehicle_journey_ref_structure import DatedVehicleJourneyRefStructure
from .distributor_visit_number import DistributorVisitNumber
from .interchange_code import InterchangeCode

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TargetedInterchangeStructure:
    interchange_code: Optional[InterchangeCode] = field(
        default=None,
        metadata={
            "name": "InterchangeCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_vehicle_journey_ref: DatedVehicleJourneyRefStructure = field(
        metadata={
            "name": "DistributorVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    distributor_connection_link_ref_or_distributor_connection_link: Optional[Union[ConnectionLinkRefStructure, ContextualisedConnectionLinkStructure]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistributorConnectionLinkRef",
                    "type": ConnectionLinkRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "DistributorConnectionLink",
                    "type": ContextualisedConnectionLinkStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
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
    distributor_order: Optional[int] = field(
        default=None,
        metadata={
            "name": "DistributorOrder",
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
