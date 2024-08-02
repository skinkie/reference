from dataclasses import dataclass, field
from typing import Optional

from .dated_vehicle_journey_indirect_ref_structure import DatedVehicleJourneyIndirectRefStructure
from .framed_vehicle_journey_ref_structure import FramedVehicleJourneyRefStructure
from .line_ref_structure import LineRefStructure
from .operator_ref_structure import OperatorRefStructure
from .participant_ref_structure import ParticipantRefStructure
from .train_number_ref_structure import TrainNumberRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class ConnectingJourneyRefStructure:
    framed_vehicle_journey_ref: Optional[FramedVehicleJourneyRefStructure] = field(
        default=None,
        metadata={
            "name": "FramedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    dated_vehicle_journey_indirect_ref: Optional[DatedVehicleJourneyIndirectRefStructure] = field(
        default=None,
        metadata={
            "name": "DatedVehicleJourneyIndirectRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "LineRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    train_number_ref: Optional[TrainNumberRefStructure] = field(
        default=None,
        metadata={
            "name": "TrainNumberRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    operator_ref: Optional[OperatorRefStructure] = field(
        default=None,
        metadata={
            "name": "OperatorRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
    participant_ref: Optional[ParticipantRefStructure] = field(
        default=None,
        metadata={
            "name": "ParticipantRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
        },
    )
