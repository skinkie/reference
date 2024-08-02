from dataclasses import dataclass, field
from typing import List, Optional, Union

from .destination_ref import DestinationRef
from .natural_language_place_name_structure import NaturalLanguagePlaceNameStructure
from .natural_language_string_structure import NaturalLanguageStringStructure
from .origin_ref import OriginRef
from .passage_between_trains_structure import PassageBetweenTrainsStructure
from .train import Train
from .train_ref import TrainRef
from .via_name_structure import ViaNameStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class TrainInCompoundTrainStructure:
    train_in_compound_train_code: Optional[str] = field(
        default=None,
        metadata={
            "name": "TrainInCompoundTrainCode",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    order: int = field(
        metadata={
            "name": "Order",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    label: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Label",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    description: Optional[NaturalLanguageStringStructure] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_ref_or_train: Optional[Union[TrainRef, Train]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "TrainRef",
                    "type": TrainRef,
                    "namespace": "http://www.siri.org.uk/siri",
                },
                {
                    "name": "Train",
                    "type": Train,
                    "namespace": "http://www.siri.org.uk/siri",
                },
            ),
        },
    )
    origin_ref: Optional[OriginRef] = field(
        default=None,
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_display_at_origin: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationDisplayAtOrigin",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    via: List[ViaNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "Via",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_ref: Optional[DestinationRef] = field(
        default=None,
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_name: List[NaturalLanguageStringStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    destination_short_name: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "DestinationShortName",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    origin_display_at_destination: List[NaturalLanguagePlaceNameStructure] = field(
        default_factory=list,
        metadata={
            "name": "OriginDisplayAtDestination",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    reversed_orientation: Optional[bool] = field(
        default=None,
        metadata={
            "name": "ReversedOrientation",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    passages: Optional["TrainInCompoundTrainStructure.Passages"] = field(
        default=None,
        metadata={
            "name": "Passages",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )

    @dataclass(kw_only=True)
    class Passages:
        passage_between_trains: List[PassageBetweenTrainsStructure] = field(
            default_factory=list,
            metadata={
                "name": "PassageBetweenTrains",
                "type": "Element",
                "namespace": "http://www.siri.org.uk/siri",
                "min_occurs": 1,
                "max_occurs": 2,
            },
        )
