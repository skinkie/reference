from dataclasses import dataclass

from .private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AccountingCode(PrivateCodeStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
