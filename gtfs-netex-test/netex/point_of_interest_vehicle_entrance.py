from dataclasses import dataclass, field
from netex.point_of_interest_vehicle_entrance_version_structure import PointOfInterestVehicleEntranceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PointOfInterestVehicleEntrance(PointOfInterestVehicleEntranceVersionStructure):
    """
    A VEHICLE ENTRANCE to a POINT OF INTEREST.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
