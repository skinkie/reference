from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .stop_point_name import StopPointName
from .stop_point_ref import StopPointRef

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ContextualisedConnectionLinkStructure:
    connection_link_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "ConnectionLinkCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: Optional[StopPointName] = field(
        default=None,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    default_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "DefaultDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    frequent_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FrequentTravellerDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    occasional_traveller_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "OccasionalTravellerDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    impaired_access_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ImpairedAccessDuration",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
