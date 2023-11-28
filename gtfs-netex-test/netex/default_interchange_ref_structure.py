from dataclasses import dataclass
from netex.interchange_ref_structure import InterchangeRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DefaultInterchangeRefStructure(InterchangeRefStructure):
    """
    Type for a reference to a DEFAULT INTERCHANGE.
    """
