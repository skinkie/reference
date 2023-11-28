from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration, XmlTime
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.block_parts_rel_structure import BlockPartsRelStructure
from netex.compound_train_ref import CompoundTrainRef
from netex.courses_of_journeys_rel_structure import CoursesOfJourneysRelStructure
from netex.day_type_refs_rel_structure import DayTypeRefsRelStructure
from netex.journey_refs_rel_structure import JourneyRefsRelStructure
from netex.multilingual_string import MultilingualString
from netex.point_ref_structure import PointRefStructure
from netex.private_code import PrivateCode
from netex.relief_opportunities_rel_structure import ReliefOpportunitiesRelStructure
from netex.train_ref import TrainRef
from netex.vehicle_service_part_ref import VehicleServicePartRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class BlockVersionStructure(DataManagedObjectStructure):
    """
    Type for BLOCK.

    :ivar name: Name of BLOCK.
    :ivar description: Description of BLOCK.
    :ivar private_code:
    :ivar preparation_duration: Time to complete BLOCK.
    :ivar start_time: Start time of BLOCK- In principle this can be
        derived from the Start time of the first journey and the
        preparation duration but may be stated  explicitly as well.
    :ivar start_time_day_offset: Day offset of Start time from current
        OPERATING DAY.
    :ivar finishing_duration: Time to complete BLOCK.
    :ivar end_time: End time of BLOCK. In principle this can be derived
        from the Start time of the last journey and the finishing
        duration but may be stated  explicitly as well.
    :ivar end_time_day_offset: Day offset of end time from current
        OPERATING DAY.
    :ivar day_types: DAY TYPEs for BLOCK.
    :ivar vehicle_service_part_ref:
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    :ivar start_point_ref: Point at which BLOCK starts Should be a
        PARKING POINT but might be of unknown type.
    :ivar end_point_ref: Point at which BLOCK ends Point at which BLOCK
        starts Should be a PARKING POINT but might be of unknown type.
    :ivar journeys: JOURNEYS making up BLOCK.
    :ivar courses_of_journeys: Runs in BLOCK PART.
    :ivar block_parts: BLOCK PARTS in BLOCK.
    :ivar relief_opportunities: RELIEF OPPORTUNITIES of a BLOCK-
    """
    class Meta:
        name = "Block_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    preparation_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "PreparationDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    start_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "StartTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    finishing_duration: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "FinishingDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_time: Optional[XmlTime] = field(
        default=None,
        metadata={
            "name": "EndTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
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
    day_types: Optional[DayTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "dayTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    vehicle_service_part_ref: Optional[VehicleServicePartRef] = field(
        default=None,
        metadata={
            "name": "VehicleServicePartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    compound_train_ref_or_train_ref_or_vehicle_type_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CompoundTrainRef",
                    "type": CompoundTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleTypeRef",
                    "type": VehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    start_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[PointRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    journeys: Optional[JourneyRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    courses_of_journeys: Optional[CoursesOfJourneysRelStructure] = field(
        default=None,
        metadata={
            "name": "coursesOfJourneys",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    block_parts: Optional[BlockPartsRelStructure] = field(
        default=None,
        metadata={
            "name": "blockParts",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    relief_opportunities: Optional[ReliefOpportunitiesRelStructure] = field(
        default=None,
        metadata={
            "name": "reliefOpportunities",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
