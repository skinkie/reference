from dataclasses import dataclass

from .network_restriction_ref_structure import NetworkRestrictionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class OvertakingPossibilityRefStructure(NetworkRestrictionRefStructure):
    pass
