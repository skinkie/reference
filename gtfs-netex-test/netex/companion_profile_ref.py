from dataclasses import dataclass

from .companion_profile_ref_structure import CompanionProfileRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CompanionProfileRef(CompanionProfileRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
