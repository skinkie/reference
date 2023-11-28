from dataclasses import dataclass, field
from decimal import Decimal
from typing import Optional
from netex.alternative_texts_rel_structure import DataManagedObjectStructure
from netex.multilingual_string import MultilingualString
from netex.transfer_duration_structure import TransferDurationStructure
from netex.type_of_transfer_ref import TypeOfTransferRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferVersionStructure(DataManagedObjectStructure):
    """
    Type for a TRANSFER.

    :ivar name: Name of TRANSFER.
    :ivar type_of_transfer_ref:
    :ivar description: Name of TRANSFER.
    :ivar distance: Distance of TRANSFER.
    :ivar transfer_duration: Timings for the TRANSFER to use in journey
        planning, etc.
    :ivar walk_transfer_duration: Timings for walking over TRANSFER if
        different from the JOURNEY PATTERN  transfer duration,
    :ivar both_ways: Whether timings and validity applies to both
        directions (true) or just to the from-to direction of the
        TRANSFER.
    """
    class Meta:
        name = "Transfer_VersionStructure"

    name: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Name",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    type_of_transfer_ref: Optional[TypeOfTransferRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTransferRef",
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
    distance: Optional[Decimal] = field(
        default=None,
        metadata={
            "name": "Distance",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    transfer_duration: Optional[TransferDurationStructure] = field(
        default=None,
        metadata={
            "name": "TransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    walk_transfer_duration: Optional[TransferDurationStructure] = field(
        default=None,
        metadata={
            "name": "WalkTransferDuration",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    both_ways: Optional[bool] = field(
        default=None,
        metadata={
            "name": "BothWays",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
