from dataclasses import dataclass
from netex.series_constraint_price_ref_structure import SeriesConstraintPriceRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class SeriesConstraintPriceRef(SeriesConstraintPriceRefStructure):
    """
    Reference to a SERIES CONSTRAINT PRICE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
