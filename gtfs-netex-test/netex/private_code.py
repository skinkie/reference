from dataclasses import dataclass
from .private_code_structure import PrivateCodeStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PrivateCode(PrivateCodeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
