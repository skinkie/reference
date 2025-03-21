from dataclasses import dataclass

from .authority_ref_structure import AuthorityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AuthorityRef(AuthorityRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
