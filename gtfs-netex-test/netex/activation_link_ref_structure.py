from dataclasses import dataclass
from netex.link_ref_structure import LinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationLinkRefStructure(LinkRefStructure):
    """
    Type for a reference to an ACTIVATION LINK.
    """
