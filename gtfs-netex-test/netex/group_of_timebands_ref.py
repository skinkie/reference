from dataclasses import dataclass
from .group_of_timebands_ref_structure import GroupOfTimebandsRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GroupOfTimebandsRef(GroupOfTimebandsRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
