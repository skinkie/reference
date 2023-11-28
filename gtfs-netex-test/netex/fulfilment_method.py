from dataclasses import dataclass, field
from netex.fulfilment_method_version_structure import FulfilmentMethodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FulfilmentMethod(FulfilmentMethodVersionStructure):
    """The means by which the ticket is delivered to the Customer.

    e.g. online, collection, etc.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
