from dataclasses import dataclass
from netex.tariff_zone_ref_structure import TariffZoneRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareZoneRefStructure(TariffZoneRefStructure):
    """
    Type for Reference to a FARE ZONE.
    """
