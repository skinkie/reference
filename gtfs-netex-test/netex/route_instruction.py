from dataclasses import dataclass
from .route_instruction_version_structure import (
    RouteInstructionVersionStructure,
)


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RouteInstruction(RouteInstructionVersionStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
