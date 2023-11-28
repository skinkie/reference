from dataclasses import dataclass, field
from typing import List, Optional, Type
from netex.cell_ref import CellRef
from netex.fare_price_versioned_child_structure import FarePriceVersionedChildStructure
from netex.geographical_unit_price_ref import GeographicalUnitPriceRef
from netex.geographical_unit_ref import GeographicalUnitRef
from netex.strict_containment_aggregation_structure import StrictContainmentAggregationStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnitPricesRelStructure(StrictContainmentAggregationStructure):
    """
    Type for a list of GEOGRAPHICAL UNIT PRICEs.
    """
    class Meta:
        name = "geographicalUnitPrices_RelStructure"

    geographical_unit_price_ref_or_geographical_unit_price_or_cell_ref: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "GeographicalUnitPriceRef",
                    "type": GeographicalUnitPriceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "GeographicalUnitPrice",
                    "type": Type["GeographicalUnitPriceVersionedChildStructure"],
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "CellRef",
                    "type": CellRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnitPriceVersionedChildStructure(FarePriceVersionedChildStructure):
    """
    Type for a GEOGRAPHICAL UNIT PRICE.

    :ivar geographical_unit_ref:
    :ivar prices: Prices for GEOGRAPHICAL UNIT.
    """
    class Meta:
        name = "GeographicalUnitPrice_VersionedChildStructure"

    geographical_unit_ref: Optional[GeographicalUnitRef] = field(
        default=None,
        metadata={
            "name": "GeographicalUnitRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    prices: Optional[GeographicalUnitPricesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
