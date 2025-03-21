from dataclasses import dataclass, field
from typing import Union

from .codespace import Codespace
from .codespace_ref import CodespaceRef
from .one_to_many_relationship_structure import OneToManyRelationshipStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class CodespacesRelStructure(OneToManyRelationshipStructure):
    class Meta:
        name = "codespaces_RelStructure"

    codespace_ref_or_codespace: list[Union[CodespaceRef, Codespace]] = field(
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
        },
    )
