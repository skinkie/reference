from dataclasses import dataclass, field
from typing import Optional
from xsdata.models.datatype import XmlDuration
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultInterchangeVersionStructure(DataManagedObjectStructure):
    """
    Type for DEFAULT INTERCHANGE.

    :ivar from_stop_point_ref: SCHEDULED STOP POINT feeding INTERCHANGE.
        If absent apply to all STOP POINTs.
    :ivar to_stop_point_ref: SCHEDULED STOP POINT distributing from
        INTERCHANGE. If absent apply to all STOP POINTs.
    :ivar description: Description of INTERCHANGE.
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
    """
    class Meta:
        name = "DefaultInterchange_VersionStructure"

    from_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromStopPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_stop_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToStopPointRef",
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
