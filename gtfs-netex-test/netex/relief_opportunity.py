from dataclasses import dataclass
from .relief_opportunity_version_structure import (
    ReliefOpportunityVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ReliefOpportunity(ReliefOpportunityVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
