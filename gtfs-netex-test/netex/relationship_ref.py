from dataclasses import dataclass
from .relationship_ref_structure import RelationshipRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class RelationshipRef(RelationshipRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
