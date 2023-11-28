from dataclasses import dataclass, field
from netex.quality_structure_factor_price_versioned_child_structure import QualityStructureFactorPriceVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class QualityStructureFactorPrice(QualityStructureFactorPriceVersionedChildStructure):
    """A set of all possible price features of a QUALITY STRUCTURE FACTOR: default total price etc."""
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
