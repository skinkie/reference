from dataclasses import dataclass, field
from typing import Optional
from netex.priceable_object_ref_structure import PriceableObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintRefStructure2(PriceableObjectRefStructure):
    """
    Extending type for Reference to a SERIES CONSTRAINT.

    :ivar order: order of constraint.
    """
    class Meta:
        name = "SeriesConstraintRefStructure_"

    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        }
    )
