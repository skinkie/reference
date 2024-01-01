from dataclasses import dataclass
from .mobility_journey_version_frame_structure import (
    MobilityJourneyVersionFrameStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class MobilityJourneyFrame(MobilityJourneyVersionFrameStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
