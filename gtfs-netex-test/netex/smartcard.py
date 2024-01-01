from dataclasses import dataclass
from .smartcard_version_structure import SmartcardVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Smartcard(SmartcardVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
