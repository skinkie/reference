from dataclasses import dataclass, field
from typing import List, Optional, Union

from xsdata.models.datatype import XmlDuration

from .abstract_functional_service_request_structure import AbstractFunctionalServiceRequestStructure
from .connecting_journey_filter_structure import ConnectingJourneyFilterStructure
from .connecting_time_filter_structure import ConnectingTimeFilterStructure
from .connection_link_ref_structure import ConnectionLinkRefStructure
from .connection_monitoring_detail_enumeration import ConnectionMonitoringDetailEnumeration
from .extensions_1 import Extensions1
from .include_translations import IncludeTranslations

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectionMonitoringRequestStructure(AbstractFunctionalServiceRequestStructure):
    preview_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreviewInterval",
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
    connecting_time_filter_or_connecting_journey_filter: List[Union[ConnectingTimeFilterStructure, ConnectingJourneyFilterStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ConnectingTimeFilter",
                    "type": ConnectingTimeFilterStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectingJourneyFilter",
                    "type": ConnectingJourneyFilterStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    language: List[str] = field(
        default_factory=list,
        metadata={
            "name": "Language",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    include_translations: Optional[IncludeTranslations] = field(
        default=None,
        metadata={
            "name": "IncludeTranslations",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_monitoring_detail_level: Optional[ConnectionMonitoringDetailEnumeration] = field(
        default=None,
        metadata={
            "name": "ConnectionMonitoringDetailLevel",
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
    version: str = field(
        default="2.1",
        metadata={
            "type": "Attribute",
        },
    )
