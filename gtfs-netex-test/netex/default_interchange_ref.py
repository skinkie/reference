from dataclasses import dataclass

from .default_interchange_ref_structure import DefaultInterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class DefaultInterchangeRef(DefaultInterchangeRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
