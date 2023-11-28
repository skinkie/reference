from dataclasses import dataclass, field
from netex.rental_option_version_structure import RentalOptionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RentalOption(RentalOptionVersionStructure):
    """Parameters relating to paying by RentalOption for a product.

    +v1.1
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
