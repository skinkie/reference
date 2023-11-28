from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.headway_use_enumeration import HeadwayUseEnumeration
from netex.multilingual_string import MultilingualString

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FrequencyStructure:
    """
    Type for a HEADWAY INTERVAL.

    :ivar scheduled_headway_interval: Scheduled normal headway interval.
    :ivar minimum_headway_interval: Minimum headway interval.
    :ivar maximum_headway_interval: Maximum headway interval.
    :ivar headway_display: Use to be made of Headway information when
        displaying to public. Default is Display Instead of Passing
        Times.
    :ivar frequency_regulated: Whether service falls under regulations
        for frequency service.
    :ivar description: Descriptive phrase to use for frequency. e.g.
        "Every x minus"  If not specified generate from individual
        elements.
    """
    scheduled_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ScheduledHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_headway_interval: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumHeadwayInterval",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    headway_display: Optional[HeadwayUseEnumeration] = field(
        default=None,
        metadata={
            "name": "HeadwayDisplay",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    frequency_regulated: Optional[bool] = field(
        default=None,
        metadata={
            "name": "FrequencyRegulated",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
