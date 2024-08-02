from dataclasses import dataclass, field
from typing import List, Optional

from xsdata.models.datatype import XmlDateTime

from .abstract_identified_item_structure import AbstractIdentifiedItemStructure
from .connection_link_ref_structure import ConnectionLinkRefStructure
from .interchange_ref_structure import InterchangeRefStructure
from .order import Order
from .stop_point_name import StopPointName
from .stop_point_ref import StopPointRef
from .visit_number import VisitNumber

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class AbstractFeederItemStructure(AbstractIdentifiedItemStructure):
    valid_until_time: Optional[XmlDateTime] = field(
        default=None,
        metadata={
            "name": "ValidUntilTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
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
    stop_point_ref: Optional[StopPointRef] = field(
        default=None,
        metadata={
            "name": "StopPointRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    visit_number: Optional[VisitNumber] = field(
        default=None,
        metadata={
            "name": "VisitNumber",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: Optional[Order] = field(
        default=None,
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    stop_point_name: List[StopPointName] = field(
        default_factory=list,
        metadata={
            "name": "StopPointName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
