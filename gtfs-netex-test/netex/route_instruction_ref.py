from dataclasses import dataclass
from .route_instruction_ref_structure import RouteInstructionRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteInstructionRef(RouteInstructionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
