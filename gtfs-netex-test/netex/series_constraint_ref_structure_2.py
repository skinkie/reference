from dataclasses import dataclass, field
from typing import Optional

from .priceable_object_ref_structure import PriceableObjectRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class SeriesConstraintRefStructure2(PriceableObjectRefStructure):
    class Meta:
        name = "SeriesConstraintRefStructure_"

    order: Optional[int] = field(
        default=None,
        metadata={
            "type": "Attribute",
        },
    )
