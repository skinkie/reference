from dataclasses import dataclass
from .link_in_sequence_ref_structure import LinkInSequenceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class PathLinkInSequenceRefStructure(LinkInSequenceRefStructure):
    value: RestrictedVar
