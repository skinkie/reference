from dataclasses import dataclass
from .headway_journey_group_ref_structure import (
    HeadwayJourneyGroupRefStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadwayJourneyGroupRef(HeadwayJourneyGroupRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
