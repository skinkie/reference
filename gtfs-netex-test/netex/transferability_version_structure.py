from dataclasses import dataclass, field
from typing import Optional
from netex.shared_usage_enumeration import SharedUsageEnumeration
from netex.usage_parameter_version_structure import UsageParameterVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TransferabilityVersionStructure(UsageParameterVersionStructure):
    """
    Type for TRANSFERABILITY.

    :ivar can_transfer: Whether ticket can be transferred to another.
    :ivar maximum_number_of_named_transferees: If product can be used by
        a named group, e.g. parents of a family, maximum number of named
        holders allowed.
    :ivar has_transfer_fee: Whether there is a fee for transferring
        ticket or travel document.
    :ivar shared_usage: Indicates the nature of the permitted sharing,
        if any, of products that can be shared, e.g. trips from a multi-
        trip carnet. +v1.1
    """
    class Meta:
        name = "Transferability_VersionStructure"

    can_transfer: Optional[bool] = field(
        default=None,
        metadata={
            "name": "CanTransfer",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    maximum_number_of_named_transferees: Optional[int] = field(
        default=None,
        metadata={
            "name": "MaximumNumberOfNamedTransferees",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    has_transfer_fee: Optional[bool] = field(
        default=None,
        metadata={
            "name": "HasTransferFee",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    shared_usage: Optional[SharedUsageEnumeration] = field(
        default=None,
        metadata={
            "name": "SharedUsage",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
