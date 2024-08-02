from dataclasses import dataclass, field
from typing import List, Optional

from .affected_connection_link_structure import AffectedConnectionLinkStructure
from .dated_vehicle_journey_ref_structure import DatedVehicleJourneyRefStructure
from .extensions_1 import Extensions1
from .interchange_ref_structure import InterchangeRefStructure
from .interchange_status_type import InterchangeStatusType
from .natural_language_string_structure import NaturalLanguageStringStructure
from .stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedInterchangeStructure:
    interchange_ref: Optional[InterchangeRefStructure] = field(
        default=None,
        metadata={
            "name": "InterchangeRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "InterchangeStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "InterchangeStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connecting_vehicle_journey_ref: Optional[DatedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "ConnectingVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    interchange_status_type: Optional[InterchangeStatusType] = field(
        default=None,
        metadata={
            "name": "InterchangeStatusType",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link: List[AffectedConnectionLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLink",
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
