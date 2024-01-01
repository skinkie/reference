from dataclasses import dataclass
from .authority_ref_structure import AuthorityRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AuthorityRef(AuthorityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RestrictedVar
