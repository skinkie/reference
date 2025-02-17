from dataclasses import dataclass

from .tariff_ref_structure import TariffRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TariffRef(TariffRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
