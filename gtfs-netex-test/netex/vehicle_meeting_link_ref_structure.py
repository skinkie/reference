from dataclasses import dataclass
from .link_ref_structure import LinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class VehicleMeetingLinkRefStructure(LinkRefStructure):
    value: RestrictedVar
