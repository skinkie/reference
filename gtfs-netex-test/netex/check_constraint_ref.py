from dataclasses import dataclass
from netex.check_constraint_ref_structure import CheckConstraintRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintRef(CheckConstraintRefStructure):
    """
    Identifier of a CHECK CONSTRAINT.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
