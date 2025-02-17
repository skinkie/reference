from dataclasses import dataclass

from .locale_structure import LocaleStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Locale(LocaleStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
