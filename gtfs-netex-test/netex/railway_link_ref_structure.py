from dataclasses import dataclass

from .infrastructure_link_ref_structure import InfrastructureLinkRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RailwayLinkRefStructure(InfrastructureLinkRefStructure):
    pass
