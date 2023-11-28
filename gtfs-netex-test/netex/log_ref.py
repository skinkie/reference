from dataclasses import dataclass
from netex.log_ref_structure import LogRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class LogRef(LogRefStructure):
    """
    Reference to a LOG.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
