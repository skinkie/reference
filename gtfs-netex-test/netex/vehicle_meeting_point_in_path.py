from dataclasses import dataclass, field
from netex.vehicle_meeting_point_in_path_version_structure import VehicleMeetingPointInPathVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleMeetingPointInPath(VehicleMeetingPointInPathVersionStructure):
    """The planned movement of a public transport vehicle on a DAY TYPE from the
    start point to the end point of a JOURNEY PATTERN on a specified ROUTE.

    +v1.2.2

    :ivar id: Identifier of ENTITY.
    :ivar order: Order of POINT in sequence.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
