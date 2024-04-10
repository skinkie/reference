from dataclasses import dataclass

from .version_version_structure import VersionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class Version(VersionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
