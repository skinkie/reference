from dataclasses import dataclass
from .headway_journey_group_version_structure import (
    HeadwayJourneyGroupVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class HeadwayJourneyGroup(HeadwayJourneyGroupVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
