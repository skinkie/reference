from dataclasses import dataclass
from .transfer_restriction_version_structure import (
    TransferRestrictionVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class TransferRestriction(TransferRestrictionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
