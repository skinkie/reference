from dataclasses import dataclass
from .activation_link_ref_by_value_structure import (
    ActivationLinkRefByValueStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ActivationLinkRefByValue(ActivationLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
