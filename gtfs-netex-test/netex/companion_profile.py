from dataclasses import dataclass

from .companion_profile_version_structure import CompanionProfileVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CompanionProfile(CompanionProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
