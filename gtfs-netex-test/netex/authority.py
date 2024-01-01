from dataclasses import dataclass
from .authority_version_structure import AuthorityVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Authority(AuthorityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
