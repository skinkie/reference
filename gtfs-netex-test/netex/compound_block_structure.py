from dataclasses import dataclass, field
from typing import Optional, Union

from .block_parts_rel_structure import BlockPartsRelStructure
from .compound_train_ref import CompoundTrainRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .timing_point_in_journey_pattern_ref_structure import TimingPointInJourneyPatternRefStructure
from .train_ref import TrainRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompoundBlockStructure(DataManagedObjectStructure):
    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_type_ref: Optional[Union[CompoundTrainRef, TrainRef, VehicleTypeRef]] = field(
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
        },
    )
    start_point_ref: Optional[TimingPointInJourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    end_point_ref: Optional[TimingPointInJourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    parts: Optional[BlockPartsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
