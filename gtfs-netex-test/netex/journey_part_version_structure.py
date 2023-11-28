from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.block_part_ref import BlockPartRef
from netex.journey_part_couple_ref import JourneyPartCoupleRef
from netex.journey_part_positions_rel_structure import JourneyPartPositionsRelStructure
from netex.journey_part_ref_structure import JourneyPartRefStructure
from netex.multilingual_string import MultilingualString
from netex.purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from netex.train_block_part_ref import TrainBlockPartRef
from netex.train_number_ref import TrainNumberRef
from netex.vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class JourneyPartVersionStructure(DataManagedObjectStructure):
    """
    Type for JOURNEY PART.

    :ivar description: Description of JOURNEY PART.
    :ivar parent_journey_ref: Reference to parent of which this is part.
        If given by context does not need to be stated.
    :ivar main_part_ref: Main JOURNEY PART for journey.
    :ivar journey_part_couple_ref:
    :ivar train_number_ref:
    :ivar train_block_part_ref_or_block_part_ref:
    :ivar from_stop_point_ref: Point at which this JOURNEY PART starts.
    :ivar to_stop_point_ref: Point at which this JOURNEY PART ends.
    :ivar start_time: Start time of JOURNEY PART.
    :ivar start_time_day_offset: Number of days after journey start time
        that start time is.
    :ivar end_time: End time of JOURNEY PART.
    :ivar end_time_day_offset: Number of days after journey start time
        that end time is.
    :ivar vehicle_orientation: Orientation of the vehicle carrying out
        the JOURNEY PART compared to the definition of the corresponding
        VEHICLE TYPE. true for forward.
    :ivar purpose_of_journey_partition_ref:
    :ivar facilities: Facilities available during JOURNEY PART.
    :ivar journey_part_positions: Positions in Train of JOURNEY PART.
    :ivar order: Order of JOURNEY PART  within JOURNEY.
    """
    class Meta:
        name = "JourneyPart_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parent_journey_ref: Optional[VehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    main_part_ref: Optional[JourneyPartRefStructure] = field(
        default=None,
        metadata={
            "name": "MainPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_couple_ref: Optional[JourneyPartCoupleRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartCoupleRef",
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
    train_block_part_ref_or_block_part_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainBlockPartRef",
                    "type": TrainBlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "BlockPartRef",
                    "type": BlockPartRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    from_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToStopPointRef",
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
    vehicle_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purpose_of_journey_partition_ref: Optional[PurposeOfJourneyPartitionRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfJourneyPartitionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journey_part_positions: Optional[JourneyPartPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPartPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
