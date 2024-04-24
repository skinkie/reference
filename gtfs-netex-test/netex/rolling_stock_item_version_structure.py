from dataclasses import dataclass, field
from typing import Optional, Union

from .authority_ref import AuthorityRef
from .entity_in_version_structure import DataManagedObjectStructure
from .equipments_rel_structure import EquipmentsRelStructure
from .multilingual_string import MultilingualString
from .operator_ref import OperatorRef
from .service_facility_set_version_structure import ServiceFacilitySetVersionStructure
from .train_element_type_type_enumeration import TrainElementTypeTypeEnumeration
from .type_of_rolling_stock_ref import TypeOfRollingStockRef
from .vehicle_model_ref import VehicleModelRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RollingStockItemVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "RollingStockItem_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
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
    vehicle_model_ref: Optional[VehicleModelRef] = field(
        default=None,
        metadata={
            "name": "VehicleModelRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    rolling_stock_type: Optional[TrainElementTypeTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "RollingStockType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_rolling_stock_ref: Optional[TypeOfRollingStockRef] = field(
        default=None,
        metadata={
            "name": "TypeOfRollingStockRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    facilities: Optional[ServiceFacilitySetVersionStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    actual_equipments: Optional[EquipmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "actualEquipments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
