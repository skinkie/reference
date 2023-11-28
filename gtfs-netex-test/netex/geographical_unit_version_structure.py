from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.fare_unit_version_structure import FareUnitVersionStructure
from netex.geographical_unit_prices_rel_structure import GeographicalUnitPricesRelStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class GeographicalUnitVersionStructure(FareUnitVersionStructure):
    """
    Type for GEOGRAPHICAL UNIT.

    :ivar distance: Distance of unit in SI meters.
    :ivar prices: PRICEs of GEOGRAPHICAL UNIT.
    """
    class Meta:
        name = "GeographicalUnit_VersionStructure"

    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
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
