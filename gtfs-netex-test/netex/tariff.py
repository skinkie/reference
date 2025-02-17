from dataclasses import dataclass

from .tariff_version_structure import TariffVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Tariff(TariffVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
