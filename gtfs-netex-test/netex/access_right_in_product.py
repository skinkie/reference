from dataclasses import dataclass, field
from typing import Optional
from netex.access_right_in_product_versioned_child_structure import AccessRightInProductVersionedChildStructure
from netex.branding_ref import BrandingRef
from netex.key_list import KeyList

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccessRightInProduct(AccessRightInProductVersionedChildStructure):
    """
    A VALIDABLE ELEMENT as a part of a PRE-ASSIGNED FARE PRODUCT, including its
    possible order in the set of all VALIDABLE ELEMENTs grouped together to define
    the access right assigned to that PRE-ASSIGNED FARE PRODUCT.

    :ivar key_list: A list of alternative Key values for an element.
    :ivar branding_ref:
    :ivar id:
    :ivar order: order of element in sequence.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    key_list: Optional[KeyList] = field(
        default=None,
        metadata={
            "name": "keyList",
            "type": "Element",
        }
    )
    branding_ref: Optional[BrandingRef] = field(
        default=None,
        metadata={
            "name": "BrandingRef",
            "type": "Element",
        }
    )
    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
    order: int = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
