from dataclasses import dataclass, field
from typing import Optional
from netex.point_in_journey_pattern_versioned_child_structure import PointInJourneyPatternVersionedChildStructure
from netex.scheduled_stop_point_view import ScheduledStopPointView
from netex.series_presentation_enumeration import SeriesPresentationEnumeration

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FarePointInPatternVersionedChildStructure(PointInJourneyPatternVersionedChildStructure):
    """
    Type for FARE POINT IN JOURNEY PATTERN.

    :ivar scheduled_stop_point_view:
    :ivar abridgement_ranking: Relative ranking for omitting this FARE
        POINT IN JOURNEY PATTERN when presenting an abridged verson of
        the series. 1=High.- omit first.
    :ivar presentation_position: Relative positiion to be given to name
        of point when presenting it in a list of stops (Left, right
        etc). Allows TAP itinerary to be constructed.
    :ivar is_forbidden: Whether use of  fare point is forbidden- can be
        used to  explicitly exclude certain routings  Default is false.
    :ivar interchange_allowed: Whether interchange to another service is
        allowed at this point. Default is true.
    :ivar is_fare_stage: Whether stop is considered to be a fare stage
    """
    class Meta:
        name = "FarePointInPattern_VersionedChildStructure"

    scheduled_stop_point_view: Optional[ScheduledStopPointView] = field(
        default=None,
        metadata={
            "name": "ScheduledStopPointView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    abridgement_ranking: Optional[int] = field(
        default=None,
        metadata={
            "name": "AbridgementRanking",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    presentation_position: Optional[SeriesPresentationEnumeration] = field(
        default=None,
        metadata={
            "name": "PresentationPosition",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_forbidden: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsForbidden",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    interchange_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "InterchangeAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    is_fare_stage: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsFareStage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
