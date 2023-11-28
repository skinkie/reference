from dataclasses import dataclass
from netex.private_code_structure import PrivateCodeStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AccountingCode(PrivateCodeStructure):
    """
    An Accounting code assigned to the Element (TAP TSI)
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
