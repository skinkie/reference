from dataclasses import dataclass

from .relief_opportunity_version_structure import ReliefOpportunityVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class ReliefOpportunity(ReliefOpportunityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
