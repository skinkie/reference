from dataclasses import dataclass, field

from .data_frame_ref_structure import DataFrameRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class FramedVehicleJourneyRefStructure:
    data_frame_ref: DataFrameRefStructure = field(
        metadata={
            "name": "DataFrameRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    dated_vehicle_journey_ref: str = field(
        metadata={
            "name": "DatedVehicleJourneyRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
