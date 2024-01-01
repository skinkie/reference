from dataclasses import dataclass
from .network_restriction_ref_structure import NetworkRestrictionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class NetworkRestrictionRef(NetworkRestrictionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
