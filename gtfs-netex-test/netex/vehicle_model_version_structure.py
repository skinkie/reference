from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional, Union

from .car_model_profile_ref import CarModelProfileRef
from .compound_train_ref import CompoundTrainRef
from .contact_structure import ContactStructure
from .cycle_model_profile_ref import CycleModelProfileRef
from .entity_in_version_structure import DataManagedObjectStructure
from .multilingual_string import MultilingualString
from .powered_train_ref import PoweredTrainRef
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_equipment_profile_refs_rel_structure import VehicleEquipmentProfileRefsRelStructure
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class VehicleModelVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "VehicleModel_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    manufacturer: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Manufacturer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_type_ref_or_vehicle_type_ref_or_train_ref: Optional[Union[SimpleVehicleTypeRef, CompoundTrainRef, UnpoweredTrainRef, PoweredTrainRef, TrainRef, VehicleTypeRef, TransportTypeRef]] = field(
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
                    "name": "UnpoweredTrainRef",
                    "type": UnpoweredTrainRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PoweredTrainRef",
                    "type": PoweredTrainRef,
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
        },
    )
    range: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Range",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    full_charge: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "FullCharge",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    equipment_profiles: Optional[VehicleEquipmentProfileRefsRelStructure] = field(
        default=None,
        metadata={
            "name": "equipmentProfiles",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    vehicle_model_profile_ref: Optional[Union[CycleModelProfileRef, CarModelProfileRef]] = field(
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
        },
    )
    customer_service_contact_details: Optional[ContactStructure] = field(
        default=None,
        metadata={
            "name": "CustomerServiceContactDetails",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
