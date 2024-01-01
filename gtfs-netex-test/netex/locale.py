from dataclasses import dataclass
from .locale_structure import LocaleStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Locale(LocaleStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
