from dataclasses import dataclass, field
from typing import List, Optional, Union

from .affected_path_link_structure import AffectedPathLinkStructure
from .connection_direction_enumeration import ConnectionDirectionEnumeration
from .connection_link_ref_structure import ConnectionLinkRefStructure
from .empty_type import EmptyType
from .extensions_1 import Extensions1
from .line_ref import LineRef
from .natural_language_string_structure import NaturalLanguageStringStructure
from .published_line_name import PublishedLineName
from .stop_point_ref_structure import StopPointRefStructure
from .zone_ref_structure import ZoneRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AffectedConnectionLinkStructure:
    connection_link_ref: List[ConnectionLinkRefStructure] = field(
        default_factory=list,
        metadata={
            "name": "ConnectionLinkRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    connection_name: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "ConnectionName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    all_lines_or_line_ref_or_published_line_name_or_connecting_stop_point_ref_or_connecting_stop_point_name_or_connecting_zone_ref: List[Union[EmptyType, LineRef, PublishedLineName, StopPointRefStructure, NaturalLanguageStringStructure, ZoneRefStructure]] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AllLines",
                    "type": EmptyType,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "PublishedLineName",
                    "type": PublishedLineName,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectingStopPointRef",
                    "type": StopPointRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectingStopPointName",
                    "type": NaturalLanguageStringStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "ConnectingZoneRef",
                    "type": ZoneRefStructure,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    connection_direction: Optional[ConnectionDirectionEnumeration] = field(
        default=None,
        metadata={
            "name": "ConnectionDirection",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    affected_path_link: List[AffectedPathLinkStructure] = field(
        default_factory=list,
        metadata={
            "name": "AffectedPathLink",
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
