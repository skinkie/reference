from dataclasses import dataclass
from netex.activation_link_ref_structure import ActivationLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class ActivationLinkRef(ActivationLinkRefStructure):
    """
    Reference to an ACTIVATION LINK.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
