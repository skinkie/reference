from dataclasses import dataclass

from .private_codes_structure import PrivateCodesStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PrivateCodes(PrivateCodesStructure):
    class Meta:
        name = "privateCodes"
        namespace = "http://www.netex.org.uk/netex"
