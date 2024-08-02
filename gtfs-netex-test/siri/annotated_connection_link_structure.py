from dataclasses import dataclass, field
from typing import List, Optional

from .connection_link_ref_structure import ConnectionLinkRefStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AnnotatedConnectionLinkStructure:
    connection_link_ref: ConnectionLinkRefStructure = field(
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    feeder_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FeederStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_stop_point_ref: Optional[StopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "DistributorStopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    monitored: Optional[bool] = field(
        default=None,
        metadata={
            "name": "Monitored",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_link_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    feeder_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "FeederStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    distributor_stop_point_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DistributorStopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    url: Optional[str] = field(
        default=None,
        metadata={
            "name": "Url",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
