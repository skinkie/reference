from dataclasses import dataclass, field
from netex.entitlement_given_version_structure import EntitlementGivenVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class EntitlementGiven(EntitlementGivenVersionStructure):
    """
    A right to a SERVICE ACCESS RIGHT is given by a FARE PRODUCT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
