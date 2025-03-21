from dataclasses import dataclass

from .allowed_line_direction_ref_structure import AllowedLineDirectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AllowedLineDirectionRef(AllowedLineDirectionRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
