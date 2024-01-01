from dataclasses import dataclass
from .online_service_ref_structure import OnlineServiceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class OnlineServiceRef(OnlineServiceRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
