from dataclasses import dataclass, field

from xsdata.models.datatype import XmlDateTime

from .stop_point_ref_structure import StopPointRefStructure

__NAMESPACE__ = "http://www.siri.org.uk/siri"


@dataclass(kw_only=True)
class DatedVehicleJourneyIndirectRefStructure:
    origin_ref: StopPointRefStructure = field(
        metadata={
            "name": "OriginRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    aimed_departure_time: XmlDateTime = field(
        metadata={
            "name": "AimedDepartureTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    destination_ref: StopPointRefStructure = field(
        metadata={
            "name": "DestinationRef",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
    aimed_arrival_time: XmlDateTime = field(
        metadata={
            "name": "AimedArrivalTime",
            "type": "Element",
            "namespace": "http://www.siri.org.uk/siri",
            "required": True,
        }
    )
