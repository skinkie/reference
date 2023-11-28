from dataclasses import dataclass, field
from typing import Optional
from netex.authority_ref import AuthorityRef
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.operator_ref import OperatorRef
from netex.transport_type_refs_rel_structure import TransportTypeRefsRelStructure
from netex.type_of_fleet_ref import TypeOfFleetRef
from netex.vehicles_rel_structure import VehiclesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FleetVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for a  FLEET.

    :ivar members: VEHICLEs in FLEET,
    :ivar authority_ref_or_operator_ref:
    :ivar type_of_fleet_ref:
    :ivar transport_types: VEHICLE TYPEs used in FLEET..
    """
    class Meta:
        name = "Fleet_VersionStructure"

    members: Optional[VehiclesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    authority_ref_or_operator_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "AuthorityRef",
                    "type": AuthorityRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "OperatorRef",
                    "type": OperatorRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
    type_of_fleet_ref: Optional[TypeOfFleetRef] = field(
        default=None,
        metadata={
            "name": "TypeOfFleetRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_types: Optional[TransportTypeRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "transportTypes",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
