from dataclasses import dataclass

from .link_on_section_versioned_child_structure import LinkOnSectionVersionedChildStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class LinkOnSection(LinkOnSectionVersionedChildStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
