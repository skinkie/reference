from dataclasses import dataclass
from netex.relationship_ref_structure import RelationshipRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class RelationshipRef(RelationshipRefStructure):
    """
    Reference to a Relationship.
    """
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
