from dataclasses import dataclass, field
from typing import List, Optional
from netex.all_vehicle_modes_of_transport_enumeration import AllVehicleModesOfTransportEnumeration
from netex.flexible_mode_of_operation_ref import FlexibleModeOfOperationRef
from netex.group_of_entities_version_structure import GroupOfEntitiesVersionStructure
from netex.group_of_lines_type_enumeration import GroupOfLinesTypeEnumeration
from netex.line_ref_structure import LineRefStructure
from netex.line_refs_rel_structure import LineRefsRelStructure
from netex.payment_method_enumeration import PaymentMethodEnumeration
from netex.personal_mode_of_operation_ref import PersonalModeOfOperationRef
from netex.purchase_moment_enumeration import PurchaseMomentEnumeration
from netex.scheduled_mode_of_operation_ref import ScheduledModeOfOperationRef
from netex.transport_submode import TransportSubmode
from netex.type_of_payment_method_value_structure import TypeOfPaymentMethodValueStructure
from netex.vehicle_pooling_ref import VehiclePoolingRef
from netex.vehicle_rental_ref import VehicleRentalRef
from netex.vehicle_sharing_ref import VehicleSharingRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GroupOfLinesVersionStructure(GroupOfEntitiesVersionStructure):
    """
    Type for GROUP OF LINES.

    :ivar use_to_exclude: Whether contents of Group should be used to
        exclude (true) from a large list . The default is include
        (i.e.false)
    :ivar members: LINEs in GROUP OF LINEs.
    :ivar main_line_ref: Primary LINE in GROUP OF LINEs, if relevant.
    :ivar transport_mode: Primary Transport MODE of NETWORK.
    :ivar transport_submode:
    :ivar choice:
    :ivar group_of_lines_type: Classification of GROUP OF LINES. +v1.1
    :ivar payment_methods: Payment Methods allowed on LINE. +v1.1
    :ivar types_of_payment_method: TYPES OF PAYMENT yment Methods
        allowed on LINE. +v1.1
    :ivar purchase_moment: PURCHASE MOMENT types allowed on LINE. +v1.1
    """
    class Meta:
        name = "GroupOfLines_VersionStructure"

    use_to_exclude: Optional[bool] = field(
        default=None,
        metadata={
            "name": "UseToExclude",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    members: Optional[LineRefsRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    main_line_ref: Optional[LineRefStructure] = field(
        default=None,
        metadata={
            "name": "MainLineRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_mode: Optional[AllVehicleModesOfTransportEnumeration] = field(
        default=None,
        metadata={
            "name": "TransportMode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transport_submode: Optional[TransportSubmode] = field(
        default=None,
        metadata={
            "name": "TransportSubmode",
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
        }
    )
    group_of_lines_type: Optional[GroupOfLinesTypeEnumeration] = field(
        default=None,
        metadata={
            "name": "GroupOfLinesType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    payment_methods: List[PaymentMethodEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PaymentMethods",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
    types_of_payment_method: Optional[TypeOfPaymentMethodValueStructure] = field(
        default=None,
        metadata={
            "name": "typesOfPaymentMethod",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    purchase_moment: List[PurchaseMomentEnumeration] = field(
        default_factory=list,
        metadata={
            "name": "PurchaseMoment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "tokens": True,
        }
    )
