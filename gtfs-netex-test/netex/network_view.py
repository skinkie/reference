from dataclasses import dataclass
from .network_derived_view_structure import NetworkDerivedViewStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkView(NetworkDerivedViewStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
