from dataclasses import dataclass
from .heading_sign_structure import HeadingSignStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadingSign(HeadingSignStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
