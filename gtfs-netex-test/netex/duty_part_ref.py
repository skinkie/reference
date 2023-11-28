from dataclasses import dataclass
from netex.duty_part_ref_structure import DutyPartRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DutyPartRef(DutyPartRefStructure):
    """
    Reference to a DUTY PART.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
