from dataclasses import dataclass

from .alternative_text_ref_structure import AlternativeTextRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AlternativeTextRef(AlternativeTextRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
