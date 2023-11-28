from dataclasses import dataclass, field
from netex.pricing_parameter_set_versioned_structure import PricingParameterSetVersionedStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class PricingParameterSet(PricingParameterSetVersionedStructure):
    """
    Parameters governing the calculation of fares.

    :ivar id: Identifier of ENTITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
