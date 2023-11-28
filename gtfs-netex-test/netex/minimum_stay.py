from dataclasses import dataclass, field
from netex.minimum_stay_version_structure import MinimumStayVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class MinimumStay(MinimumStayVersionStructure):
    """
    Details of any minimum stay at the destination  required  to use the product.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
