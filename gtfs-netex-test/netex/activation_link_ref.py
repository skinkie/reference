from dataclasses import dataclass
from .activation_link_ref_structure import ActivationLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationLinkRef(ActivationLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
