from dataclasses import dataclass, field
from typing import Optional

from xsdata.models.datatype import XmlDuration

from .headway_use_enumeration import HeadwayUseEnumeration
from .journey_frequency_group_version_structure import JourneyFrequencyGroupVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class HeadwayJourneyGroupVersionStructure(JourneyFrequencyGroupVersionStructure):
    class Meta:
        name = "HeadwayJourneyGroup_VersionStructure"

    scheduled_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    minimum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    maximum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
    headway_display: Optional[HeadwayUseEnumeration] = field(
        default=None,
        metadata={
            "name": "HeadwayDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        },
    )
