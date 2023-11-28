from dataclasses import dataclass, field
from netex.additional_driver_option_version_structure import AdditionalDriverOptionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AdditionalDriverOption(AdditionalDriverOptionVersionStructure):
    """Parameters relating to paying by AdditionalDriverOption for a product.

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
