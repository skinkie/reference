from dataclasses import dataclass

from .sections_in_sequence_rel_structure import LinkSequenceVersionStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class GenericNavigationPathVersionStructure(LinkSequenceVersionStructure):
    class Meta:
        name = "GenericNavigationPath_VersionStructure"
