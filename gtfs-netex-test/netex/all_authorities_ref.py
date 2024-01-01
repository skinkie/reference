from dataclasses import dataclass
from .all_authorities_ref_structure import AllAuthoritiesRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllAuthoritiesRef(AllAuthoritiesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
