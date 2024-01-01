from dataclasses import dataclass
from .commercial_profile_version_structure import (
    CommercialProfileVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class CommercialProfile(CommercialProfileVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
