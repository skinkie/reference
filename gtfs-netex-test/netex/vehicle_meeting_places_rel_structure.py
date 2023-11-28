from dataclasses import dataclass, field
from typing import List
from netex.containment_aggregation_structure import ContainmentAggregationStructure
from netex.vehicle_meeting_place_2 import VehicleMeetingPlace2
from netex.vehicle_pooling_meeting_place import VehiclePoolingMeetingPlace

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPlacesRelStructure(ContainmentAggregationStructure):
    """
    Type for a list of references to a VEHICLE MEETING PLACE.
    """
    class Meta:
        name = "vehicleMeetingPlaces_RelStructure"

    vehicle_pooling_meeting_place_or_vehicle_meeting_place: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "VehiclePoolingMeetingPlace",
                    "type": VehiclePoolingMeetingPlace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleMeetingPlace_",
                    "type": VehicleMeetingPlace2,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
