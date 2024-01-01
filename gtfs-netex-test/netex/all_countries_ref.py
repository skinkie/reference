from dataclasses import dataclass
from .all_countries_ref_structure import AllCountriesRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AllCountriesRef(AllCountriesRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    value: RestrictedVar
