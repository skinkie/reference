from dataclasses import dataclass, field
from netex.check_constraint_throughput_version_structure import CheckConstraintThroughputVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CheckConstraintThroughput(CheckConstraintThroughputVersionStructure):
    """Throughput of a CHECK CONSTRAINT.

    the number of passengers who can pass through it.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"

    id: str = field(
        metadata={
            "type": "Attribute",
            "required": True,
        }
    )
