from dataclasses import dataclass

from .quay_ref_structure import QuayRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TaxiStandRefStructure(QuayRefStructure):
    pass
