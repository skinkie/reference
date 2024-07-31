from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlTime

from .block_part_ref import BlockPartRef
from .entity_in_version_structure import DataManagedObjectStructure
from .journey_part_couple_ref import JourneyPartCoupleRef
from .journey_part_positions_rel_structure import JourneyPartPositionsRelStructure
from .journey_part_ref_structure import JourneyPartRefStructure
from .multilingual_string import MultilingualString
from .occupancy_view_rel_structure import OccupancyViewRelStructure
from .purpose_of_journey_partition_ref import PurposeOfJourneyPartitionRef
from .scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from .service_facility_sets_rel_structure import ServiceFacilitySetsRelStructure
from .train_block_part_ref import TrainBlockPartRef
from .train_number_ref import TrainNumberRef
from .type_of_product_category_ref import TypeOfProductCategoryRef
from .vehicle_journey_ref_structure import VehicleJourneyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class JourneyPartVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "JourneyPart_VersionStructure"

    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parent_journey_ref: Optional[VehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "ParentJourneyRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_part_ref: Optional[JourneyPartRefStructure] = field(
        default=None,
        metadata={
            "name": "MainPartRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_couple_ref: Optional[JourneyPartCoupleRef] = field(
        default=None,
        metadata={
            "name": "JourneyPartCoupleRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    train_number_ref: Optional[TrainNumberRef] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    block_part_ref: Optional[Union[TrainBlockPartRef, BlockPartRef]] = field(
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
        },
    )
    from_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    to_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
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
        },
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
        },
    )
    vehicle_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "VehicleOrientation",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purpose_of_journey_partition_ref: Optional[PurposeOfJourneyPartitionRef] = field(
        default=None,
        metadata={
            "name": "PurposeOfJourneyPartitionRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    journey_part_positions: Optional[JourneyPartPositionsRelStructure] = field(
        default=None,
        metadata={
            "name": "journeyPartPositions",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    occupancies: Optional[OccupancyViewRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_product_category_ref: Optional[TypeOfProductCategoryRef] = field(
        default=None,
        metadata={
            "name": "TypeOfProductCategoryRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
