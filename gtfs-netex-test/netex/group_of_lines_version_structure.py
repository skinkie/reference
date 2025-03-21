from dataclasses import dataclass, field
from typing import Optional, Union

from .all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from .flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from .group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from .group_of_lines_type_enumeration import GroupOfLinesTypeEnumeration
from .line_ref_structure import LineRefStructure
from .line_refs_rel_structure import LineRefsRelStructure
from .payment_method_enumeration import PaymentMethodEnumeration
from .personal_mode_of_operation_ref import PersonalModeOfOperationRef
from .purchase_moment_enumeration import PurchaseMomentEnumeration
from .scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from .transport_submode import TransportSubmode
from .type_of_payment_method_value_structure import TypeOfPaymentMethodValueStructure
from .vehicle_pooling_ref import VehiclePoolingRef
from .vehicle_rental_ref import VehicleRentalRef
from .vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class GroupOfLinesVersionStructure(GroupOfEntitiesVersionStructure):
    class Meta:
        name = "GroupOfLines_VersionStructure"

    use_to_exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    members: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    main_line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "MainLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    mode_of_operation_ref_or_alternative_mode_of_operation_ref_or_conventional_mode_of_operation_ref: Optional[Union[PersonalModeOfOperationRef, VehiclePoolingRef, VehicleSharingRef, VehicleRentalRef, FlexibleModeOfOperationRef, ScheduledModeOfOperationRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "PersonalModeOfOperationRef",
                    "type": PersonalModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehiclePoolingRef",
                    "type": VehiclePoolingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleSharingRef",
                    "type": VehicleSharingRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "VehicleRentalRef",
                    "type": VehicleRentalRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FlexibleModeOfOperationRef",
                    "type": FlexibleModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ScheduledModeOfOperationRef",
                    "type": ScheduledModeOfOperationRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    group_of_lines_type: Optional[GroupOfLinesTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    payment_methods: list[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodValueStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    purchase_moment: list[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        },
    )
