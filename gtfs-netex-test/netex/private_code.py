from dataclasses import dataclass

from .private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PrivateCode(PrivateCodeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
