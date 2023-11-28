from dataclasses import dataclass, field
from typing import Optional
from netex.compound_train_ref import CompoundTrainRef
from netex.infrastructure_link_restriction_version_structure import InfrastructureLinkRestrictionVersionStructure
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.train_ref import TrainRef
from netex.transport_type_ref import TransportTypeRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RestrictedManoeuvreVersionStructure(InfrastructureLinkRestrictionVersionStructure):
    """
    Type for a MANOEUVRE.
    """
    class Meta:
        name = "RestrictedManoeuvre_VersionStructure"

    choice: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SimpleVehicleTypeRef",
                    "type": SimpleVehicleTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
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
                {
                    "name": "TransportTypeRef",
                    "type": TransportTypeRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
