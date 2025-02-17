from dataclasses import dataclass

from .all_authorities_ref_structure import AllAuthoritiesRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AllOperatorsRefStructure(AllAuthoritiesRefStructure):
    pass
