from dataclasses import dataclass, field
from typing import Optional
from netex.access_right_in_product_ref import AccessRightInProductRef
from netex.amount_of_price_unit_product_ref import AmountOfPriceUnitProductRef
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.capped_discount_right_ref import CappedDiscountRightRef
from netex.charging_basis_enumeration import ChargingBasisEnumeration
from netex.controllable_element_in_sequence_ref import ControllableElementInSequenceRef
from netex.controllable_element_ref import ControllableElementRef
from netex.distance_matrix_element_inverse_ref import DistanceMatrixElementInverseRef
from netex.distance_matrix_element_ref import DistanceMatrixElementRef
from netex.distance_matrix_element_view import DistanceMatrixElementView
from netex.fare_product_ref import FareProductRef
from netex.fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from netex.fare_structure_element_ref import FareStructureElementRef
from netex.group_of_distance_matrix_elements_ref import GroupOfDistanceMatrixElementsRef
from netex.group_of_sales_offer_packages_ref import GroupOfSalesOfferPackagesRef
from netex.logical_operation_enumeration import LogicalOperationEnumeration
from netex.parking_tariff_ref import ParkingTariffRef
from netex.preassigned_fare_product_ref import PreassignedFareProductRef
from netex.relative_operator_enumeration import RelativeOperatorEnumeration
from netex.sale_discount_right_ref import SaleDiscountRightRef
from netex.sales_offer_package_ref import SalesOfferPackageRef
from netex.set_operator_enumeration import SetOperatorEnumeration
from netex.supplement_product_ref import SupplementProductRef
from netex.tariff_ref import TariffRef
from netex.temporal_validity_parameters_rel_structure import TemporalValidityParametersRelStructure
from netex.third_party_product_ref import ThirdPartyProductRef
from netex.type_of_access_right_assignment_ref import TypeOfAccessRightAssignmentRef
from netex.usage_discount_right_ref import UsageDiscountRightRef
from netex.usage_parameters_rel_structure import UsageParametersRelStructure
from netex.validable_element_ref import ValidableElementRef
from netex.validity_parameters_rel_structure import ValidityParametersRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRightParameterAssignmentVersionStructure(AssignmentVersionStructure1):
    """
    Type for ACCESS RIGHT PARAMETER ASSIGNMENT.

    :ivar is_allowed: Whether values are allowed ro forbiden. Defaullt
        is allowed.
    :ivar type_of_access_right_assignment_ref:
    :ivar charging_basis: Whether ACCESS RIGHT ASSIGNMENT is chargable
        or not.
    :ivar validable_element_ref:
    :ivar controllable_element_ref:
    :ivar choice:
    :ivar parking_tariff_ref_or_tariff_ref:
    :ivar fare_structure_element_ref:
    :ivar
        controllable_element_in_sequence_ref_or_fare_structure_element_in_sequence_ref_or_access_right_in_product_ref:
    :ivar distance_matrix_element_ref:
    :ivar distance_matrix_element_inverse_ref:
    :ivar distance_matrix_element_view:
    :ivar sales_offer_package_ref:
    :ivar group_of_distance_matrix_elements_ref:
    :ivar group_of_sales_offer_packages_ref:
    :ivar limitation_grouping_type: Operator for Grouping Scope
        Elements: logical OR, AND, NOT. Default is AND.
    :ivar limitation_set_selection_type: Where parameter is a group
        (GROUP of xxx), operator for distinguishing between whole set
        and item interpretation of elements which are sets of elements.
    :ivar limitations:
    :ivar validity_parameter_assignment_type: Comparison Operator for
        comparing Validity Erlements valeus. Defalut is EQ.
    :ivar validity_parameter_grouping_type: Operator for Grouping Scope
        Elements: logical OR, AND, NOT. Default is AND.
    :ivar validity_parameter_set_selection_type: Where one or more
        parameter is a group containing multiple elements, (GROUP OF
        xxx), set operator for distinguishing between whole set and item
        interpretation of elements which are sets of elements.
    :ivar temporal_validity_parameters: Temporal Validity parameters for
        the assignment.
    :ivar validity_parameters: Validity parameters for the assignment.
    """
    class Meta:
        name = "AccessRightParameterAssignment_VersionStructure"

    is_allowed: Optional[bool] = field(
        default=None,
        metadata={
            "name": "IsAllowed",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_access_right_assignment_ref: Optional[TypeOfAccessRightAssignmentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfAccessRightAssignmentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    charging_basis: Optional[ChargingBasisEnumeration] = field(
        default=None,
        metadata={
            "name": "ChargingBasis",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validable_element_ref: Optional[ValidableElementRef] = field(
        default=None,
        metadata={
            "name": "ValidableElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_ref: Optional[ControllableElementRef] = field(
        default=None,
        metadata={
            "name": "ControllableElementRef",
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
        }
    )
    parking_tariff_ref_or_tariff_ref: Optional[object] = field(
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
        }
    )
    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    controllable_element_in_sequence_ref_or_fare_structure_element_in_sequence_ref_or_access_right_in_product_ref: Optional[object] = field(
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
        }
    )
    distance_matrix_element_ref: Optional[DistanceMatrixElementRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_inverse_ref: Optional[DistanceMatrixElementInverseRef] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementInverseRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    distance_matrix_element_view: Optional[DistanceMatrixElementView] = field(
        default=None,
        metadata={
            "name": "DistanceMatrixElementView",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sales_offer_package_ref: Optional[SalesOfferPackageRef] = field(
        default=None,
        metadata={
            "name": "SalesOfferPackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_distance_matrix_elements_ref: Optional[GroupOfDistanceMatrixElementsRef] = field(
        default=None,
        metadata={
            "name": "GroupOfDistanceMatrixElementsRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    group_of_sales_offer_packages_ref: Optional[GroupOfSalesOfferPackagesRef] = field(
        default=None,
        metadata={
            "name": "GroupOfSalesOfferPackagesRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limitation_grouping_type: Optional[LogicalOperationEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitationGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limitation_set_selection_type: Optional[SetOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "LimitationSetSelectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    limitations: Optional[UsageParametersRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignment_type: Optional[RelativeOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterAssignmentType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_grouping_type: Optional[LogicalOperationEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterGroupingType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_set_selection_type: Optional[SetOperatorEnumeration] = field(
        default=None,
        metadata={
            "name": "ValidityParameterSetSelectionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    temporal_validity_parameters: Optional[TemporalValidityParametersRelStructure] = field(
        default=None,
        metadata={
            "name": "temporalValidityParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameters: Optional[ValidityParametersRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameters",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
