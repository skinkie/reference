from dataclasses import dataclass, field
from typing import Optional
from netex.codespace_ref import CodespaceRef
from netex.data_sources_rel_structure import DataSourcesRelStructure
from netex.multilingual_string import MultilingualString
from netex.responsibility_role_assignment import ResponsibilityRoleAssignment

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(unsafe_hash=True, kw_only=True)
class TopicStructure:
    """
    Type for abstract Request filter.

    :ivar description: Description of what filter does.
    :ivar sources: Data Sources to include. If more than one source is
        specified it is logically ORed with the others.
    :ivar codespace_ref:
    :ivar responsibility_role_assignment:
    """
    description: Optional[MultilingualString] = field(
        default=None,
        metadata={
            "name": "Description",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    sources: Optional[DataSourcesRelStructure] = field(
        default=None,
        metadata={
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    codespace_ref: Optional[CodespaceRef] = field(
        default=None,
        metadata={
            "name": "CodespaceRef",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
    responsibility_role_assignment: Optional[ResponsibilityRoleAssignment] = field(
        default=None,
        metadata={
            "name": "ResponsibilityRoleAssignment",
            "type": "Element",
            "namespace": "http://www.netex.org.uk/netex",
        }
    )
