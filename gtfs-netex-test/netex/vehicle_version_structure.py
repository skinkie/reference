from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDate
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.authority_ref import AuthorityRef
from netex.car_model_profile_ref import CarModelProfileRef
from netex.compound_train_ref import CompoundTrainRef
from netex.cycle_model_profile_ref import CycleModelProfileRef
from netex.equipments_rel_structure import EquipmentsRelStructure
from netex.multilingual_string import MultilingualString
from netex.operator_ref import OperatorRef
from netex.private_code import PrivateCode
from netex.simple_vehicle_type_ref import SimpleVehicleTypeRef
from netex.train_ref import TrainRef
from netex.transport_type_ref import TransportTypeRef
from netex.vehicle_model_ref import VehicleModelRef
from netex.vehicle_type_ref import VehicleTypeRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class VehicleVersionStructure(DataManagedObjectStructure):
    """
    Type for a VEHICLE.

    :ivar name: Name of VEHICLE.
    :ivar short_name: Short Name of VEHICLE.
    :ivar description: Description +V1.2.2
    :ivar registration_number: Licence plate of VEHICLE.
    :ivar registration_date: Dae of  registration or commissioning - may
        be used to determin age oif vehice
    :ivar operational_number: Operational Number of VEHICLE.
    :ivar private_code:
    :ivar authority_ref_or_operator_ref:
    :ivar choice:
    :ivar vehicle_model_ref:
    :ivar cycle_model_profile_ref_or_car_model_profile_ref:
    :ivar actual_vehicle_equipments: ACTUAL EQUIPMENT found in VEHICLE.
    """
    class Meta:
        name = "Vehicle_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    short_name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "ShortName",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[object] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    registration_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "RegistrationNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    registration_date: Optional[XmlDate] = field(
        default=None,
        metadata={
            "name": "RegistrationDate",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    operational_number: Optional[str] = field(
        default=None,
        metadata={
            "name": "OperationalNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
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
    vehicle_model_ref: Optional[VehicleModelRef] = field(
        default=None,
        metadata={
            "name": "VehicleModelRef",
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
    actual_vehicle_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "actualVehicleEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
