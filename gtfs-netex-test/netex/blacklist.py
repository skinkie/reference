from dataclasses import dataclass
from .blacklist_version_structure import BlacklistVersionStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Blacklist(BlacklistVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
