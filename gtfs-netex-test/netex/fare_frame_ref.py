from dataclasses import dataclass
from netex.fare_frame_ref_structure import FareFrameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class FareFrameRef(FareFrameRefStructure):
    """
    Reference to a FARE FRAME.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
