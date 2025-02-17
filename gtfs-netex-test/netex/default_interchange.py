from dataclasses import dataclass

from .default_interchange_version_structure import DefaultInterchangeVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DefaultInterchange(DefaultInterchangeVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
