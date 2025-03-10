from dataclasses import dataclass, field
from typing import Optional

from .customer_purchase_package_ref import CustomerPurchasePackageRef
from .entity_in_version_structure import DataManagedObjectStructure
from .marked_as_enumeration import MarkedAsEnumeration
from .multilingual_string import MultilingualString
from .private_code import PrivateCode
from .type_of_travel_document_ref import TypeOfTravelDocumentRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TravelDocumentVersionStructure(DataManagedObjectStructure):
    class Meta:
        name = "TravelDocument_VersionStructure"

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
    private_code: Optional[PrivateCode] = field(
        default=None,
        metadata={
            "name": "PrivateCode",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    type_of_travel_document_ref: Optional[TypeOfTravelDocumentRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTravelDocumentRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    customer_purchase_package_ref: Optional[CustomerPurchasePackageRef] = field(
        default=None,
        metadata={
            "name": "CustomerPurchasePackageRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    marked_as: Optional[MarkedAsEnumeration] = field(
        default=None,
        metadata={
            "name": "MarkedAs",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
