from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate, XmlTime
from netex.authority_ref import AuthorityRef
from netex.day_type_ref import DayTypeRef
from netex.direction_ref import DirectionRef
from netex.fare_day_type_ref import FareDayTypeRef
from netex.flexible_line_ref import FlexibleLineRef
from netex.line_ref import LineRef
from netex.operator_ref import OperatorRef
from netex.timing_point_ref_structure import TimingPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyDesignatorStructure:
    """
    Type for a value reference to a JOURNEY.

    :ivar from_point_ref: Origin of Journey.
    :ivar to_point_ref: Destination of Journey.
    :ivar date: Date of JOURNEY.
    :ivar departure_time: Time of departure of JOURNEY from POINT.
    :ivar departure_day_offset: Daya offset if Time of departure of
        JOURNEY from origin  POINT from current  OPERATING DAY.
    :ivar arrival_time: Time of arrival of JOURNEY at destination POINT.
    :ivar arrival_day_offset: Daya offset if Time of arrival of JOURNEY
        at destination POINT.
    :ivar fare_day_type_ref_or_day_type_ref:
    :ivar authority_ref_or_operator_ref:
    :ivar flexible_line_ref_or_line_ref:
    :ivar direction_ref:
    :ivar alternative_journey_ref: Alternative ID for journey.
    """
    from_point_ref: Optional[TimingPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_point_ref: Optional[TimingPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "Date",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "DepartureTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    departure_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "DepartureDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    arrival_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "ArrivalTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    arrival_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "ArrivalDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_day_type_ref_or_day_type_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareDayTypeRef",
                    "type": FareDayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DayTypeRef",
                    "type": DayTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    authority_ref_or_operator_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    flexible_line_ref_or_line_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FlexibleLineRef",
                    "type": FlexibleLineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "LineRef",
                    "type": LineRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    direction_ref: Optional[DirectionRef] = field(
        default=None,
        metadata={
            "name": "DirectionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    alternative_journey_ref: Optional[str] = field(
        default=None,
        metadata={
            "name": "AlternativeJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
