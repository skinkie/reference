from dataclasses import dataclass

from .generic_path_junction_version_structure import GenericPathJunctionVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericPathJunction(GenericPathJunctionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
