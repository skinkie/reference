from dataclasses import dataclass
from .infrastructure_link_ref_structure import InfrastructureLinkRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RailwayLinkRefStructure(InfrastructureLinkRefStructure):
    value: RestrictedVar
