from dataclasses import dataclass

from .timing_link_ref_structure import TimingLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimingLinkRef(TimingLinkRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
