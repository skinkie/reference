from dataclasses import dataclass, field
from typing import List, Optional

from .abstract_item_structure import AbstractItemStructure
from .connection_link_ref_structure import ConnectionLinkRefStructure
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .interchange_journey_structure import InterchangeJourneyStructure
from .interchange_ref_structure import InterchangeRefStructure
from .stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractDistributorItemStructure(AbstractItemStructure):
    interchange_ref: Optional[InterchangeRefStructure] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_ref: ConnectionLinkRefStructure = field(
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_visit_number: Optional[int] = field(
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
    distributor_journey: InterchangeJourneyStructure = field(
        metadata={
            "name": "DistributorJourney",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    feeder_vehicle_journey_ref: List[FramedVehicleJourneyRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "FeederVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
