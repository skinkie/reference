from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.block_parts_rel_structure import BlockPartsRelStructure
from netex.compound_train_ref import CompoundTrainRef
from netex.multilingual_string import MultilingualString
from netex.timing_point_in_journey_pattern_ref_structure import TimingPointInJourneyPatternRefStructure
from netex.train_ref import TrainRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CompoundBlockStructure(DataManagedObjectStructure):
    """
    Type for COMPOUND BLOCK.

    :ivar name: Name of COMPOUND BLOCK.
    :ivar description: Description of COMPOUND BLOCK.
    :ivar compound_train_ref_or_train_ref_or_vehicle_type_ref:
    :ivar start_point_ref: Staring timing point of COMPOUND BLOCK.
    :ivar end_point_ref: Ending timing point of COMPOUND BLOCK.
    :ivar parts: BLOCK PARTs which make up COMPOUND BLOCK.
    """
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
    start_point_ref: Optional[TimingPointInJourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "StartPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    end_point_ref: Optional[TimingPointInJourneyPatternRefStructure] = field(
        default=None,
        metadata={
            "name": "EndPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    parts: Optional[BlockPartsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
