from dataclasses import dataclass, field
from typing import Optional
from netex.garage_point_ref import GaragePointRef
from netex.garage_refs_rel_structure import GarageRefsRelStructure
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.parking_point_ref import ParkingPointRef
from netex.relief_point_ref import ReliefPointRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CrewBaseVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for CREW BASE.

    :ivar garage_point_ref_or_parking_point_ref_or_relief_point_ref:
    :ivar garages: garages associated with CREW BASe.
    """
    class Meta:
        name = "CrewBase_VersionStructure"

    garage_point_ref_or_parking_point_ref_or_relief_point_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GaragePointRef",
                    "type": GaragePointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ParkingPointRef",
                    "type": ParkingPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ReliefPointRef",
                    "type": ReliefPointRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    garages: Optional[GarageRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
