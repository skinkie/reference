from dataclasses import dataclass, field
from typing import Optional, Union

from xsdata.models.datatype import XmlDate

from .authority_ref import AuthorityRef
from .car_model_profile_ref import CarModelProfileRef
from .compound_train_ref import CompoundTrainRef
from .contact_ref import ContactRef
from .cycle_model_profile_ref import CycleModelProfileRef
from .entity_in_version_structure import DataManagedObjectStructure
from .equipments_rel_structure import EquipmentsRelStructure
from .multilingual_string import MultilingualString
from .operator_ref import OperatorRef
from .powered_train_ref import PoweredTrainRef
from .private_code import PrivateCode
from .simple_vehicle_type_ref import SimpleVehicleTypeRef
from .train_ref import TrainRef
from .transport_type_ref import TransportTypeRef
from .unpowered_train_ref import UnpoweredTrainRef
from .vehicle_model_ref import VehicleModelRef
from .vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "Vehicle_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
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
    build_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "BuildDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    chassis_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "ChassisNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    registration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrationNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    registration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegistrationDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    operational_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_organisation_ref: Optional[Union[AuthorityRef, OperatorRef]] = field(
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
        },
    )
    contact_ref: Optional[ContactRef] = field(
        default=None,
        metadata={
            "name": "ContactRef",
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
    vehicle_model_ref: Optional[VehicleModelRef] = field(
        default=None,
        metadata={
            "name": "VehicleModelRef",
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
    actual_vehicle_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "actualVehicleEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
