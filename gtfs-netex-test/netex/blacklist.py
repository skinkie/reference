from dataclasses import dataclass

from .blacklist_version_structure import BlacklistVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class Blacklist(BlacklistVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
