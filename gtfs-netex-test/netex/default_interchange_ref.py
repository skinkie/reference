from dataclasses import dataclass
from netex.default_interchange_ref_structure import DefaultInterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultInterchangeRef(DefaultInterchangeRefStructure):
    """
    Reference to a DEFAULT INTERCHANGE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
