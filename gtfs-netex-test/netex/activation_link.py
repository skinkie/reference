from dataclasses import dataclass
from .activation_link_version_structure import ActivationLinkVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationLink(ActivationLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
