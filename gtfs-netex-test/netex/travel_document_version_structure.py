from dataclasses import dataclass, field
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.customer_purchase_package_ref import CustomerPurchasePackageRef
from netex.marked_as_enumeration import MarkedAsEnumeration
from netex.multilingual_string import MultilingualString
from netex.private_code import PrivateCode
from netex.type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TravelDocumentVersionStructure(DataManagedObjectStructure):
    """
    Type for TRAVEL DOCUMENT.

    :ivar name: Name of TRAVEL DOCUMENT.
    :ivar description: Description of TRAVEL DOCUMENT.
    :ivar private_code:
    :ivar type_of_travel_document_ref:
    :ivar customer_purchase_package_ref:
    :ivar marked_as: Usage status of the TRAVEL DOCUMENT+v1.1
    """
    class Meta:
        name = "TravelDocument_VersionStructure"

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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    customer_purchase_package_ref: Optional[CustomerPurchasePackageRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageRef",
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
