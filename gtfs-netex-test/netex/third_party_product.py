from dataclasses import dataclass, field
from netex.third_party_product_version_structure import ThirdPartyProductVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ThirdPartyProduct(ThirdPartyProductVersionStructure):
    """
    A FARE PRODUCT that is marketed together with a Public Transport Fare Product.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
