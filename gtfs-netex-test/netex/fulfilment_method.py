from dataclasses import dataclass

from .fulfilment_method_version_structure import FulfilmentMethodVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class FulfilmentMethod(FulfilmentMethodVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
