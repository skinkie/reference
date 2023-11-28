from dataclasses import dataclass
from netex.authority_ref_structure import AuthorityRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AuthorityRef(AuthorityRefStructure):
    """
    Reference to an AUTHORITY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
