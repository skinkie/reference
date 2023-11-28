from dataclasses import dataclass, field
from typing import List, Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.fare_scheduled_stop_point_ref import FareScheduledStopPointRef
from netex.journey_part_ref_structure import JourneyPartRefStructure
from netex.scheduled_stop_point_ref import ScheduledStopPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartPositionVersionedChildStructure(VersionedChildStructure):
    """
    Type for JOURNEY PART POSITION.

    :ivar parent_journey_part_ref: Reference to parent of which this is
        part. If given by context does not need to be stated.
    :ivar fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref:
    :ivar position_in_train: Position of JOURNEY PART in TRAIN - from
        specified SCHEDULED STOP POINT until otherwise stated.
    :ivar order: Order of JOURNEY PART  POistion within JOURNEY PART.
    """
    class Meta:
        name = "JourneyPartPosition_VersionedChildStructure"

    parent_journey_part_ref: Optional[JourneyPartRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentJourneyPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_scheduled_stop_point_ref_or_scheduled_stop_point_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "FareScheduledStopPointRef",
                    "type": FareScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledStopPointRef",
                    "type": ScheduledStopPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    position_in_train: int = field(
        metadata={
            "name": "PositionInTrain",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
