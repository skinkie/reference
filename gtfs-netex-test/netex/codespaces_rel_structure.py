from dataclasses import dataclass, field
from typing import List
from netex.codespace import Codespace
from netex.codespace_ref import CodespaceRef
from netex.one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class CodespacesRelStructure(OneToManyRelationshipStructure):
    """
    A collection of one or more CODESPACEs.
    """
    class Meta:
        name = "codespaces_RelStructure"

    codespace_ref_or_codespace: List[object] = field(
        default_factory=list,
        metadata={
            "type": "Elements",
            "choices": (
                {
                    "name": "CodespaceRef",
                    "type": CodespaceRef,
                    "namespace": "http://www.netex.org.uk/netex",
                },
                {
                    "name": "Codespace",
                    "type": Codespace,
                    "namespace": "http://www.netex.org.uk/netex",
                },
            ),
        }
    )
