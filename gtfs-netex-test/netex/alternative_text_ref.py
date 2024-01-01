from dataclasses import dataclass
from .alternative_text_ref_structure import AlternativeTextRefStructure


from typing import ClassVar as RestrictedVar

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(kw_only=True)
class AlternativeTextRef(AlternativeTextRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
