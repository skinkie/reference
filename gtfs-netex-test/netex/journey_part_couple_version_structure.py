from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.block_ref import BlockRef
from netex.journey_part_ref_structure import JourneyPartRefStructure
from netex.journey_part_refs_rel_structure import JourneyPartRefsRelStructure
from netex.multilingual_string import MultilingualString
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.train_block_ref import TrainBlockRef
from netex.train_number_ref import TrainNumberRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartCoupleVersionStructure(DataManagedObjectStructure):
    """
    Type for a JOURNEY PART COUPLE.

    :ivar description: Time of Departure.
    :ivar start_time: Start time of JOURNEY PART.
    :ivar start_time_day_offset: Number of days after journey start time
        that start time is.
    :ivar end_time: End time of JOURNEY PART.
    :ivar end_time_day_offset: Number of days after journey start time
        that end time is.
    :ivar from_stop_point_ref: Point at which this  JOURNEY PART starts.
    :ivar to_stop_point_ref: Point at which this JOURNEY PART ends.
    :ivar main_part_ref: Main Journey JOURNEY PART of coupling.
    :ivar train_block_ref_or_block_ref:
    :ivar journey_parts: JOURNEY PARTs in JOURNEY PART COUPLE.
    :ivar train_number_ref:
    :ivar order: Order of JOURNEY PART COUPLE. +v1.1
    """
    class Meta:
        name = "JourneyPartCouple_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: XmlTime = field(
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    start_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "StartTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: XmlTime = field(
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    end_time_day_offset: Optional[int] = field(
        default=None,
        metadata={
            "name": "EndTimeDayOffset",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    from_stop_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    to_stop_point_ref: ScheduledStopPointRefStructure = field(
        metadata={
            "name": "ToStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    main_part_ref: JourneyPartRefStructure = field(
        metadata={
            "name": "MainPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    train_block_ref_or_block_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockRef",
                    "type": TrainBlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockRef",
                    "type": BlockRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    journey_parts: Optional[JourneyPartRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    train_number_ref: Optional[TrainNumberRef] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
