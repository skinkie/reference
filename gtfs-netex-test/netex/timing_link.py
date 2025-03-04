from dataclasses import dataclass

from .timing_link_version_structure import TimingLinkVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimingLink(TimingLinkVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
