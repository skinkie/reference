from dataclasses import dataclass
from .country_ref_structure import CountryRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CountryRef(CountryRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
