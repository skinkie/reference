from dataclasses import dataclass
from netex.allowed_line_direction_ref_structure import AllowedLineDirectionRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class AllowedLineDirectionRef(AllowedLineDirectionRefStructure):
    """
    Reference to an ALLOWED LINE DIRECTION.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
