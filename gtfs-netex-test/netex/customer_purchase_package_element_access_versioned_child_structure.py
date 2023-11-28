from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import VersionedChildStructure
from netex.customer_purchase_package_element_ref import CustomerPurchasePackageElementRef
from netex.customer_purchase_parameter_assignments_rel_structure import CustomerPurchaseParameterAssignmentsRelStructure
from netex.fare_structure_element_in_sequence_ref import FareStructureElementInSequenceRef
from netex.fare_structure_element_ref import FareStructureElementRef
from netex.marked_as_enumeration import MarkedAsEnumeration
from netex.validable_element_ref import ValidableElementRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CustomerPurchasePackageElementAccessVersionedChildStructure(VersionedChildStructure):
    """Type for a CUSTOMER PURCHASE PACKAGE ELEMENT ACCESS.

    +v1.1

    :ivar customer_purchase_package_element_ref:
    :ivar validable_element_ref:
    :ivar fare_structure_element_ref:
    :ivar fare_structure_element_in_sequence_ref:
    :ivar marked_as: Whether the element has been used
    :ivar access_number: Access number of instance +V1.2.2.
    :ivar validity_parameter_assignments: PARAMETER ASSIGNMENTs applying
        to  CUSTOMER PURCHASE PACKAGE ELEMENT ACCESS.
    """
    class Meta:
        name = "CustomerPurchasePackageElementAccess_VersionedChildStructure"

    customer_purchase_package_element_ref: Optional[CustomerPurchasePackageElementRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageElementRef",
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
    fare_structure_element_ref: Optional[FareStructureElementRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    fare_structure_element_in_sequence_ref: Optional[FareStructureElementInSequenceRef] = field(
        default=None,
        metadata={
            "name": "FareStructureElementInSequenceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    marked_as: Optional[MarkedAsEnumeration] = field(
        default=None,
        metadata={
            "name": "MarkedAs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    access_number: Optional[int] = field(
        default=None,
        metadata={
            "name": "AccessNumber",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    validity_parameter_assignments: Optional[CustomerPurchaseParameterAssignmentsRelStructure] = field(
        default=None,
        metadata={
            "name": "validityParameterAssignments",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
