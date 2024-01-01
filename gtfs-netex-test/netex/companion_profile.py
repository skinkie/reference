from dataclasses import dataclass
from .companion_profile_version_structure import (
    CompanionProfileVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CompanionProfile(CompanionProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
