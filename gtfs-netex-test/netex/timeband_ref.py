from dataclasses import dataclass
from netex.timeband_ref_structure import TimebandRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimebandRef(TimebandRefStructure):
    """
    Reference to a TIME BAND.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
