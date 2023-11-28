from dataclasses import dataclass, field
from netex.entitlement_required_version_structure import EntitlementRequiredVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementRequired(EntitlementRequiredVersionStructure):
    """
    A rerirement to a SERVICE ACCESS RIGHT in order to purchase or use PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
