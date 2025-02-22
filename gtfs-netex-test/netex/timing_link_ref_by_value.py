from dataclasses import dataclass

from .timing_link_ref_by_value_structure import TimingLinkRefByValueStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class TimingLinkRefByValue(TimingLinkRefByValueStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
