from dataclasses import dataclass, field
from typing import Optional
from netex.assignment_version_structure_1 import AssignmentVersionStructure1
from netex.scheduled_stop_point_ref_structure import ScheduledStopPointRefStructure
from netex.transfer_constraint_type_enumeration import TransferConstraintTypeEnumeration
from netex.type_of_transfer_ref import TypeOfTransferRef

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferRestrictionVersionStructure(AssignmentVersionStructure1):
    """
    Type for TRANSFER RESTRICTION.

    :ivar type_of_transfer_ref:
    :ivar both_ways: Whether timings and validity applies to both
        directions (true) or just to the from-to direction of the
        TRANSFER.
    :ivar restriction_type: Nature of restriction.
    :ivar from_point_ref: From point of restriction.
    :ivar to_point_ref: From point of restriction.
    """
    class Meta:
        name = "TransferRestriction_VersionStructure"

    type_of_transfer_ref: Optional[TypeOfTransferRef] = field(
        default=None,
        metadata={
            "name": "TypeOfTransferRef",
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
    restriction_type: TransferConstraintTypeEnumeration = field(
        metadata={
            "name": "RestrictionType",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
            "required": True,
        }
    )
    from_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "FromPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    to_point_ref: Optional[ScheduledStopPointRefStructure] = field(
        default=None,
        metadata={
            "name": "ToPointRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
