from enum import Enum

__NAMESPACE__ = "http://www.netex.org.uk/netex"


class TypeOfContractEnumeration(Enum):
    FORMAL = "formal"
    INFORMAL = "informal"
    WRITTEN = "written"
    ORAL = "oral"
    PLAIN_UNDERSTOOD = "plainUnderstood"
