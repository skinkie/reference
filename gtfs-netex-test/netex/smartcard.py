from dataclasses import dataclass

from .smartcard_version_structure import SmartcardVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Smartcard(SmartcardVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
