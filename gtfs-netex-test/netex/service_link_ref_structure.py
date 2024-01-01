from dataclasses import dataclass
from .timing_link_ref_structure import TimingLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class ServiceLinkRefStructure(TimingLinkRefStructure):
    value: RestrictedVar
