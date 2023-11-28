from dataclasses import dataclass, field
from netex.retail_consortium_version_structure import RetailConsortiumVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RetailConsortium(RetailConsortiumVersionStructure):
    """
    A group of ORGANISATIONs formally incorporated as a retailer of fare products.

    :ivar id: Identifier of RETAIL CONSORTIUM.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
