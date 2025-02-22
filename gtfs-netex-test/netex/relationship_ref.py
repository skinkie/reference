from dataclasses import dataclass

from .relationship_ref_structure import RelationshipRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class RelationshipRef(RelationshipRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
