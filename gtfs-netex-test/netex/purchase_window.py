from dataclasses import dataclass

from .purchase_window_version_structure import PurchaseWindowVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PurchaseWindow(PurchaseWindowVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
