from dataclasses import dataclass

from .activation_link_version_structure import ActivationLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ActivationLink(ActivationLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
