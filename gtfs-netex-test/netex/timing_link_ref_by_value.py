from dataclasses import dataclass
from netex.timing_link_ref_by_value_structure import TimingLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TimingLinkRefByValue(TimingLinkRefByValueStructure):
    """
    Reference to a TIMING LINK LINK BY VALUE.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
