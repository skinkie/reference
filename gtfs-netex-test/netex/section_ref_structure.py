from dataclasses import dataclass
from .link_sequence_ref_structure import LinkSequenceRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class SectionRefStructure(LinkSequenceRefStructure):
    value: RestrictedVar
