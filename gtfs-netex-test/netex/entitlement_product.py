from dataclasses import dataclass, field
from netex.entitlement_product_version_structure import EntitlementProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementProduct(EntitlementProductVersionStructure):
    """
    A precondition to access a service or to purchase a FARE PRODUCT issued by an
    organisation that may not be a PT operator (e.g. military card).
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
