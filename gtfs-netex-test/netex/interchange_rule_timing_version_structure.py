from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.journey_timing_versioned_child_structure import JourneyTimingVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class InterchangeRuleTimingVersionStructure(JourneyTimingVersionedChildStructure):
    """
    Type for INTERCHANGE RULE TIMING.

    :ivar standard_wait_time: Standard wait time for INTERCHANGE.
    :ivar maximum_wait_time: Maximum wait time for INTERCHANGE.
    :ivar maximum_automatic_wait_time: Maximum automatic wait time for
        INTERCHANGE.
    :ivar standard_transfer_time: Standard transfer  duration for
        INTERCHANGE.
    :ivar minimum_transfer_time: Maximum transfer duration for
        INTERCHANGE.
    :ivar maximum_transfer_time: Maximum transfer duration for
        INTERCHANGE.
    :ivar control_centre_notify_threshold: Interval before CONTROL
        CENTRE should be notified associated with  SERVICE JOURNEY
        INTERCHANGE.
    """
    class Meta:
        name = "InterchangeRuleTiming_VersionStructure"

    standard_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_automatic_wait_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumAutomaticWaitTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    standard_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "StandardTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    minimum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MinimumTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_transfer_time: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "MaximumTransferTime",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    control_centre_notify_threshold: Optional[XmlDuration] = field(
        default=None,
        metadata={
            "name": "ControlCentreNotifyThreshold",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
