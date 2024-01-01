from dataclasses import dataclass
from .companion_profile_ref_structure import CompanionProfileRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompanionProfileRef(CompanionProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
