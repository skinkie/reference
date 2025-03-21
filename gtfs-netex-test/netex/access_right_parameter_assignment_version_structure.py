from dataclasses import dataclass, field
from typing import Optional, Union

from .access_right_in_product_ref import AccessRightInProductRef
from .amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from .assignment_version_structure_1 import AssignmentVersionStructure1
from .capped_discount_right_ref import CappedDiscountRightRef
from .charging_basis_enumeration import ChargingBasisEnumeration
from .controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from .controllable_element_ref import ControllableElementRef
from .distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from .distance_matrix_element_ref import DistanceMatrixElementRef
from .distance_matrix_element_view import DistanceMatrixElementView
from .dynamic_distance_matrix_element import DynamicDistanceMatrixElement
from .fare_product_ref import FareProductRef
from .fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from .fare_structure_element_ref import FareStructureElementRef
from .group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from .group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from .logical_operation_enumeration import LogicalOperationEnumeration
from .parking_tariff_ref import ParkingTariffRef
from .preassigned_fare_product_ref import PreassignedFareProductRef
from .relative_operator_enumeration import RelativeOperatorEnumeration
from .sale_discount_right_ref import SaleDiscountRightRef
from .sales_offer_package_ref import SalesOfferPackageRef
from .set_operator_enumeration import SetOperatorEnumeration
from .supplement_product_ref import SupplementProductRef
from .tariff_ref import TariffRef
from .temporal_validity_parameters_rel_structure import TemporalValidityParametersRelStructure
from .third_party_product_ref import ThirdPartyProductRef
from .type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from .usage_discount_right_ref import UsageDiscountRightRef
from .usage_parameters_rel_structure import UsageParametersRelStructure
from .validable_element_ref import ValidableElementRef
from .validity_parameters_rel_structure import ValidityParametersRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccessRightParameterAssignmentVersionStructure(AssignmentVersionStructure1):
    class Meta:
        name = "AccessRightParameterAssignment_VersionStructure"

    is_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_access_right_assignment_ref: Optional[TypeOfAccessRightAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    charging_basis: Optional[ChargingBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "ChargingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    preassigned_fare_product_ref_or_fare_product_ref_or_sale_discount_right_ref: Optional[Union[SupplementProductRef, PreassignedFareProductRef, AmountOfPriceUnitProductRef, UsageDiscountRightRef, ThirdPartyProductRef, CappedDiscountRightRef, SaleDiscountRightRef, FareProductRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "SupplementProductRef",
                    "type": SupplementProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "PreassignedFareProductRef",
                    "type": PreassignedFareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AmountOfPriceUnitProductRef",
                    "type": AmountOfPriceUnitProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "UsageDiscountRightRef",
                    "type": UsageDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "ThirdPartyProductRef",
                    "type": ThirdPartyProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CappedDiscountRightRef",
                    "type": CappedDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "SaleDiscountRightRef",
                    "type": SaleDiscountRightRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareProductRef",
                    "type": FareProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    tariff_ref: Optional[Union[ParkingTariffRef, TariffRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ParkingTariffRef",
                    "type": ParkingTariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "TariffRef",
                    "type": TariffRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    fare_element_in_sequence_ref: Optional[Union[ControllableElementInSequenceRef, FareStructureElementInSequenceRef, AccessRightInProductRef]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "ControllableElementInSequenceRef",
                    "type": ControllableElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "FareStructureElementInSequenceRef",
                    "type": FareStructureElementInSequenceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "AccessRightInProductRef",
                    "type": AccessRightInProductRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    distance_matrix_element_ref_or_dynamic_distance_matrix_element: Optional[Union[DistanceMatrixElementRef, DynamicDistanceMatrixElement]] = field(
        default=None,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "DistanceMatrixElementRef",
                    "type": DistanceMatrixElementRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "DynamicDistanceMatrixElement",
                    "type": DynamicDistanceMatrixElement,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        },
    )
    distance_matrix_element_inverse_ref: Optional[DistanceMatrixElementInverseRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementInverseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    distance_matrix_element_view: Optional[DistanceMatrixElementView] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_distance_matrix_elements_ref: Optional[GroupOfDistanceMatrixElementsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    group_of_sales_offer_packages_ref: Optional[GroupOfSalesOfferPackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    limitation_grouping_type: Optional[LogicalOperationEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitationGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    limitation_set_selection_type: Optional[SetOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitationSetSelectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    limitations: Optional[UsageParametersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_assignment_type: Optional[RelativeOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterAssignmentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_grouping_type: Optional[LogicalOperationEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameter_set_selection_type: Optional[SetOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterSetSelectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    temporal_validity_parameters: Optional[TemporalValidityParametersRelStructure] = field(
        default=None,
        metadata={
            "name": "temporalValidityParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    validity_parameters: Optional[ValidityParametersRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
