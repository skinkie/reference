from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.car_model_profile_ref import CarModelProfileRef
from netex.compound_train_ref import CompoundTrainRef
from netex.cycle_model_profile_ref import CycleModelProfileRef
from netex.multilingual_string import MultilingualString
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.train_ref import TrainRef
from netex.transport_type_ref import TransportTypeRef
from netex.vehicle_equipment_profile_refs_rel_structure import VehicleEquipmentProfileRefsRelStructure
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleModelVersionStructure(DataManagedObjectStructure):
    """
    Type for a VEHICLE MODEL.

    :ivar name: Name of VEHICLE MODEL.
    :ivar description: Description of VEHICLE MODEL.
    :ivar manufacturer: Manufacturer of VEHICLE MODEL.
    :ivar choice:
    :ivar equipment_profiles: Equipment profiles assoicated with model
        +v1.2.2
    :ivar cycle_model_profile_ref_or_car_model_profile_ref:
    """
    class Meta:
        name = "VehicleModel_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    manufacturer: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
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
    equipment_profiles: Optional[VehicleEquipmentProfileRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    cycle_model_profile_ref_or_car_model_profile_ref: Optional[object] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CycleModelProfileRef",
                    "type": CycleModelProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CarModelProfileRef",
                    "type": CarModelProfileRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
