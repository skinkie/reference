from dataclasses import dataclass

from .alternative_name_ref_structure import AlternativeNameRefStructure

__NAMESPACE__ = "http://www.netex.org.uk/netex"


@dataclass(slots=True, kw_only=True)
class AlternativeNameRef(AlternativeNameRefStructure):
    class Meta:
        namespace = "http://www.netex.org.uk/netex"
