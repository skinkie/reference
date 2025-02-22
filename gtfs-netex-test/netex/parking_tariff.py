from dataclasses import dataclass

from .parking_tariff_version_structure import ParkingTariffVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ParkingTariff(ParkingTariffVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
