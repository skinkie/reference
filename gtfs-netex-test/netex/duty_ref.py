from dataclasses import dataclass
from netex.duty_ref_structure import DutyRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class DutyRef(DutyRefStructure):
    """
    Reference to a DUTY.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
