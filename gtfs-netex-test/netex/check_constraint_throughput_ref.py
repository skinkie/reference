from dataclasses import dataclass
from netex.check_constraint_throughput_ref_structure import CheckConstraintThroughputRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintThroughputRef(CheckConstraintThroughputRefStructure):
    """
    Identifier of a CHECK CONSTRAINT THROUGHPUT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
